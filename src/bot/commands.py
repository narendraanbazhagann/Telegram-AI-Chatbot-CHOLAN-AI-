"""
Bot command implementations for Cholan AI
"""

import random
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from data.jokes import get_random_joke
from data.trivia import get_random_trivia
from data.responses import get_random_would_you_rather
from utils.moderation import reset_user_warnings
from utils.logger import get_logger, log_to_channel

logger = get_logger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    welcome_message = (
        "🌾 **Welcome to Cholan AI!** 🌾\n\n"
        "I'm your friendly agricultural assistant bot, here to help with:\n"
        "• 🌱 Farming questions and crop advice\n"
        "• 🌦️ Weather and seasonal guidance\n"
        "• 🐛 Pest and disease management\n"
        "• 🌰 Soil health and fertilization tips\n"
        "• 🤖 Agricultural technology insights\n"
        "• 🎯 Fun farming trivia and jokes\n\n"
        "Type /help to see all available commands, or just ask me anything about agriculture!\n\n"
        "Happy farming! 🚜✨"
    )
    
    await update.message.reply_text(welcome_message, parse_mode=ParseMode.MARKDOWN)
    await log_to_channel(context.application, "🚀 New user started the bot with /start command")
    logger.info(f"Start command from @{update.message.from_user.username}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = (
        "🌱 **Cholan AI - Your Agricultural Assistant** 🌱\n\n"
        "**🤖 Main Features:**\n"
        "• Ask me anything about farming, crops, or agriculture\n"
        "• Get personalized advice for your farming needs\n"
        "• Learn about sustainable farming practices\n\n"
        "**📋 Available Commands:**\n"
        "• `/start` - Welcome message and introduction\n"
        "• `/help` - Show this help message\n"
        "• `/joke` - Get a random farming joke 😂\n"
        "• `/trivia` - Agricultural knowledge quiz 🧠\n"
        "• `/wouldyourather` - Fun farming scenarios 🤔\n"
        "• `/reset` - Reset your warning count ✅\n\n"
        "**💬 How to Use:**\n"
        "Just type your farming question naturally! Examples:\n"
        "• \"How do I improve my soil quality?\"\n"
        "• \"When should I plant tomatoes?\"\n"
        "• \"What's the best way to control pests?\"\n"
        "• \"Tell me about crop rotation\"\n\n"
        "**🌾 Topics I Can Help With:**\n"
        "• Crop management and planting schedules\n"
        "• Soil health and fertilization\n"
        "• Pest and disease control\n"
        "• Weather and seasonal farming\n"
        "• Organic and sustainable practices\n"
        "• Agricultural technology and tools\n"
        "• Livestock and animal husbandry basics\n\n"
        "Ready to grow your agricultural knowledge? 🚜💚"
    )
    
    await update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)
    await log_to_channel(context.application, f"ℹ️ Help command requested by @{update.message.from_user.username}")
    logger.info(f"Help command from @{update.message.from_user.username}")

async def reset_warnings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /reset command to reset user warnings"""
    user_id = update.message.from_user.id
    username = update.message.from_user.username or "Unknown"
    
    reset_user_warnings(user_id)
    
    await update.message.reply_text(
        "✅ **Warnings Reset Successfully!**\n\n"
        "Your warning count has been reset to 0. "
        "Please continue to keep our agricultural community friendly and respectful! 🌾"
    )
    
    await log_to_channel(
        context.application, 
        f"🔄 Warnings reset for user: @{username} (ID: {user_id})"
    )
    logger.info(f"Warnings reset for @{username}")

async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random agricultural joke"""
    joke = get_random_joke()
    
    joke_message = (
        f"😂 **Agricultural Joke Time!** 😂\n\n"
        f"{joke}\n\n"
        f"Hope that brought a smile to your day! 🌾\n"
        f"Type /joke again for another one!"
    )
    
    await update.message.reply_text(joke_message, parse_mode=ParseMode.MARKDOWN)
    await log_to_channel(
        context.application, 
        f"😂 Joke sent to @{update.message.from_user.username}"
    )
    logger.info(f"Joke sent to @{update.message.from_user.username}")

async def trivia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random agricultural trivia question"""
    trivia = get_random_trivia()
    
    # Send poll with trivia question
    await update.message.reply_poll(
        question=f"🧠 Agricultural Trivia: {trivia['question']}",
        options=trivia['options'],
        is_anonymous=False,
        allows_multiple_answers=False,
        correct_option_id=trivia['options'].index(trivia['answer']),
        explanation=f"The correct answer is: {trivia['answer']}! 🌾"
    )
    
    await log_to_channel(
        context.application, 
        f"🧠 Trivia question sent to @{update.message.from_user.username}: {trivia['question'][:50]}..."
    )
    logger.info(f"Trivia sent to @{update.message.from_user.username}")

async def wouldyourather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a 'Would You Rather' agricultural question"""
    question = get_random_would_you_rather()
    
    wyr_message = (
        f"🤔 **Would You Rather - Farming Edition** 🤔\n\n"
        f"{question}\n\n"
        f"Think about it and let me know your choice! "
        f"There's no wrong answer - it's all about your farming style! 🚜\n\n"
        f"Type /wouldyourather for another scenario!"
    )
    
    await update.message.reply_text(wyr_message, parse_mode=ParseMode.MARKDOWN)
    await log_to_channel(
        context.application, 
        f"🤷‍♂️ Would You Rather sent to @{update.message.from_user.username}"
    )
    logger.info(f"Would You Rather sent to @{update.message.from_user.username}")
