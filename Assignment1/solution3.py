

def solution3(data: str):
    """
    Illustrate the design in step by step approach and write a program to simulate a solution3 
    which  accept  strings  that  start  and  end  with  same  character.  Analyze  the  output  with 
    different test cases.
    """
    # cState = 0
    # for _ in data:
    #     if cState == 0:
    #         cState = 1
    #     elif cState == 1:
    #         pass
    # return cState == 1
    try:
        if data[0]==data[-1]:
            return True
    except Exception:
        pass
    return False


print("Accepted? ", solution3(input("Enter the input: ")))