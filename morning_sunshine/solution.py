def morning_sunshine(numbers : list[int]):
    
    if numbers != []:
        Retour = [numbers[-1]]
        for i in range(2,len(numbers)+1):
            if numbers[-i] <= Retour[-1]:
                continue
            else:
                Retour.append(numbers[-i])
        Retour.reverse()
    else:
        Retour = []
    return Retour
