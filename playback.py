def main():
    # take input from users 
    playback = input("Write something: ")

    #Replace space with 3 periods
    playback = play_back(playback)
    
    #print the updated text
    print(playback)

def play_back(text):
    return text.replace(" ","...")

main()