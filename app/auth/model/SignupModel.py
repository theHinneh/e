from pydantic import BaseModel


class SignupModel(BaseModel):
    org_name: str
    telephone: str
    email: str
    country: str


class Signup(BaseModel):
    org_name: str
    telephone: str
    email: str
    country: str


class SignupResponse(BaseModel):
    id: int
    basic_info: dict = {
        'org_name': '',
        'telephone': '',
        'email': '',
        'country': ''
    }
