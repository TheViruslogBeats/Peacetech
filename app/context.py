import asyncpg

from app.utils import secrets


class AppContext:
    def __init__(self, *, secrets_dir: str):
        self.secrets: secrets.SecretsReader = secrets.SecretsReader(
            secrets_dir
        )

    async def on_startup(self, app=None):
        self.db = await asyncpg.create_pool(
            user='rizyfbtd',
            password='mtgn_9cgEWDalyPDg3ka4utR0TfVvRF2',
            host='mouse.db.elephantsql.com',
            database='rizyfbtd',
            port=5432,
            min_size=1,
            max_size=3
        )
    async def on_shutdown(self, app=None):
        if self.db:
            await self.db.close()
