


def solution1(data: str):
    """
    Illustrate the design in step by step approach and write a program to simulate 
    deterministic finite state machine (DFSM) for accepting the language L = {anbm | n mod 
    2=0, m ≥1}. Analyze the output with different test cases.
    """
    cState = 0
    for char in data:
        if cState == 0 and char == 'a':
                cState = 1
        elif cState == 1:
            cState = 0 if char == 'a' else 2
        elif cState == 2 and char == 'a':
                cState = 3
        elif cState == 3 and char == 'a':
                cState = 2
    return cState == 2 or cState == 3

print("Accepted? ", solution1(input("Enter the input: ")))