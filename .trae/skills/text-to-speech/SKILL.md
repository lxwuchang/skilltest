---
name: text-to-speech
description: Converts text to speech in Chinese and English. Invoke when user needs to generate audio from text, create voiceovers, or implement TTS functionality.
---

# Text to Speech (文字转语音)

This skill provides text-to-speech capabilities for both Chinese and English languages, converting written text into natural-sounding audio.

## When to Use

Invoke this skill when:
- User wants to convert text to speech
- User needs to generate audio from written content
- User wants to create voiceovers for videos or presentations
- User needs accessibility features for text content
- User wants to implement TTS in applications

## Capabilities

### Language Support
- **Chinese (中文)**: Mandarin, Cantonese, and other dialects
- **English**: US, UK, Australian, and other accents
- **Mixed Language**: Automatic language detection and switching

### Voice Options
- Multiple voice types (male, female, neutral)
- Adjustable speaking rate
- Pitch control
- Volume control
- Emotion and tone variations

### Output Formats
- MP3 audio files
- WAV audio files
- OGG audio files
- Streaming audio playback

## Implementation Options

### Option 1: Python pyttsx3 (Offline)

```python
import pyttsx3

def text_to_speech(text, language='en', output_file='output.mp3'):
    engine = pyttsx3.init()
    
    # Configure voice
    voices = engine.getProperty('voices')
    
    # Select voice based on language
    if language == 'zh':
        # Find Chinese voice
        for voice in voices:
            if 'chinese' in voice.name.lower() or 'zh' in voice.id.lower():
                engine.setProperty('voice', voice.id)
                break
    else:
        # Use English voice
        for voice in voices:
            if 'english' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    
    # Set properties
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 1.0)  # Volume
    
    # Save to file
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    
    return output_file

# Usage
text_to_speech("Hello, this is a test.", language='en', output_file='test.mp3')
text_to_speech("你好，这是一个测试。", language='zh', output_file='test_cn.mp3')
```

### Option 2: Google Text-to-Speech (gTTS)

```python
from gtts import gTTS
import os

def google_tts(text, language='en', output_file='output.mp3'):
    # Language codes: 'en' for English, 'zh-CN' for Chinese
    lang_code = 'zh-CN' if language == 'zh' else 'en'
    
    tts = gTTS(text=text, lang=lang_code, slow=False)
    tts.save(output_file)
    
    return output_file

# Usage
google_tts("Hello, world!", language='en', output_file='hello.mp3')
google_tts("你好，世界！", language='zh', output_file='nihao.mp3')
```

### Option 3: Azure Cognitive Services

```python
import azure.cognitiveservices.speech as speechsdk

def azure_tts(text, language='en-US', voice_name='en-US-JennyNeural', output_file='output.wav'):
    speech_config = speechsdk.SpeechConfig(
        subscription='YOUR_AZURE_KEY',
        region='YOUR_AZURE_REGION'
    )
    
    # Set voice
    speech_config.speech_synthesis_voice_name = voice_name
    
    # Configure audio output
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
    
    # Create synthesizer
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )
    
    # Synthesize
    result = synthesizer.speak_text_async(text).get()
    
    return output_file

# Usage
azure_tts("Hello from Azure!", language='en-US', voice_name='en-US-JennyNeural')
azure_tts("你好，Azure！", language='zh-CN', voice_name='zh-CN-XiaoxiaoNeural')
```

### Option 4: OpenAI TTS API

```python
from openai import OpenAI

def openai_tts(text, voice='alloy', output_file='output.mp3'):
    client = OpenAI(api_key='YOUR_OPENAI_KEY')
    
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,  # alloy, echo, fable, onyx, nova, shimmer
        input=text
    )
    
    # Save to file
    response.stream_to_file(output_file)
    
    return output_file

# Usage
openai_tts("Hello from OpenAI!", voice='alloy', output_file='openai_test.mp3')
```

## Installation

### Python Libraries

```bash
# Offline TTS
pip install pyttsx3

# Google TTS (requires internet)
pip install gtts

# Azure TTS
pip install azure-cognitiveservices-speech

# OpenAI TTS
pip install openai

# Audio playback
pip install pygame
pip install playsound
```

### System Dependencies

```bash
# macOS
brew install espeak

# Linux (Ubuntu/Debian)
sudo apt-get install espeak espeak-ng

# Windows
# pyttsx3 uses built-in SAPI5
```

## Voice Selection

### Chinese Voices
- `zh-CN-XiaoxiaoNeural` - Female, Mandarin (Azure)
- `zh-CN-YunxiNeural` - Male, Mandarin (Azure)
- `zh-CN-YunyangNeural` - Male, Mandarin (Azure)
- `zh-HK-HiuGaaiNeural` - Female, Cantonese (Azure)
- `zh-TW-HsiaoChenNeural` - Female, Taiwan Mandarin (Azure)

### English Voices
- `en-US-JennyNeural` - Female, US English (Azure)
- `en-US-GuyNeural` - Male, US English (Azure)
- `en-GB-SoniaNeural` - Female, UK English (Azure)
- `en-AU-NatashaNeural` - Female, Australian English (Azure)

## Best Practices

### Text Preparation
- Clean and normalize text before synthesis
- Handle special characters and abbreviations
- Add appropriate pauses with punctuation
- Split long text into manageable chunks

### Audio Quality
- Use high-quality voice models
- Adjust speaking rate for clarity
- Test different voices for best results
- Consider background music mixing

### Performance
- Cache synthesized audio for repeated use
- Use streaming for long content
- Implement async processing for batch jobs
- Optimize file sizes with appropriate formats

## Example: Complete TTS Script

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gtts import gTTS
from pydub import AudioSegment
import os

class TextToSpeech:
    def __init__(self, language='en'):
        self.language = 'zh-CN' if language == 'zh' else 'en'
    
    def synthesize(self, text, output_file='output.mp3', slow=False):
        """Convert text to speech and save to file"""
        tts = gTTS(text=text, lang=self.language, slow=slow)
        tts.save(output_file)
        return output_file
    
    def play(self, audio_file):
        """Play audio file"""
        os.system(f'afplay {audio_file}')  # macOS
        # For Linux: os.system(f'mpg123 {audio_file}')
        # For Windows: os.system(f'start {audio_file}')

# Usage
tts = TextToSpeech(language='zh')
tts.synthesize("欢迎使用文字转语音功能！", output_file='welcome.mp3')
tts.play('welcome.mp3')
```

## Troubleshooting

### Common Issues

1. **No Chinese voice available**
   - Install espeak-ng with Chinese support
   - Use online TTS services (gTTS, Azure, OpenAI)

2. **Audio quality issues**
   - Try different voice models
   - Adjust speaking rate
   - Use higher quality TTS services

3. **Performance problems**
   - Use offline TTS for real-time needs
   - Cache synthesized audio
   - Implement async processing

## API Keys Required

- **Azure Cognitive Services**: Get from Azure Portal
- **OpenAI API**: Get from OpenAI Platform
- **Google Cloud TTS**: Optional, gTTS is free

## Resources

- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)
- [Google TTS API](https://cloud.google.com/text-to-speech)
- [Azure Speech Service](https://azure.microsoft.com/services/cognitive-services/speech-services/)
- [OpenAI TTS](https://platform.openai.com/docs/guides/text-to-speech)
