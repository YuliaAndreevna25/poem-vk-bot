from storage.db import upsert_user

def reset_command(
    user_id,
    args,
    send_message
):

    upsert_user(
        user_id,
        style="classic",
        effort=5
    )

    send_message(
        user_id,
        "Настройки сброшены."
    )