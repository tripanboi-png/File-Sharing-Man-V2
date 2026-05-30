from database.mongo import get_admins

async def is_admin(_, __, message):

    if not message.from_user:
        return False

    admins = await get_admins()

    print("USER ID:", message.from_user.id)
    print("ADMINS :", admins)

    return message.from_user.id in admins
