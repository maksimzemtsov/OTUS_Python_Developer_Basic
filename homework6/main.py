from homework6.models import engine, Base
from homework6.jsonplaceholder_requests import fetch_users_data, fetch_posts_data, save_data
import asyncio


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )

    await save_data(users_data, posts_data)
    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
