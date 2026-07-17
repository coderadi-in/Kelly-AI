# ==================================================
# IMPORTS
# ==================================================

from agents.chat_agent import generate_response
from agents.desk_agent import DeskAgent
from agents.system_prompt import PROMPT
from audio.stt import STT
from audio.tts import TTS
from dotenv import load_dotenv
import os, json

# ==================================================
# LOAD ENVIRONMENT VARIABLES
# ==================================================

load_dotenv(".venv/vars.env")

# ==================================================
# SETUP
# ==================================================

stt = STT()
tts = TTS()
desk_agent = DeskAgent()
tts.set_voice(1)

# ==================================================
# BASIC CHATTING
# ==================================================

print("Kelly AI.")
print("Press ctrl + c to exit.\n")
while (True):

    try:
        # 1. Listen for user input
        print("Speak...")
        audio = stt.listen()
        transcription = stt.transcribe(audio)
        print("You: " + transcription)

        # # 1. Listen for user input
        # text = input("You: ")

        # 2. Generate AI response
        response = generate_response(PROMPT, transcription)
        output = response['output']

        # 3. Check for any task and give the output
        try:
            command = json.loads(output)
            if (isinstance(command, dict)):
                print("Kelly: " + command['message'])
                tts.speak(command['message'])
                
                desk_agent.execute_task(
                    command['action'],
                    command['data']
                )

        except json.JSONDecodeError:
            print("Kelly: " + response['output'])
            tts.speak(response['output'])    

    except KeyboardInterrupt:
        print("\n\nStream exited by user.\n")
        exit()