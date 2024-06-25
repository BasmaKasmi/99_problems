import solution

def tux_(numbers: list[int]):
    max=numbers[0]
    min=numbers[1]
    PivotOne = [0,max]
    ListPivot = [PivotOne]
    numbers.append(numbers[-1]+1)
    for i in range(1,len(numbers)-1):
        if numbers[i] >= max:
            ListPivot.append([i,numbers[i]])
            max = numbers[i] 
        if numbers[i] < min:
            min = numbers[i]
    print(min)
    if min < ListPivot[-1][1]:
        return ListPivot[-1][0]
    return -1
  
def tux__(numbers: list[int]):
    if numbers != []:
        numbers.insert(0,min(numbers)-1)
        numbers.append(max(numbers)+1)
        for i in range(1,len(numbers)-1):
            if numbers[i] > max(numbers[:i]) and numbers[i] <= min(numbers[i:]) :
                return i-1
    return -1
          
List = [98, 98, 97, 99, 99, 108, 101]

#solution.tux(List) 

print(solution.tux(List))