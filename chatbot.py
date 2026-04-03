from groq import Groq
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
print("API KEY:", api_key)

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """You are Adikhi AI, an elite business intelligence assistant.

Give clear, practical, and structured business advice.
Use bullet points where helpful.
Be professional and direct.
"""

class AdikhiChatbot:
    def __init__(self):
        self.history = []
        self.turn_count = 0
        self.session_start = datetime.now()

    def chat(self, user_message: str) -> str:
        try:
            messages = [{"role": "system", "content": SYSTEM_PROMPT}] + self.history + [
                {"role": "user", "content": user_message}
            ]

            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=messages
            )

            reply = completion.choices[0].message.content

        except Exception as e:
            print("ERROR:", e)
            reply = "⚠️ AI error"

        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": reply})
        self.turn_count += 1

        return reply
    