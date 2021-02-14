from fastapi import APIRouter

from app.auth.model.SignupModel import Signup, SignupResponse
from app.auth.service.AuthService import sign_up

auth = APIRouter(prefix='/auth', tags=['Auth'])


@auth.post('/signup', response_model=SignupResponse)
async def signup(payload: Signup):
    return await sign_up(payload)
