#! home/shiyanlou/calculator.py python3 
import sys 
import csv      
#pay=salary-3500-insurance
#tax=pay*rate-deduct

class Args(object):
    def __init__(self):
        self.args=sys.argv[1:]
    def read_function():
        with open(     ) as f1 :
            for f1 in 



class Config():
    def __init__(self,configfile):  #get and store the configure file
        self._config={ }  # define a dict 

    def get_config(self):  # get configure news from Configure target


class UserData(object):     #get and store the staff data 
    def __init__(self,userdatafile):
        self._userdata={}  # get the user's ID and laborage
    def dumptofile(self,outputfile):
        self
    def calculator(self):
       
    def dumptofile(self,outputfile):
        

class IncomeTaxCalculator(object):
    def calc_for_all_userdata(self):
	try:
	    for arg in sys.argv[1:]:
		total= arg.split(':')
		number=total[0]    
		salary=int(total[1])
		insurance=salary*(0.08+0.02+0.005+0.06)
		if salary>3500:
		    pay=salary-3500-insurance
		    if 0<pay<=1500:
			tax=pay*0.03-0
		    elif 1500<pay<=4500:
			tax=pay*0.1-105
		    elif 4500<pay<=9000:
			tax=pay*0.2-555
		    elif 9000<pay<=35000:
			tax=pay*0.25-1005
		    elif 35000<pay<=55000:
			tax=pay*0.3-2775
		    elif 55000<pay<=80000:
			tax=pay*0.35-5505
		    else: 
			tax=pay*0.45-1350
		    tax_salary=salary-tax-insurance
		else: tax_salary=salary-insurance
		     
		print('{}:{:.2f}'.format(number,tax_salary))
	except IndexError:
	    print('Parameter Error')
	except ValueError:
	    print('Parameter Error')

if __name__=='__main__':
    """     """
