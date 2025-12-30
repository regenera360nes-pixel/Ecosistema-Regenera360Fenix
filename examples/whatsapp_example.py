"""
Example: Send WhatsApp Messages
Demonstrates how to send messages using the WhatsApp integration
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.integrations import WhatsAppBusinessIntegration
from dotenv import load_dotenv

load_dotenv()


def main():
    """Main function"""
    print("📱 WhatsApp Business Integration Example\n")
    
    # Initialize WhatsApp integration
    whatsapp = WhatsAppBusinessIntegration()
    
    # Example 1: Send simple message
    print("1️⃣  Sending simple message...")
    # recipient = "whatsapp:+1234567890"  # Replace with actual number
    # message_sid = whatsapp.send_message(
    #     to=recipient,
    #     body="Hola! Este es un mensaje de prueba desde Regenera360."
    # )
    # print(f"   Message sent: {message_sid}")
    
    # Example 2: Send appointment reminder
    print("\n2️⃣  Sending appointment reminder...")
    # message_sid = whatsapp.send_appointment_reminder(
    #     to=recipient,
    #     patient_name="Juan Pérez",
    #     appointment_date="2025-01-15",
    #     appointment_time="10:00 AM"
    # )
    # print(f"   Reminder sent: {message_sid}")
    
    # Example 3: Send health tip
    print("\n3️⃣  Sending health tip...")
    health_tip = """
    Mantente hidratado: Bebe al menos 8 vasos de agua al día para mantener 
    tu cuerpo funcionando correctamente y mejorar tu salud general.
    """
    # message_sid = whatsapp.send_health_tip(
    #     to=recipient,
    #     tip=health_tip.strip()
    # )
    # print(f"   Health tip sent: {message_sid}")
    
    print("\n✅ Examples completed!")
    print("⚠️  Uncomment the code and add real phone numbers to test")


if __name__ == "__main__":
    main()
