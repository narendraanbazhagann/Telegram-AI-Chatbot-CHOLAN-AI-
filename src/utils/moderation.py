"""
Content moderation and user management utilities
"""

import json
from typing import Dict, Optional, Any
from datetime import datetime, timedelta

from config.config import MAX_WARNINGS, USER_DATA_FILE, ERROR_MESSAGES
from utils.logger import get_logger, log_moderation_action

logger = get_logger(__name__)

# In-memory storage for warnings (will be persisted to file)
user_warnings: Dict[int, int] = {}
banned_users: Dict[int, datetime] = {}

# Banned words list
BANNED_WORDS = [
    'fuck', 'shit', 'bitch', 'damn', 'hell',
    'stupid', 'idiot', 'moron', 'dumb', 'retard',
    'asshole', 'bastard', 'crap', 'piss'
]

# Severity levels for different types of violations
VIOLATION_SEVERITY = {
    'mild': 1,      # Common swear words
    'moderate': 2,  # Offensive terms
    'severe': 3     # Hate speech, extreme language
}

def load_user_data():
    """Load user data from persistent storage"""
    global user_warnings, banned_users
    
    try:
        if USER_DATA_FILE.exists():
            with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                user_warnings = {int(k): v for k, v in data.get('warnings', {}).items()}
                
                # Convert banned users timestamps back to datetime
                banned_data = data.get('banned', {})
                banned_users = {}
                for user_id, timestamp in banned_data.items():
                    banned_users[int(user_id)] = datetime.fromisoformat(timestamp)
                
                logger.info(f"📚 Loaded user data: {len(user_warnings)} warnings, {len(banned_users)} banned users")
        else:
            logger.info("📚 No existing user data file found, starting fresh")
            
    except Exception as e:
        logger.error(f"❌ Failed to load user data: {e}")

def save_user_data():
    """Save user data to persistent storage"""
    try:
        # Convert banned users timestamps to strings for JSON serialization
        banned_data = {str(k): v.isoformat() for k, v in banned_users.items()}
        
        data = {
            'warnings': {str(k): v for k, v in user_warnings.items()},
            'banned': banned_data,
            'last_updated': datetime.now().isoformat()
        }
        
        USER_DATA_FILE.parent.mkdir(exist_ok=True)
        with open(USER_DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            
        logger.debug("💾 User data saved successfully")
        
    except Exception as e:
        logger.error(f"❌ Failed to save user data: {e}")

def check_banned_user(user_id: int) -> bool:
    """Check if user is currently banned"""
    if user_id in banned_users:
        ban_time = banned_users[user_id]
        # Check if ban has expired (optional: implement temporary bans)
        # For now, bans are permanent until manually removed
        return True
    return False

def check_banned_words(user_id: int, text: str) -> Optional[Dict[str, Any]]:
    """
    Check message for banned words and handle warnings
    
    Returns:
        Dict with message and log_message if violation found, None otherwise
    """
    
    text_lower = text.lower()
    username = f"user_{user_id}"  # Fallback if username not available
    
    # Check for banned words
    violations = []
    for word in BANNED_WORDS:
        if word in text_lower:
            violations.append(word)
    
    if not violations:
        return None
    
    # Determine violation severity
    severity = _determine_violation_severity(violations)
    warning_increment = VIOLATION_SEVERITY.get(severity, 1)
    
    # Update warnings
    current_warnings = user_warnings.get(user_id, 0)
    new_warnings = current_warnings + warning_increment
    user_warnings[user_id] = new_warnings
    
    # Save data
    save_user_data()
    
    # Log the violation
    violation_text = ', '.join(violations)
    log_moderation_action(
        logger, 
        username, 
        f"Warning {new_warnings}/{MAX_WARNINGS}", 
        f"Banned words: {violation_text}"
    )
    
    # Check if user should be banned
    if new_warnings >= MAX_WARNINGS:
        banned_users[user_id] = datetime.now()
        save_user_data()
        
        log_moderation_action(
            logger, 
            username, 
            "BANNED", 
            f"Exceeded maximum warnings ({MAX_WARNINGS})"
        )
        
        return {
            'message': ERROR_MESSAGES["banned"],
            'log_message': f"🚫 User {username} (ID: {user_id}) banned for repeated violations: '{violation_text}'"
        }
    else:
        warning_msg = ERROR_MESSAGES["warning"].format(count=new_warnings, max=MAX_WARNINGS)
        return {
            'message': warning_msg,
            'log_message': f"⚠️ User {username} (ID: {user_id}) warning {new_warnings}/{MAX_WARNINGS} for: '{violation_text}'"
        }

def _determine_violation_severity(violations: list) -> str:
    """Determine the severity level of violations"""
    
    severe_words = ['retard', 'bastard']  # More serious violations
    moderate_words = ['stupid', 'idiot', 'moron', 'dumb', 'asshole']
    
    if any(word in severe_words for word in violations):
        return 'severe'
    elif any(word in moderate_words for word in violations):
        return 'moderate'
    else:
        return 'mild'

def reset_user_warnings(user_id: int):
    """Reset warnings for a specific user"""
    user_warnings[user_id] = 0
    save_user_data()
    
    log_moderation_action(
        logger, 
        f"user_{user_id}", 
        "WARNING_RESET", 
        "Manual reset requested"
    )

def unban_user(user_id: int) -> bool:
    """Unban a user (admin function)"""
    if user_id in banned_users:
        del banned_users[user_id]
        save_user_data()
        
        log_moderation_action(
            logger, 
            f"user_{user_id}", 
            "UNBANNED", 
            "Manual unban"
        )
        return True
    return False

def get_user_warnings(user_id: int) -> int:
    """Get current warning count for user"""
    return user_warnings.get(user_id, 0)

def get_moderation_stats() -> Dict[str, Any]:
    """Get moderation statistics"""
    return {
        'total_users_with_warnings': len([w for w in user_warnings.values() if w > 0]),
        'total_banned_users': len(banned_users),
        'average_warnings': sum(user_warnings.values()) / len(user_warnings) if user_warnings else 0,
        'users_near_ban': len([w for w in user_warnings.values() if w >= MAX_WARNINGS - 1])
    }

def add_banned_word(word: str):
    """Add a word to the banned words list"""
    if word.lower() not in BANNED_WORDS:
        BANNED_WORDS.append(word.lower())
        logger.info(f"🚫 Added banned word: {word}")

def remove_banned_word(word: str) -> bool:
    """Remove a word from the banned words list"""
    if word.lower() in BANNED_WORDS:
        BANNED_WORDS.remove(word.lower())
        logger.info(f"✅ Removed banned word: {word}")
        return True
    return False

# Initialize user data on module import
load_user_data()
