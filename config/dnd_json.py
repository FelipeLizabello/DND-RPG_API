import os
import json
from services.dnd_services import get_dnd_races

class DndRace:
    def __init__(self, json_filename="dnd_races.json"):
        self.json_path = os.path.join(os.path.dirname(__file__), json_filename)

    async def fetch_and_save(self):
        data = get_dnd_races()
        races = data.get("results", [])

        races_body = []
        for race in races:
            races_body.append({
                "index" : race.get("index"),
                "name"  : race.get("name")
            })

        return races_body
    
    async def select_races():
        
