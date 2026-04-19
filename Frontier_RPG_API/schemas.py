from pydantic import BaseModel, ConfigDict

class CharacterCreate(BaseModel):
    name: str
    profession: str

class CharacterResponse(CharacterCreate):
    id: int
    level: int
    experience: int
    money: int
    energy: int
    strength: int

    model_config = ConfigDict(from_attributes=True)