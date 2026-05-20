# Voice Features Guide for Farmer Chatbot

## Overview
The Farmer Chatbot now includes comprehensive voice assistance capabilities, allowing farmers to interact via speech input and receive spoken responses. This makes the chatbot more accessible for users who prefer voice communication.

## Features

### 1. Speech-to-Text (STT)
- **Web Browser**: Uses Web Speech API (native browser support)
- **Python Backend**: Uses SpeechRecognition library with multiple engine support
- Supports multiple languages (English, Hindi, Spanish, French)
- Real-time speech recognition with interim results

### 2. Text-to-Speech (TTS)
- **Backend**: Uses pyttsx3 for offline speech synthesis
- No external API required (works offline)
- Configurable speech rate (50-300 WPM)
- Adjustable volume control (0-100%)
- Auto-play feature for automatic responses

### 3. Voice Settings
- Language selection (English, Hindi, Spanish, French)
- Speech rate adjustment
- Volume control
- Auto-play toggle
- Test voice functionality

## Usage

### Web Interface

#### Voice Input
1. Click the microphone button (🎤) in the chat input area
2. Speak your question or message clearly
3. The app will transcribe your speech and display it in the input field
4. Press Send or let the auto-send feature process it

#### Voice Output
1. Go to Voice Settings (🎙️ button in sidebar)
2. Enable "Auto-play responses"
3. Adjust language, speed, and volume as needed
4. Click "Test Voice" to hear a sample
5. All chatbot responses will now be spoken automatically

#### Voice Settings Modal
- **Language**: Select from English, Hindi, Spanish, or French
- **Speech Rate**: Adjust speed (50-300 words per minute)
- **Volume**: Adjust output volume (0-100%)
- **Auto-play**: Toggle automatic speech for responses

### Terminal Chatbot

Use the voice features in terminal chatbot:

```python
from terminal_chatbot import TerminalAgriChatbot
from voice_assistant import VoiceAssistant

chatbot = TerminalAgriChatbot()
voice_assistant = VoiceAssistant(language='hi')  # Hindi

# Get speech input
user_speech = voice_assistant.speech_to_text_from_microphone()

# Process through chatbot
response = chatbot.get_response(user_speech)

# Convert to speech
voice_assistant.text_to_speech(response)
```

## API Endpoints

### Text-to-Speech
**POST** `/api/voice/text-to-speech`

Request:
```json
{
    "text": "Your text here"
}
```

Response:
```json
{
    "success": true,
    "audio": "data:audio/wav;base64,..."
}
```

### Speech-to-Text
**POST** `/api/voice/speech-to-text`

Request:
```json
{
    "audio": "base64_encoded_audio_file"
}
```

Response:
```json
{
    "success": true,
    "text": "Transcribed text"
}
```

### Voice Chat
**POST** `/api/voice/chat`

Combined endpoint for voice input and output:

Request:
```json
{
    "audio": "base64_encoded_audio_file",
    "text": "or text if no audio"
}
```

Response:
```json
{
    "success": true,
    "response": "Chatbot response text",
    "audio": "data:audio/wav;base64,..."
}
```

### Voice Settings
**GET/POST** `/api/voice/settings`

GET - Returns current settings:
```json
{
    "language": "en",
    "speech_rate": 150,
    "volume": 0.9
}
```

POST - Update settings:
```json
{
    "language": "hi",
    "speech_rate": 175,
    "volume": 0.8
}
```

## Technical Architecture

### Frontend (JavaScript)
- **voice.js**: Main voice module
  - Web Speech API integration for speech recognition
  - Audio playback using HTML5 Audio API
  - Modal management for settings
  - Real-time UI feedback

### Backend (Python)
- **voice_assistant.py**: VoiceAssistant class
  - pyttsx3 for offline TTS
  - SpeechRecognition for STT
  - Audio encoding/decoding with base64
  - Settings management

- **app.py**: Flask endpoints
  - `/api/voice/*` endpoints
  - Request validation
  - Response formatting
  - CORS support for web frontend

## Browser Compatibility

### Speech-to-Text (Web Speech API)
- ✅ Chrome/Chromium (v25+)
- ✅ Edge (v79+)
- ✅ Safari (v15+)
- ✅ Firefox (v25+)
- ⚠️ May require HTTPS (except localhost)

### Text-to-Speech
- ✅ All modern browsers (via Audio API)
- ✅ Mobile browsers (iOS Safari, Chrome Android)

## Requirements

### Python Packages
```
pyttsx3>=2.90          # Text-to-speech
SpeechRecognition>=3.10.0  # Speech-to-text
flask>=2.3.3           # Web framework
```

### Installation
```bash
pip install -r requirements.txt
```

## Troubleshooting

### Speech Recognition Not Working
1. Check microphone permissions in browser
2. Ensure microphone is connected and working
3. Try a different browser
4. Check browser console for errors

### Audio Playback Not Working
1. Check volume settings
2. Verify speaker/audio output is working
3. Try a different browser
4. Check for browser autoplay policies

### Language Not Changing
1. Refresh the page
2. Check that language selection is properly saved
3. Verify language code is valid (en, hi, es, fr)

### Offline Issues
- TTS works offline (pyttsx3 is local)
- STT may require internet for some features
- Ensure internet connection for speech recognition

## Best Practices

1. **Speak Clearly**: Enunciate clearly for better recognition
2. **Avoid Background Noise**: Use in quiet environments
3. **Check Microphone**: Test microphone before using
4. **Language Selection**: Choose correct language for better results
5. **Volume Management**: Adjust volume to comfortable level

## Future Enhancements

- [ ] Support for more languages
- [ ] Custom wake words
- [ ] Voice commands for quick actions
- [ ] Multilingual support (mixed language input)
- [ ] Voice preference profiles
- [ ] Audio file upload support
- [ ] Conversation history with audio

## Support

For issues or questions about voice features:
1. Check browser console for error messages
2. Verify browser compatibility
3. Test microphone permissions
4. Check network connectivity
5. Review API endpoint responses

## Code Examples

### Using Voice in Web Frontend

```javascript
// Start listening
voiceAssistant.startListening();

// Speak text
voiceAssistant.speakText("Hello farmer!");

// Update settings
voiceAssistant.updateVoiceSetting('language', 'hi');

// Test voice
voiceAssistant.testVoice();
```

### Using Voice in Python

```python
from voice_assistant import VoiceAssistant

va = VoiceAssistant(language='hi')

# Set language
va.set_language('hi')

# Get speech input
text = va.speech_to_text_from_microphone()

# Generate speech output
audio_data = va.text_to_speech("नमस्ते किसान!")
```

## Privacy & Permissions

- Microphone access requires user permission
- Audio data is processed locally when possible
- No voice data is stored permanently
- Settings are stored in browser localStorage

---

**Last Updated**: 2024
**Version**: 1.0
