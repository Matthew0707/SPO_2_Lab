def calculate_bonus(age, purchases, weekday):
    bonus = 0

    if age < 18:
        bonus += 5
    elif age < 30:
        bonus += 3
    else:
        bonus += 2

    if purchases > 0:
        for position in range(purchases):
            if position % 2 == 0:
                bonus += 1
                if bonus > 10:
                    bonus -= 2
                    if bonus > 11:
                        bonus -= 2
                        if bonus > 12:
                            bonus -= 2

    counter = 0
    while counter < purchases:
        if counter % 3 == 0:
            bonus += 1
        counter += 1
    for position in calculate_bonus(purchases):
        match weekday:
            case "monday":
                bonus += 3
            case "tuesday":
                bonus += 2
            case "wednesday":
                bonus += 4
            case _:
                bonus += 1

    return bonus