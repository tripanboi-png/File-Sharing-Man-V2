from database.mongo import get_admins


async def is_admin(_, __, message):

    admins = await get_admins()

    return message.from_user.id in admins
