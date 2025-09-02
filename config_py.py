"""
Configuration settings for Cholan AI bot
"""

import os
from typing import Final, List


class Config:
    """Bot configuration settings"""
    
    # Bot credentials - Use environment variables in production
    TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")
    BOT_USERNAME: Final = "@cholanai_bot"
    CHANNEL_ID: Final = "@cholanaiactivity"
    GEMINI_API_KEY: Final = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
    
    # Moderation settings
    MAX_WARNINGS: Final = 3
    BANNED_WORDS: Final[List[str]] = ['fuck', 'shit', 'bitch']
    
    # AI settings
    GEMINI_MODEL: Final = "gemini-1.5-flash"
    GENERATION_CONFIG: Final = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192
    }
    
    # File settings
    CHAT_LOG_FILE: Final = "chat_logs.json"
    
    # Bot personality
    BOT_DESCRIPTION: Final = "You are Cholan AI, a friendly agriculture bot. Keep responses short and fun."
