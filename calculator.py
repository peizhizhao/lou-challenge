# step : 1.anlay parameter 2read config 3 read data 4 calculator 5 output 

import sys
 
class ArgError(Exception):
    pass 

class Args:
## chu li minglinghang canshu
    def __init__(self,args):
         
         self.args=args
    
    def __parse_arg(self,arg):
         try:
            #get value of parameters by index 
             value=self.args[self.args.index(arg)+1]
             except (ValueError,IndexError):
                 value=None
  	     return value
    def get_arg(self,arg):
          value=self.__parse_arg(arg)
	  if value is None:
	      raise ArgError('not found ars s%',%arg)
	  return value 

class SheBaoConfig:
##shebao config file class
    def __init__(self,file):
        self.jishu_low,self.jishu_high,self.total_rate=self.__parse_cofig(file)
    def __parse_config(self,file):
        ##jie xi shebao canshu config file
        rate=0
        jishu_low=0
        jishu_high=0

        with open(file) as f:
	    for line in f:
 	        key,value=line.split('=')
  		key=key.strip()
		try:
		    value=float(value.strip())
		except ValueError:
		    continue
		if key=='JiShuL':
		    jishu_low=value
		elif key=='JiShuH':
		    jishu_high=value
		else:
		    rate+=value
	return jishu_low,jishu_high,rate

class EmployeeData:
##employee data achieve class
    def __init__(self,file):
	
	self.data=self.__parse_file(file)
    def __parse_file(self,file):
	data=[]
	for line in open(file):
            employee_id,gongzi=line.split(',')
            data.append((int(employee_id),int(gongzi)))
	return data

    def __iter__(self):
        









































