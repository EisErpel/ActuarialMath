class rate:
    @staticmethod
    def d(i: float):
        '''
        Function for getting the discount rate of an investment
        Args:
            i (float): The interest rate of the investment
        '''
        return i/(1+i)
    
    @staticmethod
    def i(d: float):
        '''
        Function for getting the interest rate of an investment
        Args:
            d (float): The discount rate of the investment
        '''
        return d/(1-d)
    

class lumpSum:
    @staticmethod
    def AVF(n: int, i: float):
        '''
        Function for getting the accumulated value factor of an investment

        Args:
            n (int): The number of years the investment accrues interest
            i (float): The interest rate of the investment

        '''
        return (1+i)**n
    
    @staticmethod
    def v(n: int, i: float):
        '''
        Function for getting the present value factor of an investment

        Args:
            n (int): The number of years the investment accrues interest
            i (float): The interest rate of the investment

        '''
        return 1/(lumpSum.AVF(n, i))
    
class constAnnuity:
    @staticmethod
    def PVFImmediate(n: int, i: float):
        '''
        Function for calculating the present value factor of a constant
        annuity immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (1-lumpSum.v(n, i))/i
    
    @staticmethod
    def PVFDue(n: int, i: float):
        '''
        Function for calculating the present value factor of a constant
        annuity due
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (1-lumpSum.v(n, i))/rate.d(i)
    
    @staticmethod
    def AVFImmediate(self, n: int, i: float):
        '''
        Function for calculating the accumulated value factor of a constant
        annuity immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (lumpSum.AVF(n, i)-1)/i
    
    @staticmethod
    def AVFDue(n: int, i: float):
        '''
        Function for calculating the accumulated value factor of a constant
        annuity due
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (lumpSum.AVF(n, i)-1)/rate.d(i)
    
class constPerpetuity:
    @staticmethod
    def PVFImmediate(i: float):
        '''
        Function for calculating the present value factor of a constant
        perpetuity immediate
        Args:
            i (float): The interest rate of the perpetuity
        '''
        return 1/i
    
    @staticmethod
    def PVFDue(i: float):
        '''
        Function for calculating the present value factor of a constant
        perpetuity due
        Args:
            i (float): The interest rate of the perpetuity
        '''
        return 1/rate.d(i)
    
class incAnnuity:
    @staticmethod
    def PVFImmediate(n: int, i: float):
        '''
        Function for calculating the present value factor of an increasing 
        annuity immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (constAnnuity.PVFDue(n, i) - n * lumpSum.v(n, i))/i
    
    @staticmethod
    def PVFDue(n: int, i: float):
        '''
        Function for calculating the present value factor of an increasing 
        annuity immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (constAnnuity.PVFDue(n, i) - n*lumpSum.v(n, i))/rate.d(i)
    
    @staticmethod
    def AVFImmediate(n: int, i: float):
        '''
        Function for calculating the accumulated value factor of an increasing
        annuity immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (constAnnuity.AVFDue(n, i) - n)/i
    
    @staticmethod
    def AVFDue(n: int, i: float):
        '''
        Function for calculating the accumulated value factor of an increasing
        annuity due
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (constAnnuity.AVFDue(n, i) - n)/rate.d(i)
    
class incPerpetuity:
    @staticmethod
    def PVFImmediate(i: float):
        '''
        Function for calculating the present value factor of an increasing 
        perpetuity immediate
        Args:
            i (float): The interest rate of the annuity
        '''
        return(1+i)/i**2
    
    @staticmethod
    def PVFDue(i: float):
        '''
        Function for calculating the present value factor of an increasing 
        perpetuity due
        Args:
            i (float): The interest rate of the annuity
        '''
        return 1/rate.d(i)**2
    
class decAnnuity:
    @staticmethod
    def PVFImmediate(n: int, i: float):
        '''
        Function for calculating the present value factor of a decreasing 
        annuity immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (n - constAnnuity.PVFImmediate(n, i))/i
    
    @staticmethod
    def PVFDue(n: int, i:float):
        '''
        Function for calculating the present value factor of a decreasing 
        annuity due
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (n - constAnnuity.PVFImmediate(n, i))/rate.d(i)
    
    @staticmethod
    def AVFImmediate(n: int, i: float):
        '''
        Function for calculating the accumulated value factor of a decreasing 
        annuity immediate
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (n*lumpSum.AVF(n, i) - constAnnuity.AVFImmediate(n, i))/i
    
    @staticmethod
    def AVFDue(n: int, i: float):
        '''
        Function for calculating the accumulated value factor of a decreasing 
        annuity due
        Args:
            n (int): The number of years the annuity accrues interest
            i (float): The interest rate of the annuity
        '''
        return (n*lumpSum.AVF(n, i) - constAnnuity.AVFImmediate(n, i))/rate.d(i)