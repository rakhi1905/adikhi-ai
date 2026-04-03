from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response.choices[0].message.content

        except Exception as e:
            print("ERROR:", e)
            reply = "⚠️ AI error"

        self.history.append({"role": "assistant", "content": reply})
        self.turn_count += 1

        return reply

    def reset(self):
        self.history = []
        self.turn_count = 0
        self.session_start = datetime.now()

    def stats(self):
        mins = (datetime.now() - self.session_start).seconds // 60
        return {
            "turns": self.turn_count,
            "messages": len(self.history),
            "duration_mins": mins
        }