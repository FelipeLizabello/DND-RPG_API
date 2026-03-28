from fastapi import APIRouter
from config.dnd_json import DndRace

router = APIRouter()

@router.get("/dnd/races")
async def get_races():
    dnd_races = DndRace()
    races = await dnd_races.fetch_and_save()
    return races

@router.get("dnd/races/{race_id}")
async def set_races(race_id : str):
    return {"race_id": race_id}
    