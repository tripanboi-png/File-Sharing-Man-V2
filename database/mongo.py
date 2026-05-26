from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)

db = mongo_client["chindo_bot"]

admins_col = db.admins
buttons_col = db.buttons
users_col = db.users
settings_col = db.settings
