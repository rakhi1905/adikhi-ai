from groq import Groq
import os
from dotenv import load_dotenv
from datetime import datetime

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in environment")

print("API KEY LOADED:", api_key[:10])  # safe print

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
    model="mixtral-8x7b-32768",
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
    