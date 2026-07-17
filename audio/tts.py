# ==================================================
# IMPORTS
# ==================================================

import win32com.client

# ==================================================
# CLASS INIT
# ==================================================

class TTS:
    # * CONSTRUCTOR
    def __init__(self):
        '''
        Setups a text-to-speech engine.
        '''

        self.engine = win32com.client
        self.speaker = self.engine.Dispatch('SAPI.SpVoice')

    # * FUNCTION TO GET AVAILABLE VOICES
    def get_voices(self):
        '''
        Returns a list of all available voices
        '''

        return self.speaker.GetVoices()
    
    # * FUNCTION TO PRINT AVAILABLE VOICES
    def print_voices(self):
        '''
        Prints all available voices in a proper format.
        '''

        voices = self.get_voices()
        for i in range(voices.Count):
            print(f"Index {i}: {voices.Item(i).GetAttribute('Name')}")

    # * FUNCTION TO SET A VOICE FOR THE TTS ENGINE
    def set_voice(self, voice_index: int = 0):
        '''
        Set a voice to the engine.

        :param voice_index: The voice to set.
        '''

        voices = self.get_voices()
        self.speaker.Voice = voices.Item(voice_index)


    # * FUNCTION TO SPEAK TEXT
    def speak(self, text: str):
        '''
        Speaks the given text.

        :param text: The text to speak.
        '''

        self.speaker.Speak(text)