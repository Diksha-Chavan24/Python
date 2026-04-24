def Replace(data):

    output = ""
    
    for ch in data:
        if(ch == 'a'):
            output = output + '_'
        else:
            output = output + ch

    return output

def main():
    print("Enter String : ")
    str = input()

    strx = Replace(str)

    print(f"Updated string is {strx}")
        
if __name__ == "__main__":
    main()
