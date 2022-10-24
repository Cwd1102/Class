if __name__ == '__main__':

    first_name = str(input("First name"))
    last_name = str(input("Last name"))

    first_name = first_name.swapcase()
    last_name = last_name.lower()
    print(first_name[0] + last_name)
