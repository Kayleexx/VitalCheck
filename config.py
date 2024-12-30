from dotenv import load_dotenv
import os
import logging
from typing import Dict

def load_config() -> Dict[str, str]:
    """Load configuration from environment"""
    logger = logging.getLogger(__name__)
    
    try:
        # Check if .env file exists
        if not os.path.exists('.env'):
            raise ValueError("'.env' file not found. Please create a .env file in the project root.")
        
        load_dotenv()
        api_key = os.getenv("API_KEY")
        
        if not api_key:
            raise ValueError("""API Key not found! Please set SCRAPYBARA_API_KEY in .env file.
            
Example .env file content:
SCRAPYBARA_API_KEY=your_api_key_here""")
        
        return {
            "api_key": api_key
        }
    except Exception as e:
        logger.error(f"Error loading configuration: {str(e)}")
        raise

