"""
Wix Integration for Website Management
Manages Wix website content and automation
"""
import os
from typing import Optional, Dict, Any, List
import requests
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)


class WixIntegration:
    """Integration with Wix for website management"""
    
    def __init__(self, api_key: Optional[str] = None, site_id: Optional[str] = None):
        """
        Initialize Wix integration
        
        Args:
            api_key: Wix API key
            site_id: Wix site ID
        """
        self.api_key = api_key or os.getenv("WIX_API_KEY")
        self.site_id = site_id or os.getenv("WIX_SITE_ID")
        self.account_id = os.getenv("WIX_ACCOUNT_ID")
        self.base_url = "https://www.wixapis.com"
        self.headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }
        logger.info("Wix integration initialized")
    
    def get_site_info(self) -> Dict[str, Any]:
        """Get Wix site information"""
        try:
            url = f"{self.base_url}/v1/sites/{self.site_id}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error getting site info: {str(e)}")
            return {"error": str(e)}
    
    def update_site_content(self, page_id: str, content: Dict[str, Any]) -> bool:
        """
        Update content on a Wix page
        
        Args:
            page_id: Page ID to update
            content: Content to update
            
        Returns:
            Success status
        """
        try:
            url = f"{self.base_url}/v1/sites/{self.site_id}/pages/{page_id}"
            response = requests.patch(url, headers=self.headers, json=content)
            response.raise_for_status()
            logger.info(f"Updated page: {page_id}")
            return True
        except requests.RequestException as e:
            logger.error(f"Error updating page: {str(e)}")
            return False
    
    def create_blog_post(self, title: str, content: str, tags: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
        """
        Create a blog post
        
        Args:
            title: Post title
            content: Post content
            tags: Post tags
            
        Returns:
            Created post data
        """
        try:
            url = f"{self.base_url}/v3/posts"
            data = {
                "post": {
                    "title": title,
                    "content": content,
                    "tags": tags or [],
                    "status": "PUBLISHED"
                }
            }
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            logger.info(f"Created blog post: {title}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error creating blog post: {str(e)}")
            return None
    
    def get_contact_submissions(self) -> List[Dict[str, Any]]:
        """Get contact form submissions"""
        try:
            url = f"{self.base_url}/v2/contacts"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json().get("contacts", [])
        except requests.RequestException as e:
            logger.error(f"Error getting contacts: {str(e)}")
            return []
    
    def schedule_appointment(self, service_id: str, start_time: str, contact_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Schedule an appointment using Wix Bookings
        
        Args:
            service_id: Service ID
            start_time: Appointment start time
            contact_info: Contact information
            
        Returns:
            Booking data
        """
        try:
            url = f"{self.base_url}/v2/bookings"
            data = {
                "booking": {
                    "serviceId": service_id,
                    "startTime": start_time,
                    "contactDetails": contact_info
                }
            }
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            logger.info("Appointment scheduled successfully")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error scheduling appointment: {str(e)}")
            return None
