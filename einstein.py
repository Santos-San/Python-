def main():
    #take input of mass in kg
    mass = int(input("what is mass "))
    
    #Using einstein formula
    print(convert(mass))
    
def convert(mass, c=300000000):
    return mass*(c*c)
    

main()    