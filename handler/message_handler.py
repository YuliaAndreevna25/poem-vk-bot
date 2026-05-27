from storage.db import get_user
from storage.db import upsert_user

from ai.yandex_gpt import generate_poem

from .command_handler import handle_command

BUTTON_MAPPINGS = {
    "🌧️ Меланхоличный": "/style melancholic",

    "❤️ Романтичный": "/style romantic",

    "☀️ Жизнерадостный": "/style cheerful",
    
    "⚙️ Мои настройки": "/preferences",

    "❓ Помощь": "/help",

    "🔄 Сброс": "/reset",
}

def handle_message(
    event,
    send_message,
    vk
):

    user_id = event.user_id

    text = event.text.strip()

    vk.messages.setActivity(
        user_id=user_id,
        type="typing"
    )

    if text in BUTTON_MAPPINGS:
        text = BUTTON_MAPPINGS[text]

    if text == "⚡ + Усилия":

        user = get_user(user_id)

        effort = min(
            user["effort"] + 1,
            10
        )

        upsert_user(
            user_id,
            effort=effort
        )

        send_message(
            user_id,
            f"⚡ Усилия: {effort}/10"
        )

        return

    if text == "💤 - Усилия":

        user = get_user(user_id)

        effort = max(
            user["effort"] - 1,
            1
        )

        upsert_user(
            user_id,
            effort=effort
        )

        send_message(
            user_id,
            f"💤 Усилия: {effort}/10"
        )

        return

    if text.startswith("/"):

        handle_command(
            user_id,
            text,
            send_message
        )

        return

    try:
        user = get_user(user_id)
    except Exception as e:
        send_message(user_id, f"Ошибка: {e}")
        return
    

    poem = generate_poem(
        prompt=text,
        style=user["style"],
        effort=user["effort"]
    )

    send_message(
        user_id,
        poem
    )