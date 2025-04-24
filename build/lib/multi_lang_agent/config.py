"""
Configuration module for the multi-language agent.

This module loads environment variables from .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google API credentials
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Constants for the application
DEFAULT_MODEL_ID = "gemini-2.0-flash"
SUPPORTED_LANGUAGES = ["English", "Japanese", "Chinese", "German"]

def get_api_key():
    """Get the Google API key from environment variables."""
    if not GOOGLE_API_KEY:
        raise ValueError(
            "Google API key not found. Please set GOOGLE_API_KEY environment variable."
        )
    return GOOGLE_API_KEY 