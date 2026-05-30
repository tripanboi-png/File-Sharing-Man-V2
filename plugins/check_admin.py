from database.mongo import get_admins

async def is_admin(_, __, message):
    user = getattr(message, "from_user", None)

    if user is None:
        return False

    admins = await get_admins()
    return user.id in admins
