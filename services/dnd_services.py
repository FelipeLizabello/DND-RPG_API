from repository.dnd_repo import get_dnd_races

class DndRace:

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
    
    async def fetch_race_by_id(self, race_id: str):
        data = get_dnd_races()
        races = data.get("results", [])

        for race in races:
            if race.get("index") == race_id:
                return {
                    "index" : race.get("index"),
                    "name"  : race.get("name")
                }
            
        return {"error" : "Race not found"}