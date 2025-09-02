"""
AI response handler using Google Gemini
"""

import google.generativeai as genai
from datetime import datetime
from config import Config


def get_greeting():
    """Get time-appropriate greeting"""
    current_hour = datetime.now().hour
    if 0 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


async def get_ai_response(user_message: str) -> str:
    """
    Generate AI response using Gemini
    
    Args:
        user_message: User's input message
        
    Returns:
        AI generated response
    """
    processed_message = user_message.lower()
    greeting = get_greeting()

    # Handle simple greetings locally
    if 'hello' in processed_message:
        return f"{greeting}! Hey there! 🌾"
    if 'hlo' in processed_message:
        return f"{greeting}! Hey there! 😊"

    # Use Gemini for complex responses
    try:
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        model = genai.GenerativeModel(
            model_name=Config.GEMINI_MODEL,
            generation_config=Config.GENERATION_CONFIG
        )
        
        chat_session = model.start_chat(history=[])
        
        # Set bot personality
        chat_session.send_message(Config.BOT_DESCRIPTION)
        
        # Get response
        response = chat_session.send_message(user_message)
        return response.text
        
    except Exception as e:
        print(f"Error getting AI response: {e}")
        return f"{greeting}! I'm having trouble thinking right now, but I'm here to help with your agricultural questions! 🌱"
