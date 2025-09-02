"""
Logging utilities for Cholan AI Bot
"""

import logging
import sys
from pathlib import Path
from typing import Optional
from telegram.ext import Application

from config.config import LOG_LEVEL, LOG_FORMAT, LOG_FILE, CHANNEL_ID, FEATURES

# Global logger dictionary to avoid duplicate loggers
_loggers = {}

def setup_logger():
    """Setup logging configuration for the entire application"""
    
    # Create logs directory if it doesn't exist
    LOG_FILE.parent.mkdir(exist_ok=True)
    
    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper()),
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Set specific logger levels
    logging.getLogger("telegram").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    
    root_logger = logging.getLogger("cholan_ai")
    root_logger.info("📝 Logging system initialized")
    root_logger.info(f"📁 Log file: {LOG_FILE}")

def get_logger(name: str) -> logging.Logger:
    """Get or create a logger with the specified name"""
    
    if name not in _loggers:
        logger = logging.getLogger(f"cholan_ai.{name}")
        _loggers[name] = logger
    
    return _loggers[name]

async def log_to_channel(application: Application, message: str):
    """Send log message to the configured Telegram channel"""
    
    if not FEATURES["enable_logging_to_channel"]:
        return
    
    try:
        await application.bot.send_message(
            chat_id=CHANNEL_ID, 
            text=f"🤖 **Cholan AI Log**\n{message}",
            parse_mode="Markdown"
        )
    except Exception as e:
        logger = get_logger(__name__)
        logger.error(f"Failed to send log to channel: {e}")

class BotLogger:
    """Context manager for bot operation logging"""
    
    def __init__(self, logger: logging.Logger, operation: str):
        self.logger = logger
        self.operation = operation
    
    def __enter__(self):
        self.logger.info(f"🔄 Starting: {self.operation}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.logger.info(f"✅ Completed: {self.operation}")
        else:
            self.logger.error(f"❌ Failed: {self.operation} - {exc_val}")

# Convenience function for structured logging
def log_user_action(logger: logging.Logger, username: str, action: str, details: str = ""):
    """Log user actions in a structured format"""
    log_message = f"👤 User @{username} - {action}"
    if details:
        log_message += f" | {details}"
    logger.info(log_message)

def log_ai_interaction(logger: logging.Logger, username: str, query: str, response_length: int):
    """Log AI interactions"""
    logger.info(f"🤖 AI Response for @{username} - Query: {query[:50]}... Response: {response_length} chars")

def log_moderation_action(logger: logging.Logger, username: str, action: str, reason: str):
    """Log moderation actions"""
    logger.warning(f"⚠️ Moderation - @{username} - {action} - Reason: {reason}")

# Export commonly used logger instances
main_logger = get_logger("main")
bot_logger = get_logger("bot")
ai_logger = get_logger("ai")
moderation_logger = get_logger("moderation")
