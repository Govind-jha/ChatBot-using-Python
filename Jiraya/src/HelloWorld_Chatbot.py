# # -*- coding: utf-8 -*-
# 
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# 
# 
# chatbot = ChatBot("Jiraya")
# chatbot.set_trainer(ListTrainer)
# 
# conversation = [
#     "Hello",
#     "Hi there!",
#     "Hi there!",
#     "Hello",
#     "How are you doing?",
#     "I'm doing great.",
#     "Cool!",
#     "^_^"
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome.",
# ]
# 
# chatbot.set_trainer(ListTrainer)
# chatbot.train(conversation)
# 
# response = chatbot.get_response("Hello")
# print(response)
# 
# response = chatbot.get_response("I am hungry.")
# print(response)

from chatterbot import ChatBot
import logging


'''
This is an example showing how to train a chat bot using the
Ubuntu Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    'Example Bot',
    trainer='chatterbot.trainers.UbuntuCorpusTrainer'
)

# Start by training our bot with the Ubuntu corpus data
chatbot.train()

# Now let's get a response to a greeting
response = chatbot.get_response('How are you doing today?')
print(response)