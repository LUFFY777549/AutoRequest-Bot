import aiosqlite

DB_NAME = "auto_approval_bot.db"

# ------------------ Setup tables ------------------
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS approvals (
                chat_id INTEGER PRIMARY KEY,
                status INTEGER
            )
        """)
        await db.commit()

# ------------------ Users ------------------
async def add_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,)
        )
        await db.commit()

async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT user_id FROM users")
        rows = await cursor.fetchall()
        return [row[0] for row in rows]

# ------------------ Approvals ------------------
async def set_approval(chat_id: int, status: bool):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO approvals (chat_id, status) VALUES (?, ?) "
            "ON CONFLICT(chat_id) DO UPDATE SET status=excluded.status",
            (chat_id, int(status))
        )
        await db.commit()

async def get_approval(chat_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT status FROM approvals WHERE chat_id = ?", (chat_id,))
        row = await cursor.fetchone()
        return bool(row[0]) if row else False