"""
Data Models for Medical Ecosystem
"""
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class Patient(BaseModel):
    """Patient model"""
    id: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    medical_history: Optional[List[str]] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)


class Appointment(BaseModel):
    """Appointment model"""
    id: str
    patient_id: str
    service_id: str
    appointment_date: str
    appointment_time: str
    status: str = "scheduled"  # scheduled, confirmed, completed, cancelled
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)


class HealthTip(BaseModel):
    """Health tip model"""
    id: str
    title: str
    content: str
    category: str  # nutrition, exercise, mental_health, etc.
    target_audience: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)


class MarketingCampaign(BaseModel):
    """Marketing campaign model"""
    id: str
    name: str
    platform: str  # meta, google, etc.
    objective: str
    budget: float
    status: str = "draft"
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)


class Message(BaseModel):
    """Message model"""
    id: str
    sender_id: str
    recipient_id: str
    platform: str  # whatsapp, email, etc.
    content: str
    status: str = "sent"
    sent_at: datetime = Field(default_factory=datetime.now)


class AnalyticsReport(BaseModel):
    """Analytics report model"""
    id: str
    report_type: str  # daily, weekly, monthly
    start_date: str
    end_date: str
    metrics: dict
    generated_at: datetime = Field(default_factory=datetime.now)
