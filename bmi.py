def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))

    #Code to calculate BMI
    bmi=weight/(height+height)
    
    #Code to Display BMI
    print("BMI="+str(bmi))
    return(bmi)

#Function to Classify BMI Range
def  bmi_range(bmi):
    if(bmi < 18.5):
        print("Classified Under Weight")
        return -1
    elif(bmi <= 18.5 and bmi <= 25.0):
        print("Classified Normal Weight")
        return 0
    elif(bmi > 25.0):
        print("Classified Over Weight")
        return 1
    else:
        print("error")


bmi = calculate_bmi(weight=57,height=1.73)
bmi_range(bmi)