import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_input):
    prompt = f"You are CompanionBot, a warm and kind friend who provides comfort but never gives medical advice.\n\nUser: {user_input}\nBot:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a supportive, empathetic chatbot friend."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )
    return response.choices[0].message['content']
