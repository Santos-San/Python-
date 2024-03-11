#making do while loop 
while True:
    try:
        positive_integer = int(input("what is numbers? "))
    except ValueError:
        print("Only Number!!!")
    else:
        if positive_integer >=5 and positive_integer <=8: 

            break
print(positive_integer)