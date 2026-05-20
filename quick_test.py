from terminal_chatbot import TerminalAgriChatbot
chatbot = TerminalAgriChatbot('data/knowledge_base.json', 'data/processed_training_data.json')
for crop in ['bell pepper', 'beans', 'cucumber', 'lemon', 'pineapple', 'corn', 'sugarcane']:
    r = chatbot.get_response(f'Fertilizer for {crop}')
    print(f"{'✓' if 'Fertilizer Recommendations' in r else '✗'} {crop}")
