#take input from users 
# answer = input("What is the Answer to the Gret question of life, the Universse and Everything? ")


#if users input 42 or (casea-insensitively)"forty-two" or "forty two " otherwise output No
#checking condition 

# if answer == "42":
#     print("yes")

# elif answer.lower().strip() == "forty-two":
#     print("yes")

# elif answer.lower().strip() == "forty two":
#     print("yes")

# else:
#     print("No")

good_answer = ["42","forty-two","forty two"]
answer = input("What is the Answer to the Gret question of life, the Universse and Everything? ").lower().strip()
if answer in good_answer:
    print("Yes")
else:
    print("No")        
        
