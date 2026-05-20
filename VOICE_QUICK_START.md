# Voice Assistance Quick Start

## 🎤 Getting Started with Voice

### For Web Users

#### 1. Voice Input (Speak to Chat)
```
1. Click the 🎤 microphone button
2. Speak your question (e.g., "How to grow tomatoes?")
3. Click Send or auto-submit
4. Get response from chatbot
```

#### 2. Voice Output (Hear Responses)
```
1. Click the 🎙️ Voice button (sidebar)
2. Toggle "Auto-play responses" ON
3. Select your language
4. Adjust speed and volume
5. Chat normally - responses are now spoken!
```

#### 3. Test Voice Quality
```
1. Open Voice Settings (🎙️)
2. Click "Test Voice" button
3. Hear a sample message
4. Adjust settings as needed
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Microphone (for voice input)
- Speakers (for voice output)

### Installation

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Start the web app**
```bash
python app.py
```

3. **Open in browser**
```
http://localhost:8000
```

4. **Allow microphone access** when prompted

---

## 🎯 Voice Settings

| Setting | Options | Default |
|---------|---------|---------|
| **Language** | English, Hindi, Spanish, French | English |
| **Speech Rate** | 50-300 WPM | 150 |
| **Volume** | 0-100% | 90% |
| **Auto-play** | On/Off | On |

---

## 💡 Usage Tips

### Best Practices
- ✅ Speak clearly and naturally
- ✅ Use quiet environment
- ✅ Select correct language
- ✅ Test volume before use

### Common Tasks

**Ask about crop diseases**
- "What pests affect tomatoes?"
- "How to treat potato blight?"
- "हटरमट्टर में क्या रोग हैं?" (Hindi)

**Get market information**
- "What's the tomato price today?"
- "Where can I sell onions?"
- "बाजार में गेहूं की कीमत क्या है?" (Hindi)

**Learn growing techniques**
- "How to water vegetables?"
- "Best fertilizer for chili?"
- "धान उगाने का तरीका क्या है?" (Hindi)

---

## 🔧 Troubleshooting

### Microphone Not Working
```
✓ Check browser permissions
✓ Allow microphone access
✓ Test microphone in system settings
✓ Try different browser
```

### Can't Hear Responses
```
✓ Check speaker volume
✓ Disable mute button
✓ Check browser volume
✓ Enable Auto-play in settings
```

### Language Not Working
```
✓ Select language in Voice Settings
✓ Speak in selected language
✓ Refresh browser
✓ Check browser console for errors
```

---

## 📱 Mobile Support

### iOS (Safari)
- ✅ Speech-to-text: Chrome or Safari
- ✅ Text-to-speech: Supported
- ⚠️ Requires iOS 15+

### Android (Chrome)
- ✅ Speech-to-text: Supported
- ✅ Text-to-speech: Supported
- ✅ Works offline for TTS

---

## 🌍 Supported Languages

| Language | Code | Status |
|----------|------|--------|
| English | en | ✅ Full support |
| Hindi | hi | ✅ Full support |
| Spanish | es | ✅ Full support |
| French | fr | ✅ Full support |

---

## 📚 API Quick Reference

### Voice Input
```
POST /api/voice/speech-to-text
Input: audio file
Output: transcribed text
```

### Voice Output
```
POST /api/voice/text-to-speech
Input: text
Output: audio (base64)
```

### Combined Chat
```
POST /api/voice/chat
Input: audio or text
Output: response + audio
```

### Settings
```
GET/POST /api/voice/settings
Get/update language, speed, volume
```

---

## 🎓 Examples

### Python Example
```python
from voice_assistant import VoiceAssistant

# Create voice assistant
va = VoiceAssistant(language='hi')

# Get voice input
text = va.speech_to_text_from_microphone()
# User speaks: "गेहूं कैसे उगाते हैं?"

# Send to chatbot
from terminal_chatbot import TerminalAgriChatbot
chatbot = TerminalAgriChatbot()
response = chatbot.get_response(text)

# Convert to speech
va.text_to_speech(response)
# Chatbot speaks the answer!
```

### JavaScript Example
```javascript
// Start listening
voiceAssistant.startListening();

// Listen for transcription in input field
// Then send message...

// Speak response
voiceAssistant.speakText("Your text here");

// Change language
voiceAssistant.updateVoiceSetting('language', 'hi');
```

---

## ⚙️ Advanced Configuration

### Change Default Voice Settings
Edit in `static/voice.js`:
```javascript
let voiceSettings = {
    enabled: true,
    autoPlay: true,        // Auto-play responses
    language: 'en',        // Default language
    speechRate: 150,       // Words per minute
    volume: 0.9            // 0-1 scale
};
```

### Change Backend Voice Settings
Edit in `voice_assistant.py`:
```python
self.engine.setProperty('rate', 150)    # Speech rate
self.engine.setProperty('volume', 0.9)  # Volume 0-1
```

---

## 🆘 Need Help?

### Check Logs
```bash
# Terminal logs show voice API errors
# Browser console (F12) shows frontend errors
```

### Common Error Messages

| Error | Solution |
|-------|----------|
| "No speech detected" | Speak louder, check mic |
| "Microphone denied" | Allow permission in browser |
| "No audio output" | Check speaker volume |
| "Language not supported" | Choose supported language |

---

## 📞 Support Resources

- GitHub Issues: [Report bugs]
- Documentation: See VOICE_FEATURES_GUIDE.md
- Video Tutorials: [Coming soon]
- Community Forum: [Coming soon]

---

**Ready to go?** 
1. Start the app: `python app.py`
2. Open browser: `http://localhost:8000`
3. Click 🎤 to start talking!

Enjoy voice-powered farming assistance! 🌾
