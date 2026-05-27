from storage.db import upsert_user

def effort_command(
    user_id,
    args,
    send_message
):

    if not args:

        send_message(
            user_id,
            "Используйте: /effort 1-10"
        )

        return

    try:

        effort = int(args[0])

        effort = max(1, min(effort, 10))

        upsert_user(
            user_id,
            effort=effort
        )

        send_message(
            user_id,
            f"⚡ Усилия: {effort}/10"
        )

    except:

        send_message(
            user_id,
            "Значение усилия должно быть числом."
        )