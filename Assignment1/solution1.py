


def solution1(data: str):
    """
    Illustrate the design in step by step approach and write a program to simulate 
    deterministic finite state machine (DFSM) for accepting the language L = {anbm | n mod 
    2=0, m ≥1}. Analyze the output with different test cases.
    """
    cState, aCount, bCount = 0, 0, 0
    for char in data:
        if char == 'a' and cState == 1:
            return False
        elif char == 'a':
            cState = 0
            aCount += 1
        elif char == 'b':
            cState = 1
            bCount += 1
        else:
            return False
    return aCount%2 == 0 and bCount >= 1

print("Accepted? ", solution1(input("Enter the input: ")))

