"""
WhatsApp Business Integration for Messaging Automation
Manages WhatsApp Business messaging using Twilio
"""
import os
from typing import Optional, Dict, Any, List
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv
import logging

# Use relative import instead of sys.path manipulation
from ..utils.helpers import format_phone_number

load_dotenv()
logger = logging.getLogger(__name__)


class WhatsAppBusinessIntegration:
    """Integration with WhatsApp Business API via Twilio"""
    
    def __init__(self, account_sid: Optional[str] = None, auth_token: Optional[str] = None,
                 phone_number: Optional[str] = None):
        """
        Initialize WhatsApp Business integration
        
        Args:
            account_sid: Twilio account SID
            auth_token: Twilio auth token
            phone_number: WhatsApp Business phone number
        """
        self.account_sid = account_sid or os.getenv("WHATSAPP_ACCOUNT_SID")
        self.auth_token = auth_token or os.getenv("WHATSAPP_AUTH_TOKEN")
        self.phone_number = phone_number or os.getenv("WHATSAPP_PHONE_NUMBER")
        
        if self.account_sid and self.auth_token:
            self.client = Client(self.account_sid, self.auth_token)
            logger.info("WhatsApp Business API initialized")
    
    def send_message(self, to: str, body: str, media_url: Optional[str] = None) -> Optional[str]:
        """
        Send a WhatsApp message
        
        Args:
            to: Recipient phone number (format: whatsapp:+1234567890)
            body: Message body
            media_url: Optional media URL
            
        Returns:
            Message SID if successful
        """
        try:
            # Format phone number properly
            to = format_phone_number(to)
            
            params = {
                'from_': self.phone_number,
                'to': to,
                'body': body
            }
            
            if media_url:
                params['media_url'] = [media_url]
            
            message = self.client.messages.create(**params)
            logger.info(f"Sent WhatsApp message: {message.sid}")
            return message.sid
        except TwilioRestException as e:
            logger.error(f"Error sending message: {str(e)}")
            return None
    
    def send_template_message(self, to: str, template_name: str, 
                            template_params: Optional[List[str]] = None) -> Optional[str]:
        """
        Send a WhatsApp template message
        
        Args:
            to: Recipient phone number
            template_name: Template name
            template_params: Template parameters
            
        Returns:
            Message SID if successful
        """
        try:
            # Format phone number properly
            to = format_phone_number(to)
            
            # Template format depends on your approved templates
            body = f"Template: {template_name}"
            if template_params:
                body += f" - Params: {', '.join(template_params)}"
            
            message = self.client.messages.create(
                from_=self.phone_number,
                to=to,
                body=body
            )
            logger.info(f"Sent template message: {message.sid}")
            return message.sid
        except TwilioRestException as e:
            logger.error(f"Error sending template message: {str(e)}")
            return None
    
    def get_message_status(self, message_sid: str) -> Optional[Dict[str, Any]]:
        """
        Get message status
        
        Args:
            message_sid: Message SID
            
        Returns:
            Message status information
        """
        try:
            message = self.client.messages(message_sid).fetch()
            return {
                'sid': message.sid,
                'status': message.status,
                'to': message.to,
                'from': message.from_,
                'body': message.body,
                'date_sent': str(message.date_sent),
                'error_code': message.error_code,
                'error_message': message.error_message
            }
        except TwilioRestException as e:
            logger.error(f"Error getting message status: {str(e)}")
            return None
    
    def send_appointment_reminder(self, to: str, patient_name: str, 
                                 appointment_date: str, appointment_time: str) -> Optional[str]:
        """
        Send appointment reminder
        
        Args:
            to: Patient phone number
            patient_name: Patient name
            appointment_date: Appointment date
            appointment_time: Appointment time
            
        Returns:
            Message SID if successful
        """
        message_body = f"""
Hola {patient_name},

Este es un recordatorio de tu cita médica:

📅 Fecha: {appointment_date}
🕐 Hora: {appointment_time}

Por favor, llega 10 minutos antes.

Para cancelar o reprogramar, responde a este mensaje.

Regenera360 - Tu salud es nuestra prioridad
        """.strip()
        
        return self.send_message(to, message_body)
    
    def send_health_tip(self, to: str, tip: str) -> Optional[str]:
        """
        Send health tip to patient
        
        Args:
            to: Patient phone number
            tip: Health tip content
            
        Returns:
            Message SID if successful
        """
        message_body = f"""
💡 Consejo de Salud del Día

{tip}

Regenera360 - Cuidando tu bienestar
        """.strip()
        
        return self.send_message(to, message_body)
