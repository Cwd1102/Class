if __name__ == '__main__':

    toppings = ["caramel","marshmallow","gummi bears"]

    ice_cream_flavors = ["vanilla","strawberry","chocolate"]

    for i in range(len(ice_cream_flavors)):
        if(i != 1): 
            for x in range(len(toppings)):
                print(ice_cream_flavors[i], "is great with" , toppings[x])
        else:
            print("Strawberry is fine on its own")