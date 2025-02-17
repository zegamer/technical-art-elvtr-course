from utils import load_messages

# Load messages
FOLLOW_MESSAGES = load_messages("assignment_1/portfolio/annoying_messages.txt")
CONVERSATION_MESSAGES = load_messages("assignment_1/portfolio/conversation.txt")

# Message settings
CONVERSATION_TRACKER = 0
MESSAGE_DISPLAY_TIME = 2000  # Time to display each message in milliseconds