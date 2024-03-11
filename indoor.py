def main():
    # take input from usr
    text = input("write something: ")
    # convert to lower
    text = to_lower(text)
    # print user input to lower
    print(text)


def to_lower(text):
    return text.lower()

main()




     