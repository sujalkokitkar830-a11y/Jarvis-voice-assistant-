# from openai import OpenAI
# import os

# # client = OpenAI()

# # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # if you saved the key under a different environment variable name, you
# # can do something like:
# client = OpenAI(api_key=
#     "api_key",
# ) 

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
#         {"role": "user", "content": "what is coding."}
#     ]
# )

# print(completion.choices[0].message.content)



# # this is a paid service so cannot work 


from groq import Groq
try:
    client = Groq(api_key="api_key")  # paste your key here for local testing

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # free, fast, good quality
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
            {"role": "user", "content": "what is coding tell this in short ."}
        ]
    )

    print(completion.choices[0].message.content)

except Exception as e:
    print(e)