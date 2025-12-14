# Tourism Bot - Mistral AI Powered

A conversational tourism guide bot powered by Mistral AI API.

## Features

- **Interactive Conversation**: Chat with an AI tourism guide
- **Expert Knowledge**: Get information about destinations, hotels, restaurants, and travel tips
- **Conversation History**: Maintains context across multiple messages
- **Easy to Use**: Simple command-line interface

## Setup

### 1. Prerequisites
- Python 3.8 or higher
- Virtual environment (already created)

### 2. Install Dependencies

With the virtual environment activated:
```bash
pip install -r requirements.txt
```

### 3. Configuration

The API key is already set in the `.env` file:
```
MISTRAL_API_KEY=rXATKLEZqD4bOIvJQrvHWkTB4COW0DII
```

## Usage

### Run the Bot

```bash
python tourism_bot.py
```

### Commands

- **quit**: Exit the bot
- **clear**: Clear conversation history
- **help**: Show available commands

### Example Queries

- "What are the best attractions in Paris?"
- "Recommend me a hotel in Tokyo"
- "What's the best time to visit Bali?"
- "Tell me about local cuisine in Thailand"
- "What's the safest way to travel in New York City?"

## How It Works

The bot uses the Mistral AI API with the following components:

1. **System Prompt**: Defines the bot's role as a tourism guide
2. **Conversation History**: Maintains context for multi-turn conversations
3. **Chat API**: Sends messages to Mistral and receives responses
4. **Interactive Loop**: Allows continuous conversation with the user

## File Structure

```
Tourism_bot/
├── tourism_bot.py      # Main bot application
├── requirements.txt    # Python dependencies
├── .env               # API key configuration
├── README.md          # This file
└── venv/              # Virtual environment
```

## Notes

- Keep your API key secure. Never share it publicly.
- The bot maintains conversation history for context awareness.
- Responses are generated using the "mistral-small" model.

## Troubleshooting

If you encounter issues:

1. **Module not found**: Make sure the virtual environment is activated and dependencies are installed
2. **API Key errors**: Verify the API key in `.env` file
3. **Connection issues**: Check your internet connection and Mistral API status

## License

This project uses the Mistral AI API. Please refer to Mistral's terms of service.
