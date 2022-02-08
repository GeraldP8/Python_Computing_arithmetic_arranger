#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
#
#Output:
#
#   32      3801      45      123
#+ 698    -    2    + 43    +  49
#-----    ------    ----    -----

def arithmetic_arranger(problems, displayMode=False):

        
    arith = problems

    space = "    "
    line1_final = ""
    line2_final = ""
    line3_final = ""
    line4_final = ""

    try:
        #Check amount of problems, may not be more than 5
        if len(arith) > 5:
            raise BaseException
    except:
        return "Error to many problems."

    for equation in arith:


        
        #Split values into its own variables
        equationList = equation.split()
        #split first, second and third line into respective variables
        number1 = equationList[0]
        number2 = equationList[2]
        oper = equationList[1]

        #print(type(number1))
        #check that all numbers are actual numbers
        try:
            if not int(number1):
                
                raise BaseException
        except:
            return "Error: Numbers must only contain digits."

        try:
            if not int(number2):
                
                raise BaseException
        except:
            return "Error: Numbers must only contain digits."

        #Check that operation is valid
        try:
            if oper != "+" and oper != "-":
                raise BaseException
        except:
            return "Error: Operator must be '+' or '-'."
       
        #Calculate optional result for final line
        if oper == "+" and displayMode == True:
            operResult = int(number1) + int(number2)
        elif oper == "-" and displayMode == True:
            operResult = int(number1) - int(number2)

        #Get the longest number2
        if len(number1) >= len(number2):
            maxLen = len(number1) + 2
        elif len(number2) > len(number1):
            maxLen = len(number2) + 2

        #Check that the numbers are not more than 4
        try:
            if maxLen - 2 > 4:
                raise BaseException
        except:
            return "Error: Numbers cannot be more than four digits."
            

        #Build Line1
        line1 = ""
        line1 = str(number1).rjust(maxLen)
        #Build final line1 output
        line1_final = line1_final + line1 + space

        #Build Line 2
        line2 = ""
        #line2 = str(oper) + space + str(line2) + str(number2)
        line2 = oper + str(number2).rjust(maxLen - 1) 
        #Build final line2 output
        line2_final = line2_final + line2 + space
        #print(oper)

        #Build line 3 which is static
        line3 = "-" * maxLen
        #print(line3)
        line3 = str(line3).rjust(maxLen)
        line3_final = line3_final + line3 + space

        if displayMode:
            #Build Line1
            line4 = ""
            line4 = str(operResult).rjust(maxLen)
            #Build final line1 output
            line4_final = line4_final + line4 + space



    #Build final output
    newline = '\n'

    if not displayMode:
        arranged_problems = (line1_final.rstrip() + newline + line2_final.rstrip() + newline + line3_final.rstrip())
    elif  displayMode:
        arranged_problems = (line1_final.rstrip() + newline + line2_final.rstrip() + newline + line3_final.rstrip() + newline + line4_final.rstrip())

 
    return arranged_problems


arr = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']

print(arithmetic_arranger(arr, True))


