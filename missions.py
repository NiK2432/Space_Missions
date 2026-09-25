SPACE_MISSIONS = [
    {
        "name": "Mars 2020",
        "year": 2020,
        "direction": "Марс",
    },
    {
        "name": "Artemis I",
        "year": 2022,
        "direction": "Луна",
    },
    {
        "name": "Voyager 1",
        "year": 1977,
        "direction": "Дальний космос",
    },
    {
        "name": "Chandrayaan-3",
        "year": 2023,
        "direction": "Луна",
    }
]

def display_missions(missions_list):
    print("\n=== Каталог космических миссий ===\n")
    for i, mission in enumerate(missions_list):
        print(f"{i + 1}. {mission['name']}")
        print(f"  Год запуска: {mission['year']}")
        print(f"  Направление: {mission['direction']}\n")
def find_missions_by_direction(missions_list, direction):
    found_missions = []
    for mission in missions_list:
        if mission["direction"].lower() == direction.lower():
            found_missions.append(mission)
    return found_missions