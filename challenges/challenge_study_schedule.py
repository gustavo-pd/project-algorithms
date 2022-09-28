def study_schedule(permanence_period, target_time):
    try:
        for i, value in permanence_period:
            count = 0
            if target_time >= i and int(target_time) <= value:
                count += 1
        return count
    except TypeError:
        return None
