"""
AI response handler using Google Gemini
"""

import google.generativeai as genai
from datetime import datetime
from typing import Optional

from config.config import GEMINI_API_KEY, MODEL_NAME, GENERATION_CONFIG, SYSTEM_PROMPT, ERROR_MESSAGES
from utils.logger import get_logger, log_ai_interaction
from data.responses import get_time_based_greeting

logger = get_logger(__name__)

# Initialize Gemini AI
try:
    genai.configure(api_key=GEMINI_API_KEY)
    logger.info("🤖 Gemini AI initialized successfully")
except Exception as e:
    logger.error(f"❌ Failed to initialize Gemini AI: {e}")

class AIResponseHandler:
    """Handles AI response generation with context management"""
    
    def __init__(self):
        self.model = None
        self.chat_sessions = {}  # Store chat sessions per user
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the Gemini model"""
        try:
            self.model = genai.GenerativeModel(
                model_name=MODEL_NAME,
                generation_config=GENERATION_CONFIG
            )
            logger.info(f"✅ Model {MODEL_NAME} initialized")
        except Exception as e:
            logger.error(f"❌ Model initialization failed: {e}")
            self.model = None
    
    def get_chat_session(self, user_id: int):
        """Get or create chat session for user"""
        if user_id not in self.chat_sessions:
            if self.model:
                self.chat_sessions[user_id] = self.model.start_chat(history=[])
                # Send system prompt to establish context
                try:
                    self.chat_sessions[user_id].send_message(SYSTEM_PROMPT)
                    logger.debug(f"Chat session created for user {user_id}")
                except Exception as e:
                    logger.error(f"Failed to initialize chat session: {e}")
            else:
                return None
        return self.chat_sessions[user_id]
    
    def clear_chat_session(self, user_id: int):
        """Clear chat session for user (useful for context reset)"""
        if user_id in self.chat_sessions:
            del self.chat_sessions[user_id]
            logger.debug(f"Chat session cleared for user {user_id}")

# Global AI handler instance
ai_handler = AIResponseHandler()

async def handle_ai_response(text: str, user_id: Optional[int] = None, username: str = "Unknown") -> str:
    """
    Generate AI response for user input
    
    Args:
        text: User's message text
        user_id: Telegram user ID (for session management)
        username: Username for logging
    
    Returns:
        AI-generated response string
    """
    
    processed_text = text.lower().strip()
    
    # Handle simple greetings first
    greeting_response = _handle_simple_greetings(processed_text)
    if greeting_response:
        log_ai_interaction(logger, username, text, len(greeting_response))
        return greeting_response
    
    # Generate AI response
    try:
        if not ai_handler.model:
            logger.error("AI model not available")
            return ERROR_MESSAGES["ai_error"]
        
        # Get user's chat session if user_id provided
        if user_id:
            chat_session = ai_handler.get_chat_session(user_id)
        else:
            # Create temporary session
            chat_session = ai_handler.model.start_chat(history=[])
            chat_session.send_message(SYSTEM_PROMPT)
        
        if not chat_session:
            return ERROR_MESSAGES["ai_error"]
        
        # Generate response
        response = chat_session.send_message(text)
        ai_response = response.text.strip()
        
        # Post-process response
        ai_response = _post_process_response(ai_response)
        
        # Log the interaction
        log_ai_interaction(logger, username, text, len(ai_response))
        
        return ai_response
        
    except Exception as e:
        logger.error(f"AI response generation failed: {e}")
        return ERROR_MESSAGES["ai_error"]

def _handle_simple_greetings(text: str) -> Optional[str]:
    """Handle simple greetings without AI"""
    
    greeting_keywords = ['hello', 'hi', 'hey', 'hlo', 'greetings', 'good morning', 'good afternoon', 'good evening']
    
    if any(keyword in text for keyword in greeting_keywords):
        greeting = get_time_based_greeting()
        return f"{greeting}! 🌾 Welcome to Cholan AI! How can I help you with your agricultural needs today?"
    
    return None

def _post_process_response(response: str) -> str:
    """Post-process AI response for better formatting"""
    
    # Remove excessive newlines
    response = '\n'.join(line.strip() for line in response.split('\n') if line.strip())
    
    # Ensure response isn't too long
    max_length = 1000  # Telegram message limit consideration
    if len(response) > max_length:
        response = response[:max_length-3] + "..."
        logger.warning("Response truncated due to length")
    
    # Add agricultural context if response seems too generic
    if len(response) < 50 and "agricultural" not in response.lower() and "farm" not in response.lower():
        response += " 🌱"
    
    return response

def reset_user_context(user_id: int):
    """Reset user's chat context (useful for fresh start)"""
    ai_handler.clear_chat_session(user_id)
    logger.info(f"AI context reset for user {user_id}")

# Health check function
def check_ai_health() -> bool:
    """Check if AI service is healthy"""
    try:
        if ai_handler.model:
            # Try a simple test
            test_chat = ai_handler.model.start_chat(history=[])
            test_response = test_chat.send_message("Test")
            return bool(test_response.text)
        return False
    except Exception as e:
        logger.error(f"AI health check failed: {e}")
        return False
