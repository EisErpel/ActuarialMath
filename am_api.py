import ActuarialMath as am

finished = False
def financialAPI():
    print("Please enter the payment scheme of your investment.")
    print("For lump sum, type L")
    print("For annuity, type A")
    print("For perpetuity , type P")
    scheme = input("Choice: ")
    if scheme != "L" and scheme != "A" and scheme != "P":
         TypeError("Invalid payment scheme!")
    elif scheme == "L":
        dir = input("Would you like to find the (F)uture Value or (P)resent Value?")
        if dir != "F" and dir != "P":
            raise TypeError("Invalid value type!")

        principal = float(input("Please Enter the principal of the investment: "))
        numYears = int(input("Please Enter the number of accruing years: "))
        interest = float(input("Please Enter the interest rate: "))

        if dir == "F":
            return principal * am.lumpSum.AVF(numYears, interest)
        elif dir == "P":
            return principal * am.lumpSum.v(numYears, interest)
    elif scheme == "A": 
        startOrEnd = input("Is your investment an Annuity (I)mmediate or an Annuity (D)ue?")
        if startOrEnd != "I" and startOrEnd != "D":
            raise TypeError("Must be annuity immediate or due!")
        
        dir = input("Would you like to find the (F)uture Value or (P)resent Value?")
        if dir != "F" and dir != "P":
            raise TypeError("Invalid value type!")
        
        print("Please enter the payment stream of your investment.")
        print("For constant payments, type C")
        print("For increasing payments, type I")
        print("For decreasing payments, type D")
        payment = input("Choice: ")
        if payment != "C" and payment != "I" and payment != "D":
            raise TypeError("Invalid payment stream!")
        

        principal = float(input("Please Enter the periodic payement: "))
        numYears = int(input("Please Enter the number of accruing years: "))
        interest = float(input("Please Enter the interest rate: "))

        if payment == "C":
            if startOrEnd == "I":
                if dir == "F":
                    return principal * am.constAnnuity.AVFImmediate(numYears, interest)
                elif dir == "P":
                    return principal * am.constAnnuity.PVFImmediate(numYears, interest)
            elif startOrEnd == "D":
                if dir == "F":
                    return principal * am.constAnnuity.AVFDue(numYears, interest)
                elif dir == "P":
                    return principal * am.constAnnuity.PVFDue(numYears, interest)
        elif payment == "I":
            if startOrEnd == "I":
                if dir == "F":
                    return principal * am.incAnnuity.AVFImmediate(numYears, interest)
                elif dir == "P":
                    return principal * am.incAnnuity.PVFImmediate(numYears, interest)
            elif startOrEnd == "D":
                if dir == "F":
                    return principal * am.incAnnuity.AVFDue(numYears, interest)
                elif dir == "P":
                    return principal * am.incAnnuity.PVFDue(numYears, interest)
        elif payment == "D":
            if startOrEnd == "I":
                if dir == "F":
                    return principal * am.decAnnuity.AVFImmediate(numYears, interest)
                elif dir == "P":
                    return principal * am.decAnnuity.PVFImmediate(numYears, interest)
            elif startOrEnd == "D":
                if dir == "F":
                    return principal * am.decAnnuity.AVFDue(numYears, interest)
                elif dir == "P":
                    return principal * am.decAnnuity.PVFDue(numYears, interest)
                
print("The value of your investment is:", financialAPI())
            

    


