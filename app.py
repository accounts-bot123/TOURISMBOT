import os
from dotenv import load_dotenv
import streamlit as st
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Load environment variables
load_dotenv()

# Initialize Mistral client
api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="🌍 Tourism Bot",
    page_icon="🧳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stTitle {
        text-align: center;
        color: #1f77b4;
    }
    .chat-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
    }
    .user-message {
        background-color: #e3f2fd;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        border-left: 4px solid #1f77b4;
    }
    .bot-message {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        border-left: 4px solid #4caf50;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🌍 Tourism Bot - Your AI Travel Guide")
st.markdown("Powered by Mistral AI | Ask me anything about travel and destinations!")

# Sidebar
with st.sidebar:
    st.header("About Tourism Bot")
    st.write("""
    I'm your AI-powered tourism guide assistant. I can help you with:
    - Travel destinations and attractions
    - Hotel and accommodation recommendations
    - Local cuisine and restaurant suggestions
    - Transportation and travel logistics
    - Safety tips and travel advisories
    - Best times to visit places
    - Cultural and historical information
    - Activity and tour recommendations
    """)
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.success("Chat history cleared!")
    
    st.divider()
    st.subheader("Example Questions:")
    examples = [
        "What are the top attractions in Paris?",
        "Best hotels in Tokyo under $150/night?",
        "What's the best time to visit Bali?",
        "Tell me about street food in Bangkok",
        "How to travel safely in New York City?"
    ]
    for example in examples:
        st.caption(f"• {example}")

# Display chat history
st.subheader("Chat")
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message"><b>You:</b> {message["content"]}</div>', 
                       unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message"><b>Bot:</b> {message["content"]}</div>', 
                       unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Ask me about travel and tourism...")

if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Prepare messages for API call
    system_prompt = """You are an expert tourism guide assistant. 
You provide helpful information about:
- Travel destinations and attractions
- Hotels and accommodation recommendations
- Local cuisine and restaurants
- Transportation and logistics
- Travel tips and safety information
- Best times to visit places
- Cultural and historical information
- Activity and tour recommendations

Be friendly, informative, and provide practical advice for travelers."""
    
    messages = [ChatMessage(role="system", content=system_prompt)]
    for msg in st.session_state.messages:
        messages.append(ChatMessage(role=msg["role"], content=msg["content"]))
    
    try:
        # Get response from Mistral
        response = client.chat(
            model="mistral-small",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )
        
        # Extract assistant response
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        
        # Rerun to display the new messages
        st.rerun()
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Please check your API key and internet connection.")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.9em;">
    Tourism Bot v1.0 | Powered by Mistral AI
</div>
""", unsafe_allow_html=True)
