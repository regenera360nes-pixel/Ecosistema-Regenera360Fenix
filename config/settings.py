"""
Application Settings Configuration
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "Regenera360 Medical Ecosystem"
    APP_VERSION: str = "1.0.0"
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # Huggingface
    HUGGINGFACE_API_KEY: Optional[str] = os.getenv("HUGGINGFACE_API_KEY")
    HUGGINGFACE_MODEL_ID: str = os.getenv("HUGGINGFACE_MODEL_ID", "microsoft/BioGPT-Large")
    
    # GitHub
    GITHUB_TOKEN: Optional[str] = os.getenv("GITHUB_TOKEN")
    GITHUB_REPO_OWNER: str = os.getenv("GITHUB_REPO_OWNER", "regenera360nes-pixel")
    GITHUB_REPO_NAME: str = os.getenv("GITHUB_REPO_NAME", "Ecosistema-Regenera360Fenix")
    
    # Wix
    WIX_API_KEY: Optional[str] = os.getenv("WIX_API_KEY")
    WIX_SITE_ID: Optional[str] = os.getenv("WIX_SITE_ID")
    WIX_ACCOUNT_ID: Optional[str] = os.getenv("WIX_ACCOUNT_ID")
    
    # Meta/Facebook Ads
    META_ACCESS_TOKEN: Optional[str] = os.getenv("META_ACCESS_TOKEN")
    META_APP_ID: Optional[str] = os.getenv("META_APP_ID")
    META_APP_SECRET: Optional[str] = os.getenv("META_APP_SECRET")
    META_AD_ACCOUNT_ID: Optional[str] = os.getenv("META_AD_ACCOUNT_ID")
    
    # WhatsApp Business (Twilio)
    WHATSAPP_ACCOUNT_SID: Optional[str] = os.getenv("WHATSAPP_ACCOUNT_SID")
    WHATSAPP_AUTH_TOKEN: Optional[str] = os.getenv("WHATSAPP_AUTH_TOKEN")
    WHATSAPP_PHONE_NUMBER: Optional[str] = os.getenv("WHATSAPP_PHONE_NUMBER")
    
    # Google Business
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    GOOGLE_BUSINESS_ACCOUNT_ID: Optional[str] = os.getenv("GOOGLE_BUSINESS_ACCOUNT_ID")
    GOOGLE_LOCATION_ID: Optional[str] = os.getenv("GOOGLE_LOCATION_ID")
    
    # Redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_DB: int = int(os.getenv("REDIS_DB", "0"))
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./regenera360.db")
    
    class Config:
        case_sensitive = True


settings = Settings()
