


def solution4(data: str):
    """
    Illustrate the design in step by step approach and write a program to simulate a DFSM 
    which  accept  Binary  strings  that  starts  or  ends  with "01".  Analyze  the  output  with 
    different test cases.
    """
    cState = 0
    aChar = [0,0,2]
    bChar = [0,1,2]
    for char in data:
        if char == '0':
            cState = aChar[cState]
        elif char == '1':
            if cState in bChar:
                cState = 1
    return cState == 1 or cState == 2
    # return data[:2] == '01' or data[-2:] == '01'

print("Accepted? ", solution4(input("Enter the input: ")))
