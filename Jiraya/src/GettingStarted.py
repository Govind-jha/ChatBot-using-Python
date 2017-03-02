# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.chatterbot import ChatBot


bot = ChatBot(
    # Bot Name
    "Jiraya",
    # Type of adapter for database
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    # Read input from terminal
    input_adapter="chatterbot.input.TerminalAdapter",
    # Display output on terminal
    output_adapter="chatterbot.output.TerminalAdapter",
    # Logic adapters, takes an input and generate a response 
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    # Database location
    database="./database.json"
)

print("Type something to begin...") 

while True:
    try:
        bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
