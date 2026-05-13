from fastapi import APIRouter
from services.dnd_services import DndRace

router = APIRouter()

@router.get("/dnd/races")
async def get_races():
    dnd_races = DndRace()
    races = await dnd_races.fetch_and_save()
    return races

@router.get("/dnd/races/{race_id}")
async def get_races_id(race_id : str):
    dnd_races = DndRace()
    race = await dnd_races.fetch_race_by_id(race_id)
    return race
    