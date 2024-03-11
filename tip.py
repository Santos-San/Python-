def main():
    #takes input from users 
    dollars = dollars_to_float(input("how much was the meal? "))
    percent = percent_to_float(input("what percentage would you like to tip? "))
    
    #tip calculator 
    tip = dollars * percent
    
    #print output 
    print(f"leave ${tip:.2f}")

#creating functions for dollar and percentage 
def dollars_to_float(d):
    # without_dollar = d.replace("$","")
    to_float = float(d.replace("$",""))
    return to_float

def percent_to_float(p):
    without_percent = p.replace("%","")
    percent_float = float(without_percent) / 100
    return percent_float

main()

