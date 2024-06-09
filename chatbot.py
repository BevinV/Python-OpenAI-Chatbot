import os
import openai

openai.api_key = os.environ.get('OPENAI_API')


def chat_with_gpt(prompt):
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return respone.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
