"""
Message and command handlers for Cholan AI Bot
"""

from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, 
    filters, ContextTypes
)
from telegram.constants import ParseMode

from bot.commands import (
    start_command, help_command, reset_warnings_command,
    joke_command, trivia_command, wouldyourather_command
)
from utils.ai_handler import handle_ai_response
from utils.moderation import check_banned_user, check_banned_words
from utils.logger import get_logger, log_to_channel
from config.config import ERROR_MESSAGES, FEATURES
from data.responses import get_emoji_reaction

logger = get_logger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Main message handler for user messages"""
    
    try:
        user_id = update.message.from_user.id
        username = update.message.from_user.username or "Unknown"
        text = update.message.text
        
        logger.info(f"Message from @{username}: {text[:50]}...")
        
        # Send processing indicator
        processing_message = await update.message.reply_text(ERROR_MESSAGES["processing"])
        
        # Check if user is banned
        if FEATURES["enable_moderation"] and check_banned_user(user_id):
            await processing_message.edit_text(ERROR_MESSAGES["banned_user"])
            await log_to_channel(
                context.application, 
                f"❌ Banned user @{username} tried to send: '{text[:100]}'"
            )
            return
        
        # Check for banned words
        if FEATURES["enable_moderation"]:
            warning_result = check_banned_words(user_id, text)
            if warning_result:
                await processing_message.edit_text(warning_result["message"])
                await log_to_channel(context.application, warning_result["log_message"])
                return
        
        # Generate AI response
        if FEATURES["enable_ai_responses"]:
            response = await handle_ai_response(text)
            await processing_message.edit_text(response, parse_mode=ParseMode.MARKDOWN)
            
            # Log activity to channel
            if FEATURES["enable_logging_to_channel"]:
                activity_message = (
                    f"👤 User: @{username}\n"
                    f"💬 Message: {text[:100]}{'...' if len(text) > 100 else ''}\n"
                    f"🤖 Response: {response[:100]}{'...' if len(response) > 100 else ''}"
                )
                await log_to_channel(context.application, activity_message)
        
        # Handle emoji reactions
        if FEATURES["enable_emoji_reactions"]:
            emoji = get_emoji_reaction(text)
            if emoji:
                await update.message.reply_text(emoji)
                
    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await processing_message.edit_text(ERROR_MESSAGES["general_error"])
        await log_to_channel(
            context.application, 
            f"⚠️ Error handling message from @{username}: {str(e)}"
        )

async def handle_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Global error handler"""
    error_message = f"❌ Error occurred: {context.error}"
    logger.error(error_message)
    
    if FEATURES["enable_logging_to_channel"]:
        await log_to_channel(context.application, error_message)

def setup_handlers(application: Application):
    """Setup all bot handlers"""
    logger.info("Setting up bot handlers...")
    
    # Command handlers
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('reset', reset_warnings_command))
    
    if FEATURES["enable_jokes"]:
        application.add_handler(CommandHandler('joke', joke_command))
    
    if FEATURES["enable_trivia"]:
        application.add_handler(CommandHandler('trivia', trivia_command))
    
    if FEATURES["enable_would_you_rather"]:
        application.add_handler(CommandHandler('wouldyourather', wouldyourather_command))
    
    # Message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Error handler
    application.add_error_handler(handle_error)
    
    logger.info("✅ All handlers setup complete")
