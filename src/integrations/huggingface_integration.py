"""
Huggingface Integration for Medical AI
Provides AI-powered medical assistance using Huggingface models
"""
import os
from typing import Optional, Dict, Any
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import HfApi, login
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)


class HuggingfaceIntegration:
    """Integration with Huggingface for medical AI capabilities"""
    
    def __init__(self, api_key: Optional[str] = None, model_id: Optional[str] = None):
        """
        Initialize Huggingface integration
        
        Args:
            api_key: Huggingface API key
            model_id: Model ID to use for medical AI
        """
        self.api_key = api_key or os.getenv("HUGGINGFACE_API_KEY")
        self.model_id = model_id or os.getenv("HUGGINGFACE_MODEL_ID", "microsoft/BioGPT-Large")
        self.api = None
        self.model = None
        self.tokenizer = None
        self.pipeline = None
        
        if self.api_key:
            login(token=self.api_key)
            self.api = HfApi()
            logger.info("Huggingface API initialized")
    
    def load_medical_model(self):
        """Load medical AI model"""
        try:
            logger.info(f"Loading medical model: {self.model_id}")
            # Use a text-generation pipeline for medical queries
            self.pipeline = pipeline(
                "text-generation",
                model=self.model_id,
                device=-1  # Use CPU, change to 0 for GPU
            )
            logger.info("Medical model loaded successfully")
            return True
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            return False
    
    def generate_medical_response(self, query: str, max_length: int = 200) -> str:
        """
        Generate medical response using AI
        
        Args:
            query: Medical query
            max_length: Maximum response length
            
        Returns:
            AI-generated medical response
        """
        try:
            if not self.pipeline:
                self.load_medical_model()
            
            response = self.pipeline(
                query,
                max_length=max_length,
                num_return_sequences=1,
                temperature=0.7
            )
            
            return response[0]['generated_text']
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return f"Error: {str(e)}"
    
    def analyze_medical_text(self, text: str) -> Dict[str, Any]:
        """
        Analyze medical text for insights
        
        Args:
            text: Medical text to analyze
            
        Returns:
            Analysis results
        """
        try:
            # Simple sentiment analysis for medical context
            sentiment_pipeline = pipeline("sentiment-analysis")
            sentiment = sentiment_pipeline(text[:512])[0]  # Limit length
            
            return {
                "text": text,
                "sentiment": sentiment,
                "length": len(text),
                "word_count": len(text.split())
            }
        except Exception as e:
            logger.error(f"Error analyzing text: {str(e)}")
            return {"error": str(e)}
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current model"""
        try:
            if self.api:
                model_info = self.api.model_info(self.model_id)
                return {
                    "id": model_info.id,
                    "author": model_info.author,
                    "downloads": model_info.downloads,
                    "likes": model_info.likes,
                    "tags": model_info.tags
                }
            return {"error": "API not initialized"}
        except Exception as e:
            logger.error(f"Error getting model info: {str(e)}")
            return {"error": str(e)}
