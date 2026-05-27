import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YANDEX_API_SECRET_KEY")
FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"


STYLE_PROMPTS = {
    "classic": "Классическая поэзия.",

    "melancholic": """
    Мрачная, меланхоличная,
    декадентская поэзия.
    """,

    "romantic": """
    Романтичная,
    нежная,
    лиричная поэзия.
    """,

    "cheerful": """
    жизнерадотсный, веселый.
    """
}


def generate_poem(
    prompt: str,
    style: str = "classic",
    effort: int = 5
):

    effort = max(1, min(effort, 10))

    temperature = 0.3 + (effort * 0.07)
    max_tokens = 120 + (effort * 60)

    style_prompt = STYLE_PROMPTS.get(
        style,
        STYLE_PROMPTS["classic"]
    )

    system_prompt = f"""
        Ты талантливый поэт.

        Стиль:
        {style_prompt}

        Уровень вдохновения:
        {effort}/10

        Пиши только стихотворение.
        Без пояснений.
        Без вступлений.
        """

    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite/latest",

        "completionOptions": {
            "stream": False,
            "temperature": temperature,
            "maxTokens": max_tokens
        },

        "messages": [
            {
                "role": "system",
                "text": system_prompt
            },

            {
                "role": "user",
                "text": prompt
            }
        ]
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        return result["result"]["alternatives"][0]["message"]["text"]

    except Exception as e:

        return f"Ошибка генерации: {e}"