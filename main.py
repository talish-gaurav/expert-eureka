
bc = input("Is your vechile a bike or car? Only write bike or car in lower case ")

if bc == "bike":

    b= input("Is it used for work or for fun. Only type the word fun or work in this same format")

    if b == "work":

        print("It is either a city, hybrid or folding bike")

    elif b == "fun":

        print("It is a offroad cycle or hybrid")

    else:

        print("Invalid input! Read instructions again")

elif bc == "car":

    b= input("Is it diesel or electric? Type the word diesel or electric in the same format")

    if b == "diesel":

        print("Your car has better fuel efficiency")

    elif b == "electric":

        print("Your car causes less pollution to the environment")

    else:

        print("Invalid input! Read instructions again")

else:

    print("Invalid input!")