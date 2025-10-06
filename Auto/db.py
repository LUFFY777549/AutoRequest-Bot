from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://sufyan532011:5042@auctionbot.5ms20.mongodb.net/?retryWrites=true&w=majority&appName=AuctionBot"
mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["AutoApprovalBot"]

users = db["users"]
approvals = db["approvals"]

async def add_user(user_id: int):
    await users.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

async def get_all_users():
    return [u["_id"] async for u in users.find({})]

async def set_approval(chat_id: int, status: bool):
    await approvals.update_one({"_id": chat_id}, {"$set": {"status": status}}, upsert=True)

async def get_approval(chat_id: int):
    data = await approvals.find_one({"_id": chat_id})
    return data["status"] if data else False