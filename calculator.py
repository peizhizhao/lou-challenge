#! home/shiyanlou/calculator.py python3 

import sys 
#pay=salary-3500
#tax=pay*rate-deduct

try:
    salary=int(sys.argv[1])
    pay=salary-3500
    
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
    else: tax=pay*0.45-13505
    print(format(tax,'.2f'))
except IndexError:
    print('Parameter Error')
except ValueError:
    print('Parameter Error')
