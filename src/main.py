#!/usr/bin/env python3
"""
Cholan AI - Agricultural Assistant Bot
Main application entry point

Author: Your Name
Version: 1.0.0
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from telegram.ext import Application
from config.config import TOKEN, POLL_INTERVAL
from bot.handlers import setup_handlers
from utils.logger import setup_logger, get_logger

def main():
    """Main function to initialize and run the bot"""
    
    # Setup logging
    setup_logger()
    logger = get_logger(__name__)
    
    logger.info("🌾 Starting Cholan AI Agricultural Bot...")
    
    try:
        # Create bot application
        application = Application.builder().token(TOKEN).build()
        
        # Setup all handlers
        setup_handlers(application)
        
        logger.info("🚜 Bot initialized successfully")
        logger.info("🚜 Bot is running... Press Ctrl+C to stop")
        
        # Start polling
        application.run_polling(poll_interval=POLL_INTERVAL)
        
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Critical error: {e}")
        raise
    finally:
        logger.info("🌾 Cholan AI Bot shutdown complete")

if __name__ == '__main__':
    main()
