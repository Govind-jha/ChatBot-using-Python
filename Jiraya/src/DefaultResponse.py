# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from _overlapped import NULL


# Create a new instance of a ChatBot
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.45,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
              # Read input from terminal
    input_adapter="chatterbot.input.TerminalAdapter",   
    # Display output on terminal
    output_adapter="chatterbot.output.TerminalAdapter",
    trainer='chatterbot.trainers.ListTrainer'
)

# Train the chat bot with a few responses
bot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# Get a response for some unexpected input
while True:
    try:
        response = bot.get_response(NULL)
    
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
