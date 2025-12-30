"""
GitHub Integration for Repository Automation
Manages repository operations and automation workflows
"""
import os
from typing import Optional, List, Dict, Any
from github import Github, GithubException
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)


class GithubIntegration:
    """Integration with GitHub for repository management"""
    
    def __init__(self, token: Optional[str] = None):
        """
        Initialize GitHub integration
        
        Args:
            token: GitHub personal access token
        """
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.github = None
        self.repo = None
        
        if self.token:
            self.github = Github(self.token)
            logger.info("GitHub API initialized")
    
    def connect_repository(self, owner: Optional[str] = None, repo_name: Optional[str] = None):
        """
        Connect to a GitHub repository
        
        Args:
            owner: Repository owner
            repo_name: Repository name
        """
        try:
            owner = owner or os.getenv("GITHUB_REPO_OWNER")
            repo_name = repo_name or os.getenv("GITHUB_REPO_NAME")
            
            self.repo = self.github.get_repo(f"{owner}/{repo_name}")
            logger.info(f"Connected to repository: {owner}/{repo_name}")
            return True
        except GithubException as e:
            logger.error(f"Error connecting to repository: {str(e)}")
            return False
    
    def create_issue(self, title: str, body: str, labels: Optional[List[str]] = None) -> Optional[Any]:
        """
        Create a new issue in the repository
        
        Args:
            title: Issue title
            body: Issue description
            labels: List of label names
            
        Returns:
            Created issue object
        """
        try:
            if not self.repo:
                self.connect_repository()
            
            issue = self.repo.create_issue(
                title=title,
                body=body,
                labels=labels or []
            )
            logger.info(f"Created issue: {issue.number}")
            return issue
        except GithubException as e:
            logger.error(f"Error creating issue: {str(e)}")
            return None
    
    def list_issues(self, state: str = "open", labels: Optional[List[str]] = None) -> List[Any]:
        """
        List repository issues
        
        Args:
            state: Issue state (open, closed, all)
            labels: Filter by labels
            
        Returns:
            List of issues
        """
        try:
            if not self.repo:
                self.connect_repository()
            
            issues = self.repo.get_issues(state=state, labels=labels or [])
            return list(issues)
        except GithubException as e:
            logger.error(f"Error listing issues: {str(e)}")
            return []
    
    def create_pull_request(self, title: str, body: str, head: str, base: str = "main") -> Optional[Any]:
        """
        Create a pull request
        
        Args:
            title: PR title
            body: PR description
            head: Head branch
            base: Base branch
            
        Returns:
            Created pull request object
        """
        try:
            if not self.repo:
                self.connect_repository()
            
            pr = self.repo.create_pull(
                title=title,
                body=body,
                head=head,
                base=base
            )
            logger.info(f"Created pull request: {pr.number}")
            return pr
        except GithubException as e:
            logger.error(f"Error creating pull request: {str(e)}")
            return None
    
    def get_repository_stats(self) -> Dict[str, Any]:
        """Get repository statistics"""
        try:
            if not self.repo:
                self.connect_repository()
            
            return {
                "name": self.repo.name,
                "full_name": self.repo.full_name,
                "stars": self.repo.stargazers_count,
                "forks": self.repo.forks_count,
                "open_issues": self.repo.open_issues_count,
                "watchers": self.repo.watchers_count,
                "language": self.repo.language,
                "description": self.repo.description
            }
        except Exception as e:
            logger.error(f"Error getting repository stats: {str(e)}")
            return {"error": str(e)}
