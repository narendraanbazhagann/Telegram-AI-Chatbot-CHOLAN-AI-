# 🌾 Cholan AI - Agricultural Assistant Bot

A friendly Telegram bot designed to assist with agricultural questions and provide farming-related information. Built with Python using the python-telegram-bot library and powered by Google's Gemini AI.

## ✨ Features

- **AI-Powered Responses**: Uses Google Gemini to answer agricultural questions
- **Fun Commands**: Jokes, trivia, and "would you rather" questions about farming
- **Moderation System**: Built-in word filtering and user warning system  
- **Activity Logging**: Logs all interactions to a Telegram channel
- **Emoji Reactions**: Responds with relevant emojis to keywords
- **Time-Aware Greetings**: Provides appropriate greetings based on time of day

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Google Gemini API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cholan-ai-bot.git
   cd cholan-ai-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual tokens
   ```

5. **Run the bot**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

Edit the configuration in `config.py`:

- `TOKEN`: Your Telegram bot token
- `BOT_USERNAME`: Your bot's username  
- `CHANNEL_ID`: Channel for activity logging
- `GEMINI_API_KEY`: Your Google Gemini API key
- `BANNED_WORDS`: List of prohibited words
- `MAX_WARNINGS`: Maximum warnings before ban

## 📁 Project Structure

```
cholan-ai-bot/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── handlers/
│   ├── __init__.py       # Package initialization
│   ├── commands.py       # Command handlers
│   └── messages.py       # Message handlers
├── utils/
│   ├── __init__.py       # Package initialization
│   ├── ai_handler.py     # AI response logic
│   ├── moderation.py     # User moderation utilities
│   └── logger.py         # Logging utilities
└── data/
    ├── __init__.py       # Package initialization
    └── content.py        # Static content (jokes, trivia, etc.)
```

## 🤖 Commands

- `/start` - Initialize the bot
- `/help` - Show help message and available commands
- `/joke` - Get a random farming joke
- `/trivia` - Get an agriculture trivia question
- `/wouldyourather` - Get a fun farming-related choice question
- `/custom` - Reset your warning count

## 🔧 Development

### Adding New Commands

1. Add your command handler to `handlers/commands.py`
2. Register it in `main.py`
3. Update the help text if needed

### Adding New Content

- **Jokes**: Add to `jokes` list in `data/content.py`
- **Trivia**: Add to `trivia_questions` list in `data/content.py`
- **Would You Rather**: Add to `would_you_rather_questions` list in `data/content.py`

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🛡️ Moderation

The bot includes a built-in moderation system:

- Users get warnings for inappropriate language
- After 3 warnings, users are temporarily banned
- Admins can reset warnings using `/custom`
- All moderation actions are logged to the activity channel

## 📊 Logging

- All user interactions are logged to a JSON file
- Activity is also sent to a designated Telegram channel
- Error handling with detailed logging

## 🌍 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment
Consider using:
- **Heroku**: Easy deployment with git integration
- **VPS**: More control, use systemd or PM2 for process management
- **Docker**: Containerized deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- Agricultural knowledge and farming community inspiration

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/cholan-ai-bot/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

---

**Happy Farming! 🌾🚜**