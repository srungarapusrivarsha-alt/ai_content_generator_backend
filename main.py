from fastapi import FastAPI
from groq import Groq
from openai import OpenAI
import os
app=FastAPI()
client=OpenAI(
    api_key=os.getenv("groq_key_url"),
    base_url="https://api.groq.com/openai/v1")

@app.post("/generate")
def generate_content(
    topic:str,
    technology:str,
    content_type:str,
    tone:str
  ):
    prompt=f"Generate a content type of {content_type} and topic is {topic} in technology {technology} in tone of {tone}"
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return {
        "content":response.choices[0].message.content
    }
