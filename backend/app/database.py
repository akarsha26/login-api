"""
Database connection and configuration using Motor (async MongoDB driver)
"""
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    mongodb_uri: str
    mongodb_db_name: str = "login_app"
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7
    environment: str = "development"
    api_prefix: str = "/api"
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    email_from: str = ""
    frontend_url: str = "http://localhost:3000"  # Frontend URL for email links
    rate_limit_per_minute: int = 60
    cache_ttl_seconds: int = 300

    class Config:
        # Don't require .env file on Vercel (uses environment variables)
        env_file = ".env" if os.path.exists(".env") else None
        case_sensitive = False


# Load settings - handle missing env vars gracefully for Vercel
try:
    settings = Settings()
except Exception as e:
    print(f"Warning: Settings loading failed: {e}")
    print("Will use environment variables directly")
    # Create a minimal settings object
    import os
    class MinimalSettings:
        mongodb_uri = os.getenv("MONGODB_URI", "")
        mongodb_db_name = os.getenv("MONGODB_DB_NAME", "login_app")
        jwt_secret_key = os.getenv("JWT_SECRET_KEY", "")
        jwt_algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        jwt_access_token_expire_minutes = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
        jwt_refresh_token_expire_days = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", "7"))
        smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_user = os.getenv("SMTP_USER", "")
        smtp_password = os.getenv("SMTP_PASSWORD", "")
        email_from = os.getenv("EMAIL_FROM", "")
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
    settings = MinimalSettings()

# Global database client
client: Optional[AsyncIOMotorClient] = None
database = None


async def connect_to_mongo():
    """Create database connection"""
    global client, database
    try:
        from urllib.parse import quote, urlparse, urlunparse
        
        # URL encode password if it contains special characters
        uri = settings.mongodb_uri
        parsed = urlparse(uri)
        
        if parsed.password and ('<' in parsed.password or '>' in parsed.password or '@' in parsed.password):
            # Encode password
            encoded_password = quote(parsed.password, safe='')
            netloc = f"{parsed.username}:{encoded_password}@{parsed.hostname}"
            if parsed.port:
                netloc += f":{parsed.port}"
            uri = urlunparse((parsed.scheme, netloc, parsed.path, parsed.params, parsed.query, parsed.fragment))
        
        client = AsyncIOMotorClient(
            uri,
            serverSelectionTimeoutMS=20000,
            connectTimeoutMS=20000,
            socketTimeoutMS=20000
        )
        # Test the connection
        await client.admin.command('ping')
        database = client[settings.mongodb_db_name]
        print(f"[SUCCESS] Connected to MongoDB: {settings.mongodb_db_name}")
        return database
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise


async def close_mongo_connection():
    """Close database connection"""
    global client
    if client:
        client.close()
        print("[INFO] MongoDB connection closed")


async def get_database():
    """Get database instance - lazy connection for Vercel"""
    global database
    if database is None:
        try:
            await connect_to_mongo()
            # Create indexes on first connection (after database is set)
            await create_indexes()
        except Exception as e:
            print(f"Database connection error: {e}")
            raise
    return database


async def create_indexes():
    """Create database indexes for better performance"""
    try:
        # Get database directly (not through get_database to avoid circular dependency)
        global database
        if database is None:
            return  # Database not connected yet
        
        # Create indexes on users collection
        users_collection = database.users
        
        # Unique index on email (ignore if already exists)
        try:
            await users_collection.create_index("email", unique=True)
        except Exception:
            pass  # Index might already exist
        
        # Unique index on phone_number
        try:
            await users_collection.create_index("phone_number", unique=True, sparse=True)
        except Exception:
            pass
        
        # Index on is_active for faster queries
        try:
            await users_collection.create_index("is_active")
        except Exception:
            pass
        
        # Index on created_at for sorting
        try:
            await users_collection.create_index("created_at")
        except Exception:
            pass
        
        print("[SUCCESS] Database indexes created/verified")
    except Exception as e:
        print(f"Warning: Index creation failed (may already exist): {e}")
