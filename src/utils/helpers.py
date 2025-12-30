"""
Utility functions for the medical ecosystem
"""
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any


def generate_patient_id() -> str:
    """Generate unique patient ID"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = secrets.token_hex(4)
    return f"PAT-{timestamp}-{random_suffix}"


def generate_appointment_id() -> str:
    """Generate unique appointment ID"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = secrets.token_hex(4)
    return f"APT-{timestamp}-{random_suffix}"


def format_phone_number(phone: str) -> str:
    """
    Format phone number for WhatsApp
    
    Args:
        phone: Phone number
        
    Returns:
        Formatted phone number
    """
    # Remove all non-digit characters
    phone = ''.join(filter(str.isdigit, phone))
    
    # Add whatsapp: prefix if not present
    if not phone.startswith('whatsapp:'):
        phone = f'whatsapp:+{phone}'
    
    return phone


def hash_sensitive_data(data: str) -> str:
    """
    Hash sensitive data for storage
    
    Args:
        data: Data to hash
        
    Returns:
        Hashed data
    """
    return hashlib.sha256(data.encode()).hexdigest()


def calculate_age(date_of_birth: str) -> Optional[int]:
    """
    Calculate age from date of birth
    
    Args:
        date_of_birth: Date of birth in YYYY-MM-DD format
        
    Returns:
        Age in years
    """
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
    except ValueError:
        return None


def get_next_business_day(days_ahead: int = 1) -> str:
    """
    Get next business day
    
    Args:
        days_ahead: Number of days ahead
        
    Returns:
        Date string in YYYY-MM-DD format
    """
    current_date = datetime.now()
    days_added = 0
    
    while days_added < days_ahead:
        current_date += timedelta(days=1)
        # Skip weekends (Saturday=5, Sunday=6)
        if current_date.weekday() < 5:
            days_added += 1
    
    return current_date.strftime("%Y-%m-%d")


def sanitize_text(text: str) -> str:
    """
    Sanitize text for safe storage and display
    
    Args:
        text: Text to sanitize
        
    Returns:
        Sanitized text
    """
    # Remove potentially harmful characters
    unsafe_chars = ['<', '>', '"', "'", '&']
    for char in unsafe_chars:
        text = text.replace(char, '')
    
    return text.strip()


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Format currency amount
    
    Args:
        amount: Amount to format
        currency: Currency code
        
    Returns:
        Formatted currency string
    """
    if currency == "USD":
        return f"${amount:,.2f}"
    elif currency == "EUR":
        return f"€{amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"
