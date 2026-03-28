from pydantic import BaseModel

class Race(BaseModel):
    name : str
    ability_score: dict[str, int]
    size: int
    proficiency: dict[str, int]
    advantage: dict[str, int]
    languages: list[str]


