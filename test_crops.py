#!/usr/bin/env python3
from terminal_chatbot import TerminalAgriChatbot

chatbot = TerminalAgriChatbot('data/knowledge_base.json', 'data/processed_training_data.json')

# Test vegetables
print("VEGETABLES:")
print("="*50)
vegetables = ['cauliflower', 'spinach', 'carrot', 'brinjal', 'bell pepper', 'okra', 'radish', 'peas']
for veg in vegetables:
    response = chatbot.get_response(f'What fertilizer for {veg}?')
    if 'Fertilizer Recommendations' in response:
        print(f'✓ {veg.upper()}')

# Test fruits  
print("\nFRUITS:")
print("="*50)
fruits = ['orange', 'grapes', 'strawberry', 'papaya', 'watermelon', 'guava', 'pomegranate']
for fruit in fruits:
    response = chatbot.get_response(f'What fertilizer for {fruit}?')
    if 'Fertilizer Recommendations' in response:
        print(f'✓ {fruit.upper()}')

print("\nDone!")
