def playset(s: str) -> bool:
    length = len(s)

    if length <= 1:
        return False

    char_set = set()
    for char in s:
        if char in char_set:
            return True
        char_set.add(char)
    return False


