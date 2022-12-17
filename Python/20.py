# Find the sum of the digits in the number 100!
# Execution time: 0.214s

def equation(inputs):
    counter = 1
    for number in range(1, inputs + 1):
        counter *= number
    return counter


def sumOfEquation():
    indivNumbers = [int(i) for i in str(equation(100))]
    return sum(indivNumbers)


numSum = sumOfEquation()
print ("The sum of the digits in the number 100!", str(numSum))
