import os
from dotenv import load_dotenv
import openai
from openai import AzureOpenAI

load_dotenv(override=True)

open_ai_embedding_endpoint = "https://ai-odluser1305754ai648764271118.openai.azure.com/"
open_ai_embedding_key = "86aad2d5149a4fe5990230c1fd64d6fd"
open_ai_embedding_deployment_name = "text-embedding-ada-002"

open_ai_endpoint = "https://ai-odluser1305754ai648764271118.openai.azure.com/"
open_ai_key = "86aad2d5149a4fe5990230c1fd64d6fd"
open_ai_deployment_name = "gpt-35-turbo"

api_version = "2024-02-15-preview"


def create_openai_client() -> AzureOpenAI:
    return AzureOpenAI(
        api_key=open_ai_key,  # key
        azure_endpoint=open_ai_endpoint,  # gpt4
        api_version=api_version,  # ver
    )


client = create_openai_client()


def get_embeddings(text: str) -> str:
    embedding_client = openai.AzureOpenAI(
        api_key=open_ai_embedding_key,
        azure_endpoint=open_ai_embedding_endpoint,
        api_version=api_version,
    )
    depl_model = open_ai_embedding_deployment_name
    embedding = embedding_client.embeddings.create(input=[text], model=depl_model)
    return embedding.data[0].embedding


def get_ai_resp(query: str, system_content: str) -> str:
    try:
        message_text = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": query},
        ]
        completion = client.chat.completions.create(
            model=open_ai_deployment_name,
            messages=message_text,
            temperature=0.6,
            max_tokens=200,
            top_p=0.95,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            # response_format={"type": "json_object"},
            stop=None,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(e)
        return "Sorry, I am unable to provide an answer at this time."
