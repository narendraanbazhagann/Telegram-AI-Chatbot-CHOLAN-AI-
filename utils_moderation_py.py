"""
Moderation utilities for user warnings and bans
"""

from typing import Optional
from telegram.ext import Application
from config import Config
from utils.logger import send_to_channel

# In-memory storage for user warnings
user_warnings = {}


def get_user_warnings(user_id: int) -> int:
    """Get warning count for a user"""
    return user_warnings.get(user_id, 0)


def add_user_warning(user_id: int) -> int:
    """Add a warning to a user and return new count"""
    current_warnings = user_warnings.get(user_id, 0)
    user_warnings[user_id] = current_warnings + 1
    return user_warnings[user_id]


def reset_user_warnings(user_id: int):
    """Reset warnings for a user"""
    user_warnings[user_id] = 0


def is_user_banned(user_id: int) -> bool:
    """Check if user is banned (3+ warnings)"""
    return get_user_warnings(user_id) >= Config.MAX_WARNINGS


async def check_banned_words(message: str, user_id: int, username: str, application: Application) -> Optional[str]:
    """
    Check message for banned words and handle warnings
    
    Returns:
        Warning message if banned word found, None otherwise
    """
    message_lower = message.lower()
    
    # Check for banned words
    if any(word in message_lower for word in Config.BANNED_WORDS):
        warnings = add_user_warning(user_id)
        
        if warnings < Config.MAX_WARNINGS:
            # Send warning
            warning_msg = f"⚠️ Warning {warnings}/{Config.MAX_WARNINGS}: Please avoid using inappropriate language."
            await send_to_channel(
                application, 
                f"⚠️ @{username} got warning {warnings}/{Config.MAX_WARNINGS} for: '{message}'"
            )
            return warning_msg
        else:
            # User is now banned
            ban_msg = "⛔ You have been banned for repeated inappropriate language."
            await send_to_channel(
                application, 
                f"🚫 @{username} banned for repeated inappropriate language: '{message}'"
            )
            return ban_msg
    
    return None
