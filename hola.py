import random

def createPassword(longp):
	password=""
	abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz123456789"
	for x in range(longp):
		symbol=random.randint(1,62)
		password+=abc[symbol]
	return password
		

longp=int(input('Largo de contraseña ? '))
newPassword=createPassword(longp)
print(newPassword)