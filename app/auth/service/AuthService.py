import logging

from app.auth.model import SignupModel
from app.auth.repository.AuthRepository import signup


async def sign_up(payload: SignupModel):
    election_id = await signup(payload)
    # logger = logging.getLogger("api")
    # logger.setLevel(logging.DEBUG)
    print(election_id, payload)
    return {'id': election_id, 'basic_info': payload}
