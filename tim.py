clock = input('введите время\n')

def convert_to_time_format(clock):

	clock = clock.split(':')
	timesOfDay = ''
	clock = [int(i) for i in clock]
	suffix = ''
	if clock[1]>=60:
		raise Exception("не верный ввод")
	if int(str(clock[1])[-1])==1:
		suffix='а'
	elif 1<=int(str(clock[1])[-1])<=4:
		suffix='ы'
	if clock[0] == 00 and clock[1] == 00:
		return 'полночь'
	elif clock[0] == 12 and clock[1] == 00:
		return 'полдень'


	elif 0<=clock[0]<=4 or 20<=clock[0]<=23:
		timesOfDay = 'ночи'
	elif 4<=clock[0]<=11:
		timesOfDay='утра'
	elif 12<=clock[0]<=16:
		timesOfDay = 'дня'
	elif 16<=clock[0]<=20:
		timesOfDay = 'вечера'
	else:
		raise Exception("не верный ввод")
	if clock[0]>=13:
		clock[0] -=12

	return f'{clock[0]} часов {clock[1]} минут{suffix} {timesOfDay}'

print(convert_to_time_format(clock))

