"""
Example: AI Medical Assistant
Demonstrates how to use Huggingface AI for medical queries
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.integrations import HuggingfaceIntegration
from dotenv import load_dotenv

load_dotenv()


def main():
    """Main function"""
    print("🤖 Huggingface AI Medical Assistant Example\n")
    
    # Initialize Huggingface integration
    hf = HuggingfaceIntegration()
    
    # Example queries
    queries = [
        "¿Cuáles son los síntomas comunes de la diabetes?",
        "¿Qué es la hipertensión arterial?",
        "¿Cómo prevenir enfermedades cardiovasculares?",
    ]
    
    print("Generating AI responses for medical queries...\n")
    
    for i, query in enumerate(queries, 1):
        print(f"{i}️⃣  Query: {query}")
        print("   Generating response...")
        
        # This would work with proper API key and model
        # response = hf.generate_medical_response(query, max_length=150)
        # print(f"   Response: {response}\n")
        
        print(f"   ⚠️  Configure HUGGINGFACE_API_KEY to get real responses\n")
    
    # Get model info
    print("📊 Model Information:")
    model_info = hf.get_model_info()
    print(f"   Model ID: {model_info.get('id', 'Not configured')}")
    
    print("\n✅ Example completed!")


if __name__ == "__main__":
    main()
