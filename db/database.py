import aiosqlite

from config import DB_NAME


async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS quiz_state (
                user_id INTEGER PRIMARY KEY,
                question_index INTEGER DEFAULT 0,
                score INTEGER DEFAULT 0
            )
        """)
        await db.commit()


async def get_quiz_index(user_id: int) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
                "SELECT question_index FROM quiz_state WHERE user_id = ?",
                (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 0


async def get_score(user_id: int) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
                "SELECT score FROM quiz_state WHERE user_id = ?",
                (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 0


async def update_quiz_state(
        user_id: int,
        question_index: int | None = None,
        score: int | None = None
):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            INSERT INTO quiz_state (user_id, question_index, score)
            VALUES (
                ?,
                COALESCE(?, 0),
                COALESCE(?, 0)
            )
            ON CONFLICT(user_id) DO UPDATE SET
                question_index = COALESCE(excluded.question_index, quiz_state.question_index),
                score = COALESCE(excluded.score, quiz_state.score)
            """,
            (user_id, question_index, score)
        )
        await db.commit()


async def get_stats():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
                "SELECT user_id, score FROM quiz_state ORDER BY score DESC"
        ) as cursor:
            return await cursor.fetchall()
