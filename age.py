driving = input('have you driven before? ')
if driving!= 'yes' and driving != 'never':
	print('can only inpu yes or never')
	raise SystemExit

age = input('how old are you? ')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('you are all good!')
	else:
		print('dude! you are in trouble!')
elif driving == 'never':
	if age >= 18:
		print('dude go get a license! ')
	else:
		print('coo coo, just give it some more years.')
else:
	print('can only say yes or never')
