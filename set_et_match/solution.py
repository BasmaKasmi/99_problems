def set_et_match(numbers: list[int], n: int):
    max=len(numbers)-1
    if max<1:
        return False
    numbers.sort()
    for i in range(max):
        if numbers[i] + numbers[i+1] > n:
            if max == len(numbers)-1:
                max=i-1
            for y in range(max,-1,-1):
                if numbers[i+1] + numbers[y] < n:
                    break
                elif numbers[i+1] + numbers[y] == n:
                    return True
                elif numbers[i+1] + numbers[y] > n:
                    max = y - 1
        elif numbers[i] + numbers[i+1] == n:
            return True    

    return False
     