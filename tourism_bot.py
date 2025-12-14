import os
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Load environment variables
load_dotenv()

# Initialize Mistral client
api_key = os.getenv("MISTRAL_API_KEY")
client = MistralClient(api_key=api_key)

class TourismBot:
    def __init__(self):
        self.model = "mistral-small"
        self.conversation_history = []
        self.system_prompt = """You are an expert tourism guide assistant. 
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

    def chat(self, user_message: str) -> str:
        """Send a message to the bot and get a response."""
        
        # Add user message to history
        self.conversation_history.append(ChatMessage(role="user", content=user_message))
        
        # Prepare messages for API call
        messages = [ChatMessage(role="system", content=self.system_prompt)] + self.conversation_history
        
        # Get response from Mistral
        response = client.chat(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )
        
        # Extract assistant response
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to history
        self.conversation_history.append(ChatMessage(role="assistant", content=assistant_message))
        
        return assistant_message

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []

    def run_interactive(self):
        """Run the bot in interactive mode."""
        print("🌍 Tourism Bot - Powered by Mistral AI")
        print("=" * 50)
        print("Welcome! I'm your tourism guide. Ask me anything about travel and destinations!")
        print("Type 'quit' to exit, 'clear' to clear history, or 'help' for options.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == 'quit':
                    print("Thank you for using Tourism Bot. Safe travels! 🧳")
                    break
                
                if user_input.lower() == 'clear':
                    self.clear_history()
                    print("Conversation history cleared.\n")
                    continue
                
                if user_input.lower() == 'help':
                    print("\nAvailable commands:")
                    print("  quit  - Exit the bot")
                    print("  clear - Clear conversation history")
                    print("  help  - Show this help message\n")
                    continue
                
                print("\nBot: ", end="", flush=True)
                response = self.chat(user_input)
                print(response + "\n")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}\n")

def main():
    """Main function."""
    bot = TourismBot()
    bot.run_interactive()

if __name__ == "__main__":
    main()
