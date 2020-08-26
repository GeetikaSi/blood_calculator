def interface():
    print("My Program")
    while True:
        print("Options")
        print("Enter '1' to check HDL value")
        print("Enter '2' to check LDL value")
        print("Enter '9' to Quit")
        choice = input("Enter your choice ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()

def HDL_driver():
    #Get input
    #Check if HDL is normal
    #Output
    HDL_value = input_HDL()
    HDL_analysis = HDL_process(HDL_value)
    output(HDL_value, HDL_analysis)
    yn = input("Do you want to check analysis for your LDL value? (y/n)")
    if yn == 'y':
        LDL_driver()
    elif yn == 'n':
        return
     
def input_HDL():
#input function returns a string
    HDL_input = input("Enter your HDL value: ")
    return int(HDL_input)

def HDL_process(HDL_input): 
    if HDL_input >= 60:
        return "Normal"
    elif 40 <= HDL_input < 60:
        return "Borderline Low"
    elif HDL_input < 40:
        return "Low"
        
def output(test_result,analysis):
    print("The HDL result is {}".format(test_result))
    print("That is {}".format(analysis))


def LDL_driver():
    #Get input
    #Check if LDL is normal
    #Output
    LDL_value = input_LDL()
    LDL_analysis = LDL_process(LDL_value)
    output_LDL(LDL_value, LDL_analysis)
    yn_LDL = input("Do you want to check analysis for your HDL value?(y/n)")
    if yn_LDL == 'y':
        HDL_driver()
    elif yn_LDL == 'n':
        return
     
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