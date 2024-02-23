


def solution5():
    """
    Illustrate the design in step by step approach and write a program to simulate a DFSM 
    which  accept  the  language  having  all  'a'  before  all  'b'.  Analyze  the  output  with 
    different test cases.
    """
    pass

def dfsm(data: str):
    cState = 0
    for char in data:
        if char == 'a' and cState == 1:
            return False
        elif char == 'a':
            cState = 0
        elif char == 'b':
            cState = 1
        else:
            return False
    return True

print("Accepted? ", solution5(input("Enter the input: ")))