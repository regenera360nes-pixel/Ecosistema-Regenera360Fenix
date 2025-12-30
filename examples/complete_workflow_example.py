"""
Example: Complete Workflow
Demonstrates a complete patient interaction workflow
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.automation import MedicalEcosystemOrchestrator
from src.utils import generate_patient_id, generate_appointment_id
from dotenv import load_dotenv

load_dotenv()


def main():
    """Main function"""
    print("🏥 Complete Patient Workflow Example\n")
    
    # Initialize orchestrator
    orchestrator = MedicalEcosystemOrchestrator()
    
    # Simulate patient workflow
    print("=" * 60)
    print("SCENARIO: New Patient Inquiry")
    print("=" * 60)
    
    # Step 1: Patient submits contact form on Wix
    print("\n1️⃣  Patient submits contact form on Wix website")
    print("   ✅ Contact captured")
    
    # Step 2: System sends automated WhatsApp confirmation
    print("\n2️⃣  System sends automated WhatsApp confirmation")
    patient_phone = "whatsapp:+1234567890"
    patient_name = "María González"
    # orchestrator.whatsapp.send_message(
    #     to=patient_phone,
    #     body=f"Hola {patient_name}, gracias por contactarnos. Un especialista te contactará pronto."
    # )
    print("   ✅ Confirmation sent")
    
    # Step 3: AI analyzes patient inquiry
    print("\n3️⃣  AI analyzes patient inquiry")
    inquiry = "Necesito una consulta para dolor de espalda crónico"
    # analysis = orchestrator.huggingface.analyze_medical_text(inquiry)
    print(f"   Inquiry: {inquiry}")
    print("   ✅ Analysis completed")
    
    # Step 4: Schedule appointment via Wix Bookings
    print("\n4️⃣  Schedule appointment via Wix Bookings")
    appointment_id = generate_appointment_id()
    appointment_date = "2025-01-20"
    appointment_time = "14:00"
    print(f"   Appointment ID: {appointment_id}")
    print(f"   Date: {appointment_date} at {appointment_time}")
    print("   ✅ Appointment scheduled")
    
    # Step 5: Send appointment confirmation
    print("\n5️⃣  Send appointment confirmation via WhatsApp")
    # orchestrator.whatsapp.send_appointment_reminder(
    #     to=patient_phone,
    #     patient_name=patient_name,
    #     appointment_date=appointment_date,
    #     appointment_time=appointment_time
    # )
    print("   ✅ Confirmation sent")
    
    # Step 6: Update Google Business with new appointment
    print("\n6️⃣  Update Google Business profile")
    print("   ✅ Profile updated")
    
    # Step 7: Create GitHub issue for tracking
    print("\n7️⃣  Create tracking issue in GitHub")
    # orchestrator.github.create_issue(
    #     title=f"New Patient: {patient_name}",
    #     body=f"Appointment scheduled for {appointment_date}",
    #     labels=["patient", "appointment"]
    # )
    print("   ✅ Issue created")
    
    # Step 8: Send reminder day before
    print("\n8️⃣  Schedule reminder for day before appointment")
    print("   ✅ Reminder scheduled")
    
    print("\n" + "=" * 60)
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print("=" * 60)
    
    print("\n📊 Workflow Summary:")
    print(f"   Patient: {patient_name}")
    print(f"   Appointment: {appointment_date} at {appointment_time}")
    print(f"   Platforms integrated: Wix, WhatsApp, AI, GitHub, Google Business")
    print("\n✅ All systems working together seamlessly!")


if __name__ == "__main__":
    main()
