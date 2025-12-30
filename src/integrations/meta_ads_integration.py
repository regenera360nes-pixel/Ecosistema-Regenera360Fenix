"""
Meta Ads Integration for Marketing Automation
Manages Facebook/Instagram advertising campaigns
"""
import os
from typing import Optional, Dict, Any, List
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)


class MetaAdsIntegration:
    """Integration with Meta/Facebook Ads for marketing automation"""
    
    def __init__(self, access_token: Optional[str] = None, app_id: Optional[str] = None, 
                 app_secret: Optional[str] = None, ad_account_id: Optional[str] = None):
        """
        Initialize Meta Ads integration
        
        Args:
            access_token: Meta access token
            app_id: App ID
            app_secret: App secret
            ad_account_id: Ad account ID
        """
        self.access_token = access_token or os.getenv("META_ACCESS_TOKEN")
        self.app_id = app_id or os.getenv("META_APP_ID")
        self.app_secret = app_secret or os.getenv("META_APP_SECRET")
        self.ad_account_id = ad_account_id or os.getenv("META_AD_ACCOUNT_ID")
        
        if self.access_token and self.app_id and self.app_secret:
            FacebookAdsApi.init(self.app_id, self.app_secret, self.access_token)
            self.account = AdAccount(f'act_{self.ad_account_id}')
            logger.info("Meta Ads API initialized")
    
    def create_campaign(self, name: str, objective: str, status: str = "PAUSED") -> Optional[Campaign]:
        """
        Create a new ad campaign
        
        Args:
            name: Campaign name
            objective: Campaign objective (e.g., 'OUTCOME_ENGAGEMENT', 'OUTCOME_LEADS')
            status: Campaign status
            
        Returns:
            Created campaign object
        """
        try:
            params = {
                'name': name,
                'objective': objective,
                'status': status,
                'special_ad_categories': []
            }
            campaign = self.account.create_campaign(params=params)
            logger.info(f"Created campaign: {name}")
            return campaign
        except Exception as e:
            logger.error(f"Error creating campaign: {str(e)}")
            return None
    
    def get_campaigns(self, status: Optional[str] = None) -> List[Campaign]:
        """
        Get all campaigns
        
        Args:
            status: Filter by status
            
        Returns:
            List of campaigns
        """
        try:
            fields = [
                'name',
                'objective',
                'status',
                'daily_budget',
                'lifetime_budget'
            ]
            params = {}
            if status:
                params['effective_status'] = [status]
            
            campaigns = self.account.get_campaigns(fields=fields, params=params)
            return list(campaigns)
        except Exception as e:
            logger.error(f"Error getting campaigns: {str(e)}")
            return []
    
    def get_campaign_insights(self, campaign_id: str) -> Dict[str, Any]:
        """
        Get campaign performance insights
        
        Args:
            campaign_id: Campaign ID
            
        Returns:
            Campaign insights
        """
        try:
            campaign = Campaign(campaign_id)
            insights = campaign.get_insights(fields=[
                'impressions',
                'clicks',
                'spend',
                'reach',
                'frequency',
                'cpc',
                'cpm',
                'ctr'
            ])
            return insights[0] if insights else {}
        except Exception as e:
            logger.error(f"Error getting insights: {str(e)}")
            return {}
    
    def pause_campaign(self, campaign_id: str) -> bool:
        """
        Pause a campaign
        
        Args:
            campaign_id: Campaign ID
            
        Returns:
            Success status
        """
        try:
            campaign = Campaign(campaign_id)
            campaign.api_update(params={'status': Campaign.Status.paused})
            logger.info(f"Paused campaign: {campaign_id}")
            return True
        except Exception as e:
            logger.error(f"Error pausing campaign: {str(e)}")
            return False
    
    def get_account_insights(self) -> Dict[str, Any]:
        """Get ad account insights"""
        try:
            insights = self.account.get_insights(fields=[
                'impressions',
                'clicks',
                'spend',
                'reach',
                'account_name'
            ])
            return insights[0] if insights else {}
        except Exception as e:
            logger.error(f"Error getting account insights: {str(e)}")
            return {}
