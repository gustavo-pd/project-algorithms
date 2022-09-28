def is_anagram(first_string, second_string):
    f_string_list = list(first_string.lower())
    s_string_list = list(second_string.lower())

    for string in f_string_list:
        if string in s_string_list:
            s_string_list.remove(string)
        else:
            return False
    if len(s_string_list) != 0:
        return False
    else:
        return True