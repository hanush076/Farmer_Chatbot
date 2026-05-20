"""
Voice Assistance Module for Farmer Chatbot
Handles Speech-to-Text (STT) and Text-to-Speech (TTS)
"""

import pyttsx3
import speech_recognition as sr
from io import BytesIO
import base64
import logging

logger = logging.getLogger(__name__)


class VoiceAssistant:
    """Handles voice input and output for the chatbot"""
    
    def __init__(self, language='en'):
        """
        Initialize voice assistant
        
        Args:
            language (str): Language code for TTS and STT
        """
        self.language = language
        
        # Initialize Text-to-Speech
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)  # Speaking rate
        self.tts_engine.setProperty('volume', 0.9)  # Volume
        
        # Initialize Speech-to-Text
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        
    def text_to_speech(self, text, save_to_file=False):
        """
        Convert text to speech
        
        Args:
            text (str): Text to convert to speech
            save_to_file (bool): If True, save to file; if False, return as bytes
            
        Returns:
            str or bytes: File path if save_to_file=True, else audio bytes
        """
        try:
            if save_to_file:
                # Save to file
                output_file = "response_audio.mp3"
                self.tts_engine.save_to_file(text, output_file)
                self.tts_engine.runAndWait()
                logger.info(f"Audio saved to {output_file}")
                return output_file
            else:
                # Return as bytes
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
                logger.info("Audio generated")
                return True
                
        except Exception as e:
            logger.error(f"Error in text_to_speech: {e}")
            raise
    
    def speech_to_text_from_microphone(self):
        """
        Capture audio from microphone and convert to text
        
        Returns:
            str: Recognized text or error message
        """
        try:
            with sr.Microphone() as source:
                logger.info("Listening for speech input...")
                audio = self.recognizer.listen(source, timeout=10)
                
            # Try to recognize speech using Google Speech Recognition
            try:
                text = self.recognizer.recognize_google(
                    audio, 
                    language=self.language
                )
                logger.info(f"Recognized: {text}")
                return {
                    'success': True,
                    'text': text
                }
            except sr.UnknownValueError:
                return {
                    'success': False,
                    'error': 'Could not understand audio. Please speak clearly.'
                }
            except sr.RequestError as e:
                return {
                    'success': False,
                    'error': f'Error with speech recognition service: {e}'
                }
                
        except sr.RequestError as e:
            return {
                'success': False,
                'error': f'Could not request results: {e}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Error capturing audio: {e}'
            }
    
    def speech_to_text_from_file(self, audio_file_path):
        """
        Convert speech from audio file to text
        
        Args:
            audio_file_path (str): Path to audio file
            
        Returns:
            dict: Recognition result
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio = self.recognizer.record(source)
            
            try:
                text = self.recognizer.recognize_google(
                    audio, 
                    language=self.language
                )
                return {
                    'success': True,
                    'text': text
                }
            except sr.UnknownValueError:
                return {
                    'success': False,
                    'error': 'Could not understand audio'
                }
            except sr.RequestError as e:
                return {
                    'success': False,
                    'error': f'Error with speech recognition service: {e}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Error processing audio file: {e}'
            }
    
    def text_to_speech_base64(self, text):
        """
        Convert text to speech and return as base64 encoded audio
        For web browser playback
        
        Args:
            text (str): Text to convert
            
        Returns:
            str: Base64 encoded audio data
        """
        try:
            # Save to temporary file
            import tempfile
            import os
            
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp_file:
                tmp_path = tmp_file.name
            
            # Generate audio
            self.tts_engine.save_to_file(text, tmp_path)
            self.tts_engine.runAndWait()
            
            # Read and encode as base64
            with open(tmp_path, 'rb') as f:
                audio_bytes = f.read()
            
            # Clean up temp file
            os.unlink(tmp_path)
            
            # Encode as base64
            base64_audio = base64.b64encode(audio_bytes).decode('utf-8')
            return {
                'success': True,
                'audio': f'data:audio/mp3;base64,{base64_audio}'
            }
            
        except Exception as e:
            logger.error(f"Error in text_to_speech_base64: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def set_language(self, language_code):
        """
        Set language for TTS and STT
        
        Args:
            language_code (str): Language code (e.g., 'en', 'hi', 'es')
        """
        self.language = language_code
        logger.info(f"Language set to {language_code}")
    
    def set_speech_rate(self, rate):
        """
        Set speech rate for TTS
        
        Args:
            rate (int): Speech rate (50-300, default 150)
        """
        self.tts_engine.setProperty('rate', rate)
        logger.info(f"Speech rate set to {rate}")
    
    def set_volume(self, volume):
        """
        Set volume for TTS
        
        Args:
            volume (float): Volume level (0.0-1.0)
        """
        self.tts_engine.setProperty('volume', volume)
        logger.info(f"Volume set to {volume}")
    
    def get_available_voices(self):
        """
        Get available voices for TTS
        
        Returns:
            list: List of available voices
        """
        try:
            voices = self.tts_engine.getProperty('voices')
            voice_info = []
            for voice in voices:
                voice_info.append({
                    'id': voice.id,
                    'name': voice.name,
                    'languages': voice.languages if hasattr(voice, 'languages') else []
                })
            return voice_info
        except Exception as e:
            logger.error(f"Error getting voices: {e}")
            return []


# Utility functions for Flask routes

def initialize_voice_assistant(language='en'):
    """Initialize and return VoiceAssistant instance"""
    return VoiceAssistant(language=language)


def text_to_audio(text, language='en'):
    """
    Quick function to convert text to audio
    
    Args:
        text (str): Text to convert
        language (str): Language code
        
    Returns:
        dict: Audio data and metadata
    """
    try:
        voice_assistant = VoiceAssistant(language=language)
        result = voice_assistant.text_to_speech_base64(text)
        return result
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def audio_to_text(audio_file_path, language='en'):
    """
    Quick function to convert audio to text
    
    Args:
        audio_file_path (str): Path to audio file
        language (str): Language code
        
    Returns:
        dict: Recognized text and metadata
    """
    try:
        voice_assistant = VoiceAssistant(language=language)
        result = voice_assistant.speech_to_text_from_file(audio_file_path)
        return result
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
