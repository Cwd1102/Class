if __name__ == '__main__':
    string = input("Enter a string:")
    string = string.split()
    string = "".join(string)
    string = string.lower()
    new_string = []
    
    for i in range(len(string )):
        new_string = []
        for x in range(len(string)):
            new_string.append(string[(-1 * i) + x])
            temp_string = "".join(new_string)
            if temp_string == string and i != 0:
                print(f"{string} is a rotation with offset {i}")

            