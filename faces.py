def main(): 
    #take input from users 
    text = input("Write something ")

    #convert to emoji
    text = convert(text)

    #print the output
    print(text)

#Making convert function 
def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")

main()    
