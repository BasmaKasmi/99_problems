def tux(numbers: list[int]):
    Dict = {}
    max = -1
    for i in range(len(numbers)):
        Dict[i] = numbers[i]
    Sorted = sorted(Dict.items(), key= lambda t:t[1])
    for i in range(len(numbers)):
        if i == Sorted[i][0]:
            if i > max:
                return i
        if Sorted[i][0] > max:
            max = Sorted[i][0]
    return -1

