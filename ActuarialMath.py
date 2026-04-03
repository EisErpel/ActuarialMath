class ActuarialMath:
    def AVF(self, n: int, i: float):
        '''
        Function for getting the accumulated value factor of an investment

        Args:
            n (int): The number of years the investment accrues interest
            i (float): The interest rate of the investment

        '''
        return (1+i)**n
    
    def v(self, n: int, i: float):
        '''
        Function for getting the present value factor of an investment

        Args:
            n (int): The number of years the investment accrues interest
            i (float): The interest rate of the investment

        '''
        return 1/(self.AVF(n, i))
    
    def d(self, i: float):
        '''
        Function for getting the discount rate of an investment
        Args:
            i (float): The interest rate of the investment
        '''
        return i/(1+i)
    
    def i(self, d: float):
        '''
        Function for getting the interest rate of an investment
        Args:
            d (float): The discount rate of the investment
        '''
        return d/(1-d)
    
    def presentAnnuityImmediate(self, n: int, i: float):
        '''
        Function for calculating the present value factor of an annuity
        immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (1-self.v(n, i))/i
    
    def presentAnnuityDue(self, n: int, i: float):
        '''
        Function for calculating the present value factor of an annuity due
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (1-self.v(n, i))/self.d(i)
    
    def accumAnnuityImmediate(self, n: int, i: float):
        '''
        Function for calculating the accumulated value factor of an annuity
        immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (self.AVF(n, i)-1)/i
    
    def accumAnnuityDue(self, n: int, i: float):
        '''
        Function for calculating the accumulated value factor of an annuity due
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (self.AVF(n, i)-1)/self.d(i)
    
    def perpetuityImmediate(self, i: float):
        '''
        Function for calculating the present value factor of a perpetuity 
        immediate
        Args:
            i (float): The interest rate of the perpetuity
        '''
        return 1/i
    
    def perpetuityDue(self, i: float):
        '''
        Function for calculating the present value factor of a perpetuity due
        Args:
            i (float): The interest rate of the perpetuity
        '''
        return 1/self.d(i)
    
    