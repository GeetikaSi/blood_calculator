def interface():
    print("My Program")
    while True:
        print("Options")
        print("Enter '1' to check HDL value")
        print("Enter '9' to Quit")
        choice = input("Enter your choice ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    #Get input
    #Check if HDL is normal
    #Output
    HDL_value = input_HDL()
    HDL_analysis = HDL_process(HDL_value)
    output(HDL_value, HDL_analysis)
     
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



interface()