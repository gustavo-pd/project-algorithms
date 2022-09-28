def study_schedule(permanence_period, target_time):
    try:
        sum = 0
        for i, value in permanence_period:
            if target_time >= i and int(target_time) <= value:
                sum += 1
        return sum
    except TypeError:
        return None
