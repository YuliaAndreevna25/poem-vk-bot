from storage.db import get_user

def preferences_command(
    user_id,
    args,
    send_message
):

    user = get_user(user_id)

    style = user["style"]
    effort = user["effort"]

    send_message(
        user_id,
        f"""
        ⚙️ Ваши настройки

        🎭 Стиль: {style}
        ⚡ Усилия: {effort}/10
        """
    )