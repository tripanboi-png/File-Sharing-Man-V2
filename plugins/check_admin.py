from database.mongo import get_admins


async def is_admin(_, __, message):

    admins = await get_admins()

    admin_ids = [int(x["id"]) for x in admins]

    return message.from_user.id in admin_ids
