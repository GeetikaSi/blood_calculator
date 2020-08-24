def interface():
    print("My Program")
    while True:
        print("Options")
        print("1 - HDL")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    #Get input
    #Check if HDL is normal
    #Output
    input()
    HDL_process()
    
def input():
#input function returns a string
    HDL_input = input("Enter your HDL value: ")
    return int(HDL_input)

def HDL_process():
    if HDL_input >= 60:
        return("Normal")
    elif HDL_input >= 40 && HDL_input < 60:
        return("Borderline Low")
    elif HDL_input < 40:
        return("Low")
        
        
interface()

