'''
Generates response of user's prompt.
'''

# ==================================================
# IMPORTS
# ==================================================

import logging
import os
from openai import OpenAI

# ==================================================
# SETUP
# ==================================================

logging.basicConfig(level=logging.ERROR)

# ==================================================
# GENERATE RESPONSE FUNCTION
# ==================================================

# * FUNCTION TO SEND MESSAGE TO MODEL
def generate_response(system_prompt: str, message: str, token_size: int = 250) -> dict:
    """
    Generates a response using AI model.

    :param system_prompt: The prompt to be provided by the system.
    :param message: The prompt to be provided by the user.
    :param token_size: The max token size to generate response.

    ## Usage
    ```python
        response = get_response(
            "You're a professional story-teller.",
            "Create a small 100 words story for a tech-product."
        )
    ```
    """

    api_key = os.getenv("OPENROUTER_API")
    if not (api_key):
        return {
            "output": "There're issues in the backend!",
            "status": 503
        }

    try:
        model = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

        response = model.responses.create(
            model="openai/gpt-4o-mini",
            input=[
                { "role": "system", "content": system_prompt },
                { "role": "user", "content": message },
            ],
            temperature=0.7,
            max_output_tokens=token_size,
        )

        return {
            "output": response.output_text,
            "status": 200
        }

    except Exception as e:
        logging.error(str(e))
        return {
            "output": "Something went wrong while generating response!",
            "status": 500
        }