from bunny.Database import db

db = db.details

async def save_details(details):
    x = await db.find_one({"self": "self"})
    if x:
        await db.delete_one({"self": "self"})
    await db.update_one({"self": "self"}, {"$set": {"details": details}}, upsert=True)

async def get_details():
    x = await db.find_one({"self": "self"})
    if x:
        return x["details"]

async def details_exist():
    x = await db.find_one({"self": "self"})
    if x:
        return True
    return False
