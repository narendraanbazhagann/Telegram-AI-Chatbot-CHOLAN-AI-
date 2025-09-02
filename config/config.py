"""
Configuration settings for Cholan AI Bot
"""

import os
from typing import Final, List, Dict, Any
from pathlib import Path

# ========== PROJECT PATHS ==========
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
STORAGE_DIR = PROJECT_ROOT / "storage"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories if they don't exist
STORAGE_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# ========== BOT CONFIGURATION ==========
TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
BOT_USERNAME: Final = "@cholanai_bot"
CHANNEL_ID: Final = "@cholanaiactivity"

# Validate required environment variables
if TOKEN == "YOUR_BOT_TOKEN_HERE":
    print("⚠️  Warning: Please set TELEGRAM_BOT_TOKEN environment variable")

# ========== AI CONFIGURATION ==========
GEMINI_API_KEY: Final = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
MODEL_NAME: Final = "gemini-1.5-flash"

if GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
    print("⚠️  Warning: Please set GEMINI_API_KEY environment variable")

GENERATION_CONFIG: Dict[str, Any] = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 500
}

# ========== BOT SETTINGS ==========
MAX_WARNINGS: Final = 3
POLL_INTERVAL: Final = 1
MAX_MESSAGE_LENGTH: Final = 4000

# ========== LOGGING CONFIGURATION ==========
LOG_LEVEL: Final = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT: Final = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE: Final = LOGS_DIR / "bot.log"

# ========== STORAGE CONFIGURATION ==========
CONVERSATIONS_FILE: Final = STORAGE_DIR / "conversations.json"
USER_DATA_FILE: Final = STORAGE_DIR / "user_data.json"

# ========== SYSTEM PROMPTS ==========
SYSTEM_PROMPT: Final = """
You are Cholan AI, a friendly and knowledgeable agricultural assistant bot created to help farmers 
and agricultural enthusiasts. You specialize in:

🌱 Crop management and farming techniques
🐛 Pest and disease control
🌰 Soil health and fertilization
🌦️ Weather and seasonal farming advice
♻️ Sustainable farming practices
🤖 Agricultural technology and innovations

Guidelines for responses:
- Keep responses helpful, practical, and concise (under 200 words)
- Use appropriate farming emojis occasionally to keep conversations friendly
- Focus on providing actionable agricultural advice and support
- Be encouraging and supportive to farmers
- If you don't know something specific, admit it and suggest reliable sources
- Always prioritize safety in your recommendations
"""

# ========== ERROR MESSAGES ==========
ERROR_MESSAGES: Dict[str, str] = {
    "ai_error": "🤖 Sorry, I'm having trouble processing that right now. Please try again!",
    "banned_user": "⛔ You are banned from using this bot.",
    "processing": "🤔 Thinking...",
    "warning": "⚠️ Warning {count}/{max}: Please keep our agricultural community friendly and respectful!",
    "banned": "⛔ You have been banned for repeated inappropriate language.",
    "general_error": "❌ Sorry, I encountered an error. Please try again!"
}

# ========== FEATURE FLAGS ==========
FEATURES: Dict[str, bool] = {
    "enable_ai_responses": True,
    "enable_moderation": True,
    "enable_logging_to_channel": True,
    "enable_trivia": True,
    "enable_jokes": True,
    "enable_would_you_rather": True,
    "enable_emoji_reactions": True,
    "save_conversations": True
}
