import random

def createPassword(longp):
	password=""
	abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz123456789"
	for x in range(longp):
		password+=abc[random.randint(0,len(abc)-1)]
	return password
		
longp=int(input('Largo de contraseña ? '))
print(createPassword(longp))
