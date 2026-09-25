from missions import SPACE_MISSIONS, display_missions, find_missions_by_direction

if __name__ == "__main__":
    display_missions(SPACE_MISSIONS)

    search_direction = input("Введите направление для поиска: ")

    found = find_missions_by_direction(SPACE_MISSIONS, search_direction)

    print("\n=== Результаты поиска ===\n")
    if found:
        display_missions(found)
    else:
        print(f"Миссий по направлению '{search_direction}' не найдено.")