# WEEK 1 SUBMISSION: Multi Turn Chatbot

I created a chatbot which can hold conversation using a stateless reponse API and openai SDK using a message buffer.

## Key features:
### 1. API Hygeine:
Instead of writing the API key, I saved it as an environment variable in a (.venv) file which I have mentioned in .gitignore to avoid any key leak. Then I load the API key using `python-dotenv` library.

### 2. Architecture/ Design of the code:
I wrapped the core logic (the `call_model` method) including the message buffer updation logic inside the ChatAgent class.
It allows two things:
* Every class instance has its own corresponsing `self.messages` making it store its conversation context history.
* The `run_chatbot` method handles the input and output of each chatbot instance independently.

### 3. Memory Management/ Buffer:
For each instance there is a message list storing its conversation history. The list consists dictionaries, with index = 0 having a system message while rest being alternating `user` and `assistant` messages.
   
> *I got the idea of this alternating format from the openAI docs which described the api understood the history in this manner.
   
Also the buffer has a limit (`N`) of maximum turns which can be customized in the run_chatbot method as an argument.
The while loop in removes the first turn when the length exceeds (`2*N+1`) by removing the index = 1 element twice(the index =2 element becomes index =1 after deleting index = 1). 

### 4. Customization (Model Agnosticism + Persona):
The chatbot instance is customizable. The user can select the model of their choice with default being ("openrouter/free"). The user can also set the persona (eg: *"Strict History Teacher"* ) of the bot which gets passed as a system message.

### 5.Response analysis
I understood the structure of the response I got from executing `build1.py`. I found it had a `choices` list in the output containg possible answers to the query. Each answer was an instance of `Choice class` with `role` and `content` mentioned.