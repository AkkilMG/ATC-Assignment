

def solution2(data):
    """
    Illustrate the design in step by step approach and write a program to simulate a dfsm
    which accept the language L = {w | w ∈ {a, b}* and Na (w) mod 3 = Nb (w) mod 3}. 
    Analyze the output with different test cases
    """
    cState = 0
    aChar = [1,2,0]
    bChar = [0,1,2]
    for char in data:
        if char == 'a':
            try:
                cState = aChar[cState]
            except Exception:
                pass
        elif char == 'b':
            try:
                cState = bChar[cState]
            except Exception:
                pass
    return cState == 0
    # return data.count('a') == data.count('b')


print("Accepted? ", solution2(input("Enter the input: ")))
