def roger_rabbit(n: int) -> list[str]:
    binary_representations = []
    
    def to_binary(number):
        if number == 0:
            return '0'
        elif number == 1:
            return '1'
        else:
            return to_binary(number // 2) + str(number % 2)

    for i in range(1, n + 1):
        binary_representations.append(to_binary(i))
    
    return binary_representations


