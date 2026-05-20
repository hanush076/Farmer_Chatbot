from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import sys
from terminal_chatbot import TerminalAgriChatbot
from voice_assistant import VoiceAssistant, text_to_audio, audio_to_text
import traceback

app = Flask(__name__)
CORS(app)

# Initialize voice assistant
voice_assistant = VoiceAssistant(language='en')

# Initialize chatbot
knowledge_base_path = "data/knowledge_base.json"
training_data_path = "data/processed_training_data.json"

try:
    chatbot = TerminalAgriChatbot(knowledge_base_path, training_data_path)
    app.chatbot = chatbot
    print("✓ Chatbot initialized successfully")
except Exception as e:
    print(f"✗ Error initializing chatbot: {e}")
    traceback.print_exc()

@app.route('/')
def index():
    """Serve the main chatbot page"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chatbot responses"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Please enter a message'
            }), 400
        
        # Get response from chatbot
        response = app.chatbot.get_response(user_message)
        
        return jsonify({
            'success': True,
            'message': user_message,
            'response': response
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/help', methods=['GET'])
def get_help():
    """API endpoint for help information"""
    try:
        stats = ""
        if app.chatbot.training_data and 'statistics' in app.chatbot.training_data:
            total_records = app.chatbot.training_data['statistics']['total_records']
            stats = f"I have access to {total_records:,} farming questions and answers from agricultural experts."
        
        help_text = f"""I can help you with:
• Crop diseases and treatments
• Irrigation and watering advice
• Fertilizer recommendations
• Government schemes and subsidies
• Weather-based farming tips
• Pest control methods
• Market information and selling tips
• Animal husbandry and livestock care

{stats}

Try asking questions like:
• "My tomato plants have brown spots"
• "Tell me about PM-KISAN scheme"
• "How to control aphids in brinjal?"
• "What fertilizer dose for rice?"
"""
        return jsonify({
            'success': True,
            'help': help_text
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """API endpoint for query categories"""
    categories = [
        {
            'name': 'Diseases & Pests',
            'icon': '🐛',
            'examples': [
                'My tomato plants have brown spots',
                'How to control aphids?',
                'What is powdery mildew?'
            ]
        },
        {
            'name': 'Irrigation',
            'icon': '💧',
            'examples': [
                'How often should I water wheat?',
                'Best irrigation method?',
                'How to prevent waterlogging?'
            ]
        },
        {
            'name': 'Fertilizers',
            'icon': '🌱',
            'examples': [
                'What fertilizer for rice?',
                'Nitrogen dose for tomatoes?',
                'What is SSP and MOP?'
            ]
        },
        {
            'name': 'Government Schemes',
            'icon': '🏛️',
            'examples': [
                'Tell me about PM-KISAN',
                'What is Kisan Credit Card?',
                'Government subsidies?'
            ]
        },
        {
            'name': 'Weather & Seasons',
            'icon': '🌤️',
            'examples': [
                'Monsoon farming tips',
                'Summer crop management',
                'Winter farming advice'
            ]
        },
        {
            'name': 'Market & Selling',
            'icon': '💹',
            'examples': [
                'Current market prices',
                'Selling tips',
                'Mandi information'
            ]
        }
    ]
    return jsonify({
        'success': True,
        'categories': categories
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'status': 'online',
        'chatbot': 'ready'
    })

@app.route('/api/voice/text-to-speech', methods=['POST'])
def text_to_speech_endpoint():
    """Convert text to speech (voice output)"""
    try:
        data = request.json
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'No text provided'
            }), 400
        
        # Convert text to speech
        result = voice_assistant.text_to_speech_base64(text)
        return jsonify(result)
    
    except Exception as e:
        print(f"Error in text_to_speech: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/voice/speech-to-text', methods=['POST'])
def speech_to_text_endpoint():
    """Convert speech to text (voice input)"""
    try:
        # Check if audio file is provided
        if 'audio' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No audio file provided'
            }), 400
        
        audio_file = request.files['audio']
        
        # Save audio file temporarily
        audio_path = f"temp_{audio_file.filename}"
        audio_file.save(audio_path)
        
        try:
            # Convert speech to text
            result = audio_to_text(audio_path)
            return jsonify(result)
        finally:
            # Clean up temporary file
            if os.path.exists(audio_path):
                os.remove(audio_path)
    
    except Exception as e:
        print(f"Error in speech_to_text: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/voice/chat', methods=['POST'])
def voice_chat():
    """Combined voice chat - speech to text, get response, text to speech"""
    try:
        data = request.json
        
        # Get text from voice input
        if 'audio' in request.files:
            audio_file = request.files['audio']
            audio_path = f"temp_{audio_file.filename}"
            audio_file.save(audio_path)
            
            try:
                result = audio_to_text(audio_path)
                if not result['success']:
                    return jsonify(result), 400
                user_message = result['text']
            finally:
                if os.path.exists(audio_path):
                    os.remove(audio_path)
        else:
            user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'No input provided'
            }), 400
        
        # Get chatbot response
        response = app.chatbot.get_response(user_message)
        
        # Convert response to speech
        audio_result = voice_assistant.text_to_speech_base64(response)
        
        if audio_result['success']:
            return jsonify({
                'success': True,
                'message': user_message,
                'response': response,
                'audio': audio_result['audio']
            })
        else:
            return jsonify({
                'success': True,
                'message': user_message,
                'response': response,
                'audio': None,
                'audio_error': audio_result.get('error')
            })
    
    except Exception as e:
        print(f"Error in voice_chat: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/voice/settings', methods=['GET', 'POST'])
def voice_settings():
    """Get or update voice settings"""
    if request.method == 'GET':
        try:
            voices = voice_assistant.get_available_voices()
            return jsonify({
                'success': True,
                'voices': voices,
                'current_language': voice_assistant.language
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    elif request.method == 'POST':
        try:
            data = request.json
            
            # Update language
            if 'language' in data:
                voice_assistant.set_language(data['language'])
            
            # Update speech rate
            if 'speech_rate' in data:
                rate = data['speech_rate']
                if 50 <= rate <= 300:
                    voice_assistant.set_speech_rate(rate)
            
            # Update volume
            if 'volume' in data:
                volume = data['volume']
                if 0.0 <= volume <= 1.0:
                    voice_assistant.set_volume(volume)
            
            return jsonify({
                'success': True,
                'message': 'Settings updated'
            })
        
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🌾 Farmer-Chatbot Web Server")
    print("="*60)
    print("Starting Flask development server...")
    print("🌐 Open your browser at: http://localhost:8000")
    print("="*60 + "\n")
    
    # Try port 8000, if not available use 5000
    import socket
    try:
        app.run(debug=False, host='0.0.0.0', port=8000, use_reloader=False)
    except OSError:
        print("Port 8000 unavailable, trying port 5000...")
        app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
