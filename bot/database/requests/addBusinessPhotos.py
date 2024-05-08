from bot.database import async_session
from bot.database.models import BusinessMessage, UploadFiles

from sqlalchemy import insert


async def add_business_photos(business_message: dict, filenames: list) -> None:
    async with async_session() as session:
        msg = await session.execute(insert(BusinessMessage).values(**business_message))
        for filename in filenames:
            await session.execute(
                insert(UploadFiles).values(
                    file_id=filename, business_message_id=msg.inserted_primary_key[0]
                )
            )

        await session.commit()
