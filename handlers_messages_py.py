"""
Message handlers for Cholan AI bot
"""

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from utils.ai_handler import get_ai_response
from utils.moderation import check_banned_words, is_user_banned
from utils.logger import send_to_channel, save_chat_log
from data.content import emoji_responses


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Main message handler"""
    user_id = update.message.from_user.id
    username = update.message.from_user.username or "Unknown"
    text: str = update.message.text

    # Send processing indicator
    processing_message = await update.message.reply_text("🗯️")

    # Check if user is banned
    if is_user_banned(user_id):
        await processing_message.edit_text("⛔ You are banned.")
        await send_to_channel(
            context.application, 
            f"❌ Banned user @{username} tried to send: '{text}'"
        )
        return

    # Check for banned words
    warning_response = await check_banned_words(text, user_id, username, context.application)
    if warning_response:
        await processing_message.edit_text(warning_response)
        return

    # Get AI response
    try:
        response = await get_ai_response(text)
        await processing_message.edit_text(response, parse_mode=ParseMode.MARKDOWN)

        # Log activity to channel
        activity_message = f"👤 @{username}\n💬 {text}\n🤖 {response}"
        await send_to_channel(context.application, activity_message)

        # Save to local log
        await save_chat_log(update.message.chat.id, username, text, response)

    except Exception as e:
        error_msg = "Sorry, I'm having trouble processing your message. Please try again!"
        await processing_message.edit_text(error_msg)
        await send_to_channel(context.application, f"⚠️ Error processing message from @{username}: {str(e)}")


async def emoji_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle emoji reactions to keywords"""
    if not update.message or not update.message.text:
        return
        
    message_text = update.message.text.lower()
    
    for keyword, emoji in emoji_responses.items():
        if keyword in message_text:
            await update.message.reply_text(emoji)
            break
