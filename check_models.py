import google.generativeai as genai

genai.configure(api_key="AIzaSyAi9RfXzqoJoCci6zmqoiyfSeE1ASpKRvw")

models = genai.list_models()

for m in models:
    print(m.name)
