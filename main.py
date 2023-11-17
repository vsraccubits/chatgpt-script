from chatgpt import chat_gpt
from config.logger import logger

prompt = """"
Generate an example JSON.
"""
logger.info("Prompt------------------------------------")
logger.info(prompt)
logger.info("------------------------------------------")

response = chat_gpt.generate_json_response(prompt)
logger.info("Response----------------------------------")
logger.info(response)
logger.info("------------------------------------------")
