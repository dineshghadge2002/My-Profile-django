
from mistralai import Mistral

def chat1(user_input):

    api_key = 'your_api_key'
    model = "mistral-large-latest"
    client = Mistral(api_key = api_key)
    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": user_input,

            },
        ]
    )
    
    return chat_response.choices[0].message.content