# 🌾 Cholan AI - Agricultural Assistant Bot

Cholan AI is a friendly Telegram bot designed to assist farmers and agricultural enthusiasts with farming questions, tips, and interactive features. Built with Python and powered by Google's Gemini AI, this bot provides intelligent agricultural advice and engaging interactions.

## ✨ Features

### 🤖 AI-Powered Responses
- Intelligent agricultural assistance using Google Gemini AI
- Contextual farming advice and crop management tips
- Friendly, conversational interface

### 📚 Educational Content
- Agricultural trivia questions with interactive polls
- Farming jokes and entertainment
- "Would You Rather" scenarios related to agriculture
- Daily agricultural tips and insights

### 🛡️ Moderation System
- Automated content filtering
- Warning system for inappropriate language
- User ban functionality for repeated violations
- Activity logging to designated channel

### 🎯 Interactive Commands
- `/start` - Welcome message and bot introduction
- `/help` - Comprehensive help and feature list
- `/joke` - Random agricultural jokes
- `/trivia` - Educational quiz questions
- `/wouldyourather` - Fun farming scenarios
- `/reset` - Reset user warnings

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Google Gemini API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cholan-ai-bot.git
   cd cholan-ai-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Configure the bot**
   Edit `config.py` to update:
   - Bot username
   - Channel ID for logging
   - Other settings as needed

5. **Run the bot**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
cholan-ai-bot/
├── 📁 src/                          # Source code
│   ├── 📄 main.py                   # Application entry point
│   ├── 📁 bot/                      # Bot modules
│   │   ├── 📄 handlers.py           # Message handling
│   │   └── 📄 commands.py           # Command implementations
│   ├── 📁 utils/                    # Utilities
│   │   ├── 📄 ai_handler.py         # AI integration
│   │   ├── 📄 logger.py             # Logging system
│   │   └── 📄 moderation.py         # Content moderation
│   └── 📁 data/                     # Static data
│       ├── 📄 jokes.py              # 80+ farming jokes
│       ├── 📄 trivia.py             # 20+ trivia questions
│       └── 📄 responses.py          # Response templates
├── 📁 config/                       # Configuration
│   └── 📄 config.py                 # Settings & API keys
├── 📄 requirements.txt              # Dependencies
├── 📄 requirements-dev.txt          # Dev dependencies
├── 📄 .env.example                  # Environment template
├── 📄 .gitignore                    # Git ignore rules
├── 📄 README.md                     # Documentation
├── 📄 Dockerfile                    # Docker setup
├── 📄 docker-compose.yml            # Container orchestration
└── 📄 setup.py                      # Package setup
```

## ⚙️ Configuration

### Environment Variables
- `TELEGRAM_BOT_TOKEN` - Your Telegram bot token from BotFather
- `GEMINI_API_KEY` - Your Google Gemini API key

### Bot Settings (config.py)
- `BOT_USERNAME` - Your bot's username
- `CHANNEL_ID` - Channel for activity logging
- `MAX_WARNINGS` - Maximum warnings before ban (default: 3)
- `GENERATION_CONFIG` - AI model parameters

## 🔧 Customization

### Adding New Jokes
Edit the `jokes` list in `data.py`:
```python
jokes = [
    "Your new farming joke here! 🌾",
    # ... existing jokes
]
```

### Adding New Trivia Questions
Add questions to `trivia_questions` in `data.py`:
```python
{
    "question": "Your question here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Correct Option"
}
```

### Modifying AI Behavior
Update the `SYSTEM_PROMPT` in `config.py` to change how the AI responds.

## 🛡️ Safety Features

- **Content Filtering**: Automatically filters inappropriate language
- **Warning System**: Progressive warnings before bans
- **Activity Logging**: All interactions logged to designated channel
- **Error Handling**: Comprehensive error management and reporting

## 📊 Data Storage

The bot stores conversation data in `conversations.json` with:
- Timestamp
- User information
- Messages and responses
- Chat metadata

## 🚦 API Rate Limits

- **Gemini AI**: Respects Google's rate limits
- **Telegram Bot**: Handles rate limiting automatically
- **Error Recovery**: Graceful handling of API failures

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/cholan-ai-bot/issues) section
2. Create a new issue with detailed information
3. Contact the maintainers

## 🙏 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot API wrapper
- [Google Gemini AI](https://ai.google.dev/) - AI response generation
- Agricultural community for inspiration and feedback

## 📈 Roadmap

- [ ] Multi-language support
- [ ] Weather integration
- [ ] Crop price tracking
- [ ] Image recognition for plant diseases
- [ ] Advanced analytics dashboard
- [ ] Voice message support


📫 Creator & Contact

Creator: Narendra A
Email: narennarennatendra@gmail.com
---

**Made with ❤️ for the farming community**
Authors
Narendra Anbazhagan
Lokesh S
Deekshana CS
Darshana PS
