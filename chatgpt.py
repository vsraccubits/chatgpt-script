import json
from typing import Dict, List, Union

from openai import OpenAI

from config import settings
from config.logger import logger


class ChatGPT:
    """ChatGPT 3.5 Turbo Language Model"""

    def __init__(self) -> None:
        """Initialize ChatGPT 3.5 Turbo Language Model

        Configure OpenAI with API key
        """
        self.api_key = settings.OPENAI_API_KEY
        self.client = OpenAI(api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        """Generate a response from the prompt

        Args:
            prompt: Prompt to generate response from

        Returns:
            Generated response
        """
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        response = chat_completion.choices[0].message.content
        return response

    def generate_json_response(self, prompt: str) -> Union[Dict, List]:
        """Generate a JSON response from the prompt

        Args:
            prompt: Prompt to generate response from

        Returns:
            Generated response as JSON
        """
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        response = chat_completion.choices[0].message.content

        # retry if response is not valid JSON, set retry to True
        retry = True

        # retry until response is valid JSON
        while retry:
            try:
                response = json.loads(response)
                retry = False
            except json.JSONDecodeError:
                logger.error(
                    "Obtained invalid JSON response from GPT-3.5 Turbo Retrying..."
                )
                # write response to a JSON file for debugging
                with open("generated_response.json", "w") as f:
                    f.write(response)
                self.generate_json_response(prompt)
            except Exception as e:
                logger.error(
                    f"Error occurred while parsing JSON response from GPT {e} Retrying..."
                )
                self.generate_json_response(prompt)

        return response


# initialize chat gpt
chat_gpt = ChatGPT()
