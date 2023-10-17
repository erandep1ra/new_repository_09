name = input("What is your name: ")
hours = float(input("How many hours did you work: "))
rate = float(input("How much do you get paid per hour: "))

def pay_monthly (name:str,hours:float,rate:float):
    

    pay = hours*rate
    print (name, "Your pay is:", pay)
pay_monthly(name,hours,rate)