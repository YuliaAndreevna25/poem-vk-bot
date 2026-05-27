def help_command(
    user_id,
    args,
    send_message
):

    send_message(
        user_id,
        """
        🎭 Команды:

        /style melancholic
        /style romantic
        /style cheerful

        /effort 1-10

        Просто напиши тему стихотворения.
        """
    )