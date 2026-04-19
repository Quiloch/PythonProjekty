from sqlalchemy.orm import Session
import models, schemas



def create_character(db: Session, character: schemas.CharacterCreate):
    db_character = models.Character(name=character.name, profession=character.profession)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character