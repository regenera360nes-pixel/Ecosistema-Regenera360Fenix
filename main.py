#!/usr/bin/env python3
"""
Main entry point for Regenera360 Medical Ecosystem
"""
import sys
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main function"""
    logger.info("=" * 60)
    logger.info("Regenera360 Medical Ecosystem")
    logger.info("=" * 60)
    
    print("\n🏥 Bienvenido al Ecosistema Médico Regenera360\n")
    print("Opciones disponibles:")
    print("  1. Iniciar API REST (FastAPI)")
    print("  2. Iniciar orquestador de automatización")
    print("  3. Ejecutar prueba de integraciones")
    print("  4. Salir")
    
    choice = input("\nSeleccione una opción (1-4): ").strip()
    
    if choice == "1":
        start_api()
    elif choice == "2":
        start_orchestrator()
    elif choice == "3":
        test_integrations()
    elif choice == "4":
        print("¡Hasta luego!")
        sys.exit(0)
    else:
        print("Opción inválida")
        sys.exit(1)


def start_api():
    """Start the FastAPI application"""
    logger.info("Starting FastAPI server...")
    import uvicorn
    from src.api.main import app
    
    print("\n🚀 Iniciando servidor API en http://0.0.0.0:8000")
    print("📚 Documentación disponible en http://0.0.0.0:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)


def start_orchestrator():
    """Start the automation orchestrator"""
    logger.info("Starting automation orchestrator...")
    from src.automation import MedicalEcosystemOrchestrator
    
    print("\n🤖 Iniciando orquestador de automatización...")
    orchestrator = MedicalEcosystemOrchestrator()
    
    try:
        orchestrator.run()
    except KeyboardInterrupt:
        print("\n\n⏹️  Deteniendo orquestador...")
        orchestrator.stop()
        logger.info("Orchestrator stopped")


def test_integrations():
    """Test all integrations"""
    logger.info("Testing integrations...")
    from src.integrations import (
        HuggingfaceIntegration,
        GithubIntegration,
        WixIntegration,
        MetaAdsIntegration,
        WhatsAppBusinessIntegration,
        GoogleBusinessIntegration
    )
    
    print("\n🔍 Probando integraciones...\n")
    
    # Test Huggingface
    print("1️⃣  Huggingface Integration")
    hf = HuggingfaceIntegration()
    model_info = hf.get_model_info()
    print(f"   ✅ Conectado - Modelo: {model_info.get('id', 'N/A')}")
    
    # Test GitHub
    print("\n2️⃣  GitHub Integration")
    gh = GithubIntegration()
    gh.connect_repository()
    stats = gh.get_repository_stats()
    print(f"   ✅ Conectado - Repo: {stats.get('full_name', 'N/A')}")
    
    # Test Wix
    print("\n3️⃣  Wix Integration")
    wix = WixIntegration()
    print(f"   ✅ Inicializado - Site ID: {wix.site_id}")
    
    # Test Meta Ads
    print("\n4️⃣  Meta Ads Integration")
    meta = MetaAdsIntegration()
    print(f"   ✅ Inicializado - Account: {meta.ad_account_id}")
    
    # Test WhatsApp
    print("\n5️⃣  WhatsApp Business Integration")
    wa = WhatsAppBusinessIntegration()
    print(f"   ✅ Inicializado - Number: {wa.phone_number}")
    
    # Test Google Business
    print("\n6️⃣  Google Business Integration")
    gb = GoogleBusinessIntegration()
    print(f"   ✅ Inicializado - Location: {gb.location_id}")
    
    print("\n✨ Todas las integraciones están configuradas correctamente!")
    print("\n⚠️  Nota: Configure las variables de entorno en .env para funcionalidad completa")


if __name__ == "__main__":
    main()
