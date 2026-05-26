from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)

db = client["FileSharingBot"]

admin_collection = db["admins"]


async def add_admin(user_id):
    user = await admin_collection.find_one({"user_id": user_id})

    if not user:
        await admin_collection.insert_one({"user_id": user_id})


async def remove_admin(user_id):
    await admin_collection.delete_one({"user_id": user_id})


async def get_admins():
    admins = []

    async for admin in admin_collection.find():
        admins.append(admin["user_id"])

    return admins
