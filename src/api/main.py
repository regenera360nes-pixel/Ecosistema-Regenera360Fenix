"""
FastAPI REST API for Medical Ecosystem
Provides endpoints for all integrations and automation
"""
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict, Any, List
from pydantic import BaseModel
from datetime import datetime
import logging

from ..integrations import (
    HuggingfaceIntegration,
    GithubIntegration,
    WixIntegration,
    MetaAdsIntegration,
    WhatsAppBusinessIntegration,
    GoogleBusinessIntegration
)
from ..automation import MedicalEcosystemOrchestrator
from ..models import Patient, Appointment, HealthTip, Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Regenera360 Medical Ecosystem API",
    description="API integrada para ecosistema médico con IA",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize orchestrator
orchestrator = MedicalEcosystemOrchestrator()


class AIQueryRequest(BaseModel):
    """AI query request model"""
    query: str
    max_length: Optional[int] = 200


class MessageRequest(BaseModel):
    """WhatsApp message request model"""
    to: str
    body: str
    media_url: Optional[str] = None


class AppointmentReminderRequest(BaseModel):
    """Appointment reminder request model"""
    to: str
    patient_name: str
    appointment_date: str
    appointment_time: str


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Regenera360 Medical Ecosystem API",
        "version": "1.0.0",
        "status": "active"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


# AI Endpoints
@app.post("/ai/query")
async def ai_query(request: AIQueryRequest):
    """Query AI for medical information"""
    try:
        response = orchestrator.huggingface.generate_medical_response(
            request.query,
            max_length=request.max_length
        )
        return {"query": request.query, "response": response}
    except Exception as e:
        logger.error(f"AI query error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ai/analyze")
async def analyze_text(text: str):
    """Analyze medical text"""
    try:
        analysis = orchestrator.huggingface.analyze_medical_text(text)
        return analysis
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# WhatsApp Endpoints
@app.post("/whatsapp/send")
async def send_whatsapp_message(request: MessageRequest):
    """Send WhatsApp message"""
    try:
        message_sid = orchestrator.whatsapp.send_message(
            to=request.to,
            body=request.body,
            media_url=request.media_url
        )
        return {"message_sid": message_sid, "status": "sent"}
    except Exception as e:
        logger.error(f"WhatsApp send error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/whatsapp/appointment-reminder")
async def send_appointment_reminder(request: AppointmentReminderRequest):
    """Send appointment reminder via WhatsApp"""
    try:
        message_sid = orchestrator.whatsapp.send_appointment_reminder(
            to=request.to,
            patient_name=request.patient_name,
            appointment_date=request.appointment_date,
            appointment_time=request.appointment_time
        )
        return {"message_sid": message_sid, "status": "sent"}
    except Exception as e:
        logger.error(f"Reminder send error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Wix Endpoints
@app.get("/wix/site-info")
async def get_wix_site_info():
    """Get Wix site information"""
    try:
        info = orchestrator.wix.get_site_info()
        return info
    except Exception as e:
        logger.error(f"Wix site info error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/wix/contacts")
async def get_wix_contacts():
    """Get Wix contact submissions"""
    try:
        contacts = orchestrator.wix.get_contact_submissions()
        return {"contacts": contacts, "count": len(contacts)}
    except Exception as e:
        logger.error(f"Wix contacts error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Meta Ads Endpoints
@app.get("/meta/campaigns")
async def get_meta_campaigns(status: Optional[str] = None):
    """Get Meta Ads campaigns"""
    try:
        campaigns = orchestrator.meta_ads.get_campaigns(status=status)
        return {"campaigns": campaigns, "count": len(campaigns)}
    except Exception as e:
        logger.error(f"Meta campaigns error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/meta/insights")
async def get_meta_insights():
    """Get Meta Ads account insights"""
    try:
        insights = orchestrator.meta_ads.get_account_insights()
        return insights
    except Exception as e:
        logger.error(f"Meta insights error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Google Business Endpoints
@app.get("/google/location")
async def get_google_location():
    """Get Google Business location info"""
    try:
        location = orchestrator.google_business.get_location_info()
        return location
    except Exception as e:
        logger.error(f"Google location error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/google/insights")
async def get_google_insights():
    """Get Google Business insights"""
    try:
        insights = orchestrator.google_business.get_insights()
        return insights
    except Exception as e:
        logger.error(f"Google insights error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# GitHub Endpoints
@app.get("/github/stats")
async def get_github_stats():
    """Get GitHub repository statistics"""
    try:
        stats = orchestrator.github.get_repository_stats()
        return stats
    except Exception as e:
        logger.error(f"GitHub stats error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/github/issues")
async def get_github_issues(state: str = "open"):
    """Get GitHub issues"""
    try:
        issues = orchestrator.github.list_issues(state=state)
        return {"issues": [{"number": i.number, "title": i.title} for i in issues]}
    except Exception as e:
        logger.error(f"GitHub issues error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Automation Endpoints
@app.post("/automation/daily-tips")
async def trigger_daily_tips(background_tasks: BackgroundTasks):
    """Trigger daily health tips sending"""
    background_tasks.add_task(orchestrator.send_daily_health_tips)
    return {"status": "scheduled", "message": "Daily health tips will be sent"}


@app.post("/automation/daily-report")
async def trigger_daily_report():
    """Generate daily report"""
    try:
        report = orchestrator.generate_daily_report()
        return report
    except Exception as e:
        logger.error(f"Daily report error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/automation/patient-inquiry")
async def handle_patient_inquiry(patient_id: str, inquiry: str):
    """Handle patient inquiry with AI"""
    try:
        response = orchestrator.handle_patient_inquiry(patient_id, inquiry)
        return response
    except Exception as e:
        logger.error(f"Patient inquiry error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
