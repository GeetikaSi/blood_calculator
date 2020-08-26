def interface():
    print("My Program")
    while True:
        print("Options")
        print("Enter '1' to check LDL value")
        print("Enter '9' to Quit")
        choice = input("Enter your choice ")
        if choice == '9':
            return
        elif choice == '1':
            LDL_driver()


def LDL_driver():
    #Get input
    #Check if LDL is normal
    #Output
    LDL_value = input_LDL()
    LDL_analysis = LDL_process(LDL_value)
    output_LDL(LDL_value, LDL_analysis)
     
def input_LDL():
#input function returns a string
    LDL_input = input("Enter your LDL value: ")
    return int(LDL_input)

def LDL_process(LDL_input): 
    if LDL_input >= 190:
        return "Very high"
    elif 160 <= LDL_input <= 189:
        return "High"
    elif 130 <= LDL_input <= 159:
        return "Borderline High"
    elif LDL_input < 130:
        return "Normal"
        
def output_LDL(LDL_test_result,LDL_analysis):
    print("The HDL result is {}".format(LDL_test_result))
    print("That is {}".format(LDL_analysis))


interface()