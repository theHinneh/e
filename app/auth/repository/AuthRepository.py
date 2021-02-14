from app.auth.model import SignupModel
from app.db.db import elections_platform, database


async def signup(payload: SignupModel):
    query = elections_platform.insert().values(**payload.dict())
    return await database.execute(query=query)
