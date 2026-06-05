import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Chatbot:
    
    def __init__(self, persona_desc, model):
        self.model = model
        self.persona_desc = persona_desc
        self.client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
        )
        self.messages = [{"role": "system", "content": self.persona_desc}]
        
    def call_model(self, prompt:str) -> str:
        self.messages.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
        model= self.model,
        messages= self.messages
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

def run_chatbot(chatbot_object, N):
    print("Chat started. Type 'exit' to quit.\n")

    while True:
        user_input = input("[YOU] ")
        if user_input == "exit":
            print("Goodbye!")
            break
        else:
            response = chatbot_object.call_model(user_input)
            print("[MODEL] ", response)
            while len(chatbot_object.messages) > 2*N + 1:
                del chatbot_object.messages[1]
                del chatbot_object.messages[1]

if __name__ == "__main__":
    model = input("What model you will prefer?")
    if model == '':
        model = "openrouter/free" 
    persona_input = input("Describe the persona of the agent: ")
    chatbot = Chatbot(persona_input,model)
    run_chatbot(chatbot, 100)


