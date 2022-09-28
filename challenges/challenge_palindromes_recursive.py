def is_palindrome_recursive(word, low_index, high_index):

    if word[high_index] != word[low_index]:
        return False

    if not word:
        return False

    if high_index <= low_index:
        return True

    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
