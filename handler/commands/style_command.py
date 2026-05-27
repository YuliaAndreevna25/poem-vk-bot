from storage.db import upsert_user

def style_command(
    user_id,
    args,
    send_message
):

    if not args:

        send_message(
            user_id,
            "Используйте: /style "
        )

        return

    style = args[0]

    upsert_user(
        user_id,
        style=style
    )

    send_message(
        user_id,
        f"🎭 Стиль: {style}"
    )