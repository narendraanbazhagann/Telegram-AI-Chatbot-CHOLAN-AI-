"""
Command handlers for Cholan AI bot
"""

import random
from telegram import Update
from telegram.ext import ContextTypes
from utils.logger import send_to_channel
from data.content import jokes, trivia_questions, would_you_rather_questions
from utils.moderation import reset_user_warnings


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text("HELLO! I am Cholan AI, I'm here to help you!")
    await send_to_channel(context.application, "Bot started. /start command received.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = (
        "🌾 I am Cholan AI, your agricultural assistant! 🌾\n\n"
        "Type anything and I'll help you with farming, crops, and agriculture!\n\n"
        "📋 **Available Commands:**\n"
        "• /joke - Get a farming joke\n"
        "• /trivia - Answer agriculture trivia\n"
        "• /wouldyourather - Fun agricultural choices\n"
        "• /custom - Reset your warnings\n"
        "• /help - Show this help message"
    )
    await update.message.reply_text(help_text)
    await send_to_channel(context.application, "Help command received.")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /custom command - Reset user warnings"""
    user_id = update.message.from_user.id
    reset_user_warnings(user_id)
    await update.message.reply_text("✅ Your warnings have been reset.")
    await send_to_channel(
        context.application, 
        f"Warnings reset for user: @{update.message.from_user.username}"
    )


async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /joke command"""
    joke = random.choice(jokes)
    await update.message.reply_text(joke)
    await send_to_channel(context.application, f"Joke sent to @{update.message.from_user.username}")


async def trivia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /trivia command"""
    question = random.choice(trivia_questions)
    await update.message.reply_poll(
        question=question["question"],
        options=question["options"],
        is_anonymous=False,
        allows_multiple_answers=False
    )
    await send_to_channel(
        context.application, 
        f"Trivia question sent to @{update.message.from_user.username}"
    )


async def wouldyourather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /wouldyourather command"""
    question = random.choice(would_you_rather_questions)
    await update.message.reply_text(f"🤔 {question}")
    await send_to_channel(
        context.application, 
        f"Would you rather question sent to @{update.message.from_user.username}"
    )
