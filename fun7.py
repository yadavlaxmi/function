def fun(a):
    bmi=a/2
    if bmi<=18.5:
        return "underweight"
    elif bmi<=25.0:
        return "normal"
    elif bmi<=30.0:
        return "overweight"
    elif bmi>30:
        return "obese"
    else:
        return "nothing"
print(fun((int(input("weight")))))