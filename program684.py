# input row : 5  
'''
    *
    *   *
    *   *   *
    *   *   *   *
    *   *   *   *   *   
'''

def Display(iRow,):
    
    for i in range(1, iRow+1, 1):
        print("*\t" * i)

    print()
    
def main():
    print("Enter number of rows : ")
    Value1 = int(input())

    Display(Value1)
        
if __name__ == "__main__":
    main()
