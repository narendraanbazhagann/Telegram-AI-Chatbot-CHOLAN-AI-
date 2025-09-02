"""
Logging utilities for Cholan AI bot
"""

import json
import os
from datetime import datetime
from typing import Dict, Any
from telegram import Update
from telegram.ext import Application, ContextTypes
from config import Config


async def send_to_channel(application: Application, message: str):
    """Send a message to the activity channel"""
    try:
        await application.bot.send_message(chat_id=Config.CHANNEL_ID, text=message)
    except Exception as e:
        print(f"Error sending to channel: {e}")


async def save_chat_log(chat_id: int, username: str, message: str, bot_reply: str):
    """Save chat interaction to JSON file"""
    log_entry = {
        "timestamp": str(datetime.now()),
        "chat_id": chat_id,
        "username": username,
        "message": message,
        "bot_reply": bot_reply
    }
    
    try:
        # Load existing logs
        if os.path.exists(Config.CHAT_LOG_FILE):
            with open(Config.CHAT_LOG_FILE, "r", encoding="utf-8") as file:
                logs = json.load(file)
                if not isinstance(logs, list):
                    logs = [logs]
        else:
            logs = []
        
        # Add new log entry
        logs.append(log_entry)
        
        # Save back to file
        with open(Config.CHAT_LOG_FILE, "w", encoding="utf-8") as file:
            json.dump(logs, file, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error saving chat log: {e}")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle bot errors"""
    error_message = f"Update {update} caused error {context.error}"
    await send_to_channel(context.application, f"⚠️ Error: {error_message}")
    print(f"Bot error: {error_message}")
