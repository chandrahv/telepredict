import logging
import os

from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

open_ai_endpoint = 
open_ai_key = 
open_ai_deployment_name = 
api_version = 

client = AzureOpenAI(api_key=open_ai_key, azure_endpoint=open_ai_endpoint, api_version=api_version)


def configure_logger() -> None:
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)
