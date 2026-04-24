def Replace(data):

    output = ""
    
    for ch in data:
        if(ch == 'a'):
            output.append("_")
        else:
            output.append(ch)

    return output

def main():
    print("Enter String : ")
    str = input()

    strx = Replace(str)

    print(f"Updated string is {strx}")
        
if __name__ == "__main__":
    main()

# Error as append not allowed in python for string