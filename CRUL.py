def minChairs(simulations):
    chairs = []
    for s in simulations:
        available = 0
        min_chairs = 0
        for j in s:
            if j == 'C':
                if available == 0:
                    min_chairs = min_chairs+1
                elif available > 0:
                    available -= 1


            elif j == 'R':
                available += 1
            elif j == 'U':
                if available == 0:
                    min_chairs += 1  # Increment min_chairs only if no available chairs
                else:
                    available -= 1
            elif j == 'L':
                available +=1
                min_chairs = max(min_chairs, available)
        chairs.append(min_chairs)
    return chairs


simulations = []
numb = int(input("Enter number of elements: "))
i = 1
while i <= numb:
    simulations.append((input("Enter the elements: ")))
    i = i + 1

result = minChairs(simulations)
print(result)
