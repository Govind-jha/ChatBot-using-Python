# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("Jiraya")
chatbot.set_trainer(ListTrainer)

conversation = [
    "Hello",
    "Hi there!",
    "Hi there!",
    "Hello",
    "How are you doing?",
    "I'm doing great.",
    "Cool!",
    "^_^"
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("Hello")
print(response)

response = chatbot.get_response("I am hungry.")
print(response)