
def individual_race(race) -> dict:
    return{
        "id"            : str(race["_id"]),
        "name"          : race["name"],
        "ability_score" : race["ability_score"],
        "size"          : race["size"],
        "proficiency"   : race["proficiency"],
        "advantage"     : race["advantage"],
        "languages"     : race["languages"],
    }

def list_race(races) -> list:
    return[individual_race(race) for race in races]