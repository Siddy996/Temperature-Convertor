print("Convert Temperature into Different Units\n")
print("The Basic Temperature Units are : \n 1. Celsius \n 2. Fahrenheit \n 3. Kelvin \n 4. Rankine \n 5. Delisle \n 6. Newton\n 7. Réaumur\n 8. Rømer")
usertemp = int(input("Enter a Temperature Value: "))
print("Enter the Temperature Unit")
userunit = int(input("Enter the corresponding number from 1-8: "))
print("Enter the Unit it is to be converted into")
finalunit= int(input("Enter the corresponding number from 1-8: "))

def cf():
	finaltemp= usertemp * 9/5 +32
	return(finaltemp)
	
def ck(): 
	finaltemp=usertemp + 273.15
	return(finaltemp)
def cr():
	finaltemp = (usertemp + 273.15) * 9/5
	return(finaltemp) 
def cd():
	finaltemp = (100-usertemp) * 3/2
	return(finaltemp) 
def cn():
	finaltemp = usertemp * 33/100
	return(finaltemp)
def cre():
	finaltemp = usertemp * 4/5
	return(finaltemp) 
def cro():	
	finaltemp = usertemp *21/40 + 7.5
	return(finaltemp)

def fc():
	finaltemp = (usertemp - 32)*5/9
	return(finaltemp)
def fk():
	finaltemp = (usertemp + 459.67)*5/9
	return(finaltemp)
def fr():
	finaltemp = usertemp + 459.67
	return(finaltemp)
def fd():
	finaltemp = (212-usertemp)*5/6
	return(finaltemp)
def fn():
	finaltemp = (usertemp -32)*11/60
	return(finaltemp)
def fre():
	finaltemp = (usertemp -32)*4/9
	return(finaltemp)
def fro():
	finaltemp = (usertemp-32)*7/24+7.5
	return(finaltemp)

def kc():
	finaltemp = usertemp - 273.15
	return(finaltemp)
def kf():
	finaltemp = usertemp*9/5 - 459.67
	return(finaltemp)
def kr():
	finaltemp = usertemp*9/5
	return(finaltemp)
def kd():
	finaltemp = (373.15 - usertemp)*3/2
	return(finaltemp)
def kn():
	finaltemp = (usertemp - 273.15) *33/100
	return(finaltemp)
def kre():
	finaltemp = (usertemp - 273.15)*4/5
	return(finaltemp)
def kro():
	finaltemp = (usertemp-273.15)*21/40+7.5
	return(finaltemp)

def rc():
	finaltemp =  (usertemp - 491.67)*5/9
	return(finaltemp)
def rf():
	finaltemp = usertemp - 459.67
	return(finaltemp)
def rk():
	finaltemp = usertemp *5/9
	return(finaltemp)
def rn():
	finaltemp = (usertemp - 491.67)*11/60
	return(finaltemp)
def rd():
	finaltemp = (usertemp - 491.67)*11/60
	return(finaltemp)
def rre():
	finaltemp = (usertemp - 491.67)*4/9
	return(finaltemp)
def rro():
	finaltemp = (usertemp - 491.67)*7/24 +7.5
	return(finaltemp)


def nc():
	finaltemp= usertemp * 100/33
	return(finaltemp)
def nf():
	finaltemp = usertemp *60/11 +32
	return(finaltemp)
def nk():
	finaltemp = usertemp*100/33 +32
	return(finaltemp)
def nd():
	finaltemp = (33-usertemp)*50/11
	return(finaltemp)
def nr():
	finaltemp =  usertemp * 60/11 + 491.67
	return(finaltemp)
def nre():
	finaltemp= usertemp * 80/33
	return(finaltemp)
def nro():
	finaltemp = usertemp * 35/22 + 7.5
	return(finaltemp)


def rec():
	finaltemp = usertemp*5/4
	return(finaltemp)
def ref():
	finaltemp=usertemp*9/4 +32
	return(finaltemp)
def rek():
	finaltemp= usertemp*5/4+273.15
	return(finaltemp)
def red():
	finaltemp = (80-usertemp)*15/8
	return(finaltemp)
def rer():
	finaltemp = usertemp*9/4 + 491.67
	return(finaltemp)
def rero():
	finaltemp = usertemp*21/32 + 7.5
	return(finaltemp)
def ren():
	finaltemp = usertemp*33/80
	return(finaltemp)



def roc(): 
	finaltemp = (usertemp -7.5)*40/21
	return(finaltemp)
def rof():
	finaltemp = (usertemp -7.5)*24/7 +32
	return(finaltemp)
def rok():
	finaltemp = (usertemp - 7.5) * 40/21 + 273.15
	return(finaltemp)
def rore():
	finaltemp = (usertemp - 7.5)*24/7 + 491.67
	return(finaltemp)
def rod():
	finaltemp = (60 - usertemp)*20/7
	return(finaltemp)
def rodn():
	finaltemp = (usertemp -7.5)*22/35
	return(finaltemp)
def ror():
	finaltemp = (usertemp -7.5)*32/21
	return(finaltemp)


def dc():
	finaltemp = 100 - usertemp*2/3
	return(finaltemp)
def df():
	finaltemp = 212 - usertemp*6/5
	return(finaltemp)
def dk():
	finaltemp = 373.15-usertemp*2/3
	return(finaltemp)
def dr():
	finaltemp = 671.67 - usertemp*6/5
	return(finaltemp)
def dre():
	finaltemp = 80 - usertemp*8/15
	return(finaltemp)
def dro():
	finaltemp = 60 - usertemp*7/20
	return(finaltemp)
def dn():
	finaltemp = 33-usertemp*11/50
	return(finaltemp)




while userunit==1:
	if finalunit==2:
		print("The Temperature in Fahrenheit is : ", cf())
		break
	elif finalunit==3:
		print("The Temperature in Kelvin is : ", ck())
		break
	elif finalunit==4:
		print("The Temperature in Rankine is : ", cr())
		break
	elif finalunit==5:
		print("The Temperature in Delise is : ", cd())
		break
	elif finalunit==6:
		print("The Temperature in Newton is : ", cn())
		break
	elif finalunit==7:
		print("The Temperature in Réaumur is : ", cre())
		break
	elif finalunit==8:
		print("The Temperature in Rømer is : ", cro())
		break

while userunit==2:
	if finalunit==1:
		print("The Temperature in Celsius is : ", fc())
		break
	elif finalunit==3:
		print("The Temperature in Kelvin is : ", fk())
		break
	elif finalunit==4:
		print("The Temperature in Rankine is : ", fr())
		break
	elif finalunit==5:
		print("The Temperature in Delise is : ", fd())
		break
	elif finalunit==6:
		print("The Temperature in Newton is : ", fn())
		break
	elif finalunit==7:
		print("The Temperature in Réaumur is : ", fre())
		break
	elif finalunit==8:
		print("The Temperature in Rømer is : ", fro())
		break

while userunit==3:
	if finalunit==1:
		print("The Temperature in Celsius is : ", kc())
		break
	elif finalunit==2:
		print("The Temperature in Fahrenheit is : ", kf())
		break
	elif finalunit==4:
		print("The Temperature in Rankine is : ", kr())
		break
	elif finalunit==5:
		print("The Temperature in Delisle is : ", kd())
		break
	elif finalunit==6:
		print("The Temperature in Newton is : ", kn())
		break
	elif finalunit==7:
		print("The Temperature in Réaumur is : ", kre())
		break
	elif finalunit==8:
		print("The Temperature in Rømer is : ", kro())
		break

while userunit==4:
	if finalunit==1:
		print("The Temperature in Celsius is : ", rc())
		break
	elif finalunit==2:
		print("The Temperature in Fahrenheit is : ", rf())
		break
	elif finalunit==3:
		print("The Temperature in Kelvin is : ", rk())
		break
	elif finalunit==5:
		print("The Temperature in Delisle is : ", rd())
		break
	elif finalunit==6:
		print("The Temperature in Newton is : ", rn())
		break
	elif finalunit==7:
		print("The Temperature in Réaumur is : ", rre())
		break
	elif finalunit==8:
		print("The Temperature in Rømer is : ", rro())
		break

while userunit==5:
	if finalunit==1:
		print("The Temperature in Celcius is : ", dc())
		break
	elif finalunit==2:
		print("The Temperature in Fahrenheit is : ", df())
		break
	elif finalunit==3:
		print("The Temperature in Kelvin is : ", dk())
		break
	elif finalunit==4:
		print("The Temperature in Rankine is : ", dr())
		break
	elif finalunit==6:
		print("The Temperature in Newton is : ", dn())
		break
	elif finalunit==7:
		print("The Temperature in Réaumur is : ", dre())
		break
	elif finalunit==8:
		print("The Temperature in Rømer is : ", dro())
		break

while userunit==6:
	if finalunit==1:
		print("The Temperature in Celsius is : ", nc())
		break
	elif finalunit==2:
		print("The Temperature in Fahrenheit is : ", nf())
		break
	elif finalunit==3:
		print("The Temperature in Kelvin is : ", nk())
		break
	elif finalunit==4:
		print("The Temperature in Rankine is : ", nr())
		break
	elif finalunit==5:
		print("The Temperature in Delisle is : ", nd())
		break
	elif finalunit==7:
		print("The Temperature in Réaumur is : ", nre())
		break
	elif finalunit==8:
		print("The Temperature in Rømer is : ", nro())
		break

while userunit==7:
	if finalunit==1:
		print("The Temperature in Celsius is : ", rec())
		break
	elif finalunit==2:
		print("The Temperature in Fahrenheit is : ", ref())
		break
	elif finalunit==3:
		print("The Temperature in Kelvin is : ", rek())
		break
	elif finalunit==4:
		print("The Temperature in Rankine is : ", rer())
		break
	elif finalunit==5:
		print("The Temperature in Delisle is : ", red())
		break
	elif finalunit==6:
		print("The Temperature in Newton is : ", ren())
		break
	elif finalunit==8:
		print("The Temperature in Rømer is : ", rero())
		break

while userunit==8:
	if finalunit==1:
		print("The Temperature in Celsius is : ", roc())
		break
	elif finalunit==2:
		print("The Temperature in Fahrenheit is : ", rof())
		break
	elif finalunit==3:
		print("The Temperature in Kelvin is : ", rok())
		break
	elif finalunit==4:
		print("The Temperature in Rankine is : ", ror())
		break
	elif finalunit==5:
		print("The Temperature in Delisle is : ", rod())
		break
	elif finalunit==6:
		print("The Temperature in Newton is : ", ron())
		break
	elif finalunit==7:
		print("The Temperature in Réaumur is : ", rore())
		break
