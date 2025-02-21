def listFunc(a, b):
    return [i for i in range(a, b)] #Create list of ints from 1 to 5, Haskell equivalent [1..5]

def applicatorFunc(inpFunc, s):
    if s=='s':
        return sum(inpFunc)
    else:
        return sum(inpFunc)/len(inpFunc)

print(applicatorFunc(listFunc(1, 7), 's'))