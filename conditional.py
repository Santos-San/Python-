# == < > <= >= % ! is , not and or 
# 90 A, 80 90 B, 70 80 C, 60 70 D, 60 f
def main():
    mark = mark_float(input("what is your percentage? "))
    mark = mark_analyze(mark)
    print(mark)

def mark_analyze(mark):
    # if mark >= 90:
    #     return "you got  A"
    
    # elif mark >= 80:
    #     return "You got B"
    
    # elif mark >= 70 :
    #     return "you got c" 
    
    # elif mark >= 60 :
    #     return "you got D"   
    
    # return "failed"
    match mark :
        case 90:
            return "A"
        case 80:
            return "B"
        case 70:
            return "c"
        case 60:
            return "D"
        case _:
            return "F"

def mark_float(m):
    return float(m.replace("%",""))
    

main()


