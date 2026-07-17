'''
stt: Manages the STT class.
'''

# ==================================================
# IMPORTS
# ==================================================

import speech_recognition as sr

# ==================================================
# CLASS INIT
# ==================================================

class STT:
    # * CONSTRUCTOR
    def __init__(self):
        '''
        Setups a listening setup.
        '''

        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True

    # * FUNCTION TO LISTEN FOR USER INPUT
    def listen(self) -> sr.AudioData:
        '''
        Listens for user input and returns the audio data.
        '''

        with sr.Microphone() as source:
            print(self.recognizer.energy_threshold)
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        return audio
    
    # * FUNCTION TO TRANSCRIBE AUDIO BUFFER
    def transcribe(self, audio: sr.AudioData):
        '''
        Transcribes the audio data and returns the transcription.
        '''

        print("Transcribing...")
        transcription = self.recognizer.recognize_whisper(audio)
        return transcription