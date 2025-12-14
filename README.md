# 🌍 Tourism Bot - Mistral AI Powered

A conversational tourism guide bot powered by Mistral AI API with Streamlit web interface.

## Features

- **🎨 Web Interface**: Beautiful Streamlit web UI
- **💬 Interactive Conversation**: Chat with an AI tourism guide
- **🌏 Expert Knowledge**: Get information about destinations, hotels, restaurants, and travel tips
- **📝 Conversation History**: Maintains context across multiple messages
- **🚀 CLI Mode**: Also works as command-line interface
- **⚡ Fast Response**: Powered by Mistral Small model

## Deployment Options

### Option 1: Run Locally (Streamlit)

#### Prerequisites
- Python 3.8 or higher
- pip package manager

#### Installation

1. Clone the repository:
```bash
git clone https://github.com/accounts-bot123/TOURISMBOT.git
cd TOURISMBOT
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Option 2: Command-Line Mode

```bash
python tourism_bot.py
```

### Commands (CLI Mode)

- **quit**: Exit the bot
- **clear**: Clear conversation history
- **help**: Show available commands

### Option 3: Deploy to Streamlit Cloud

1. Push your code to GitHub (already done!)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Connect your GitHub repository
5. Select `TOURISMBOT` repo and `main` branch
6. Set the main file to `app.py`
7. Add secrets in the Streamlit Cloud dashboard:
   - `MISTRAL_API_KEY`: Your Mistral API key

The app will be live at: `https://<your-username>-tourismbot.streamlit.app`

## Example Queries

- "What are the best attractions in Paris?"
- "Recommend me a hotel in Tokyo under $150/night"
- "What's the best time to visit Bali?"
- "Tell me about local cuisine in Thailand"
- "What's the safest way to travel in New York City?"
- "What are the top museums in London?"
- "Best beaches for a family vacation?"

## File Structure

```
TOURISMBOT/
├── app.py                  # Streamlit web application
├── tourism_bot.py          # CLI bot application
├── requirements.txt        # Python dependencies
├── .env                    # API key configuration (local only)
├── .gitignore             # Git ignore rules
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── README.md              # This file
└── venv/                  # Virtual environment
```

## Configuration

### Local Setup (.env file)
```
MISTRAL_API_KEY=your_api_key_here
```

### Streamlit Cloud Setup
Add your API key as a secret in Streamlit Cloud dashboard:
- In your app settings, go to "Secrets"
- Add: `MISTRAL_API_KEY = "your_api_key_here"`

## How It Works

The bot uses the Mistral AI API with:

1. **System Prompt**: Defines the bot's role as a tourism expert
2. **Conversation History**: Maintains context for multi-turn conversations
3. **Mistral Small Model**: Fast and efficient AI responses
4. **Streamlit UI**: Beautiful interactive web interface

## Requirements

- mistralai>=0.1.0
- python-dotenv==1.0.0
- streamlit>=1.28.0

## Troubleshooting

### Module not found
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

### API Key errors
- Verify `MISTRAL_API_KEY` is set correctly in `.env` or Streamlit secrets

### Connection issues
- Check internet connection
- Verify Mistral API status at https://status.mistral.ai/

### Streamlit Cloud issues
- Ensure `app.py` is in the root directory
- Check that API key is added to Streamlit Cloud secrets
- Review deployment logs in Streamlit Cloud dashboard

## GitHub Repository

[accounts-bot123/TOURISMBOT](https://github.com/accounts-bot123/TOURISMBOT)

## License

This project uses the Mistral AI API. Please refer to [Mistral's terms of service](https://mistral.ai).
