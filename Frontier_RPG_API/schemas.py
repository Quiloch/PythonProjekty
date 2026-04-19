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
    items: list['ItemResponse'] = []

class ItemBase(BaseModel):
    name: str
    description: str
    value: int
    strength_bonus: int

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    character_id: int

    model_config = ConfigDict(from_attributes=True)