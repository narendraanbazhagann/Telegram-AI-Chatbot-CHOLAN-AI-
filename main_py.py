#!/usr/bin/env python3
"""
Cholan AI - Agricultural Assistant Telegram Bot
Main application entry point
"""

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import Config
from handlers.commands import (
    start_command, help_command, custom_command,
    joke_command, trivia_command, wouldyourather_command
)
from handlers.messages import handle_message, emoji_reaction
from utils.logger import error_handler


def main():
    """Initialize and run the bot"""
    print("Starting Cholan AI bot...")
    
    # Create application
    app = Application.builder().token(Config.TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('joke', joke_command))
    app.add_handler(CommandHandler('trivia', trivia_command))
    app.add_handler(CommandHandler('wouldyourather', wouldyourather_command))

    # Register message handlers
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, emoji_reaction))

    # Register error handler
    app.add_error_handler(error_handler)

    print("Bot initialized successfully. Starting polling...")
    app.run_polling(poll_interval=1)


if __name__ == '__main__':
    main()
