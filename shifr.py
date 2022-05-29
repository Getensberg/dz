alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

dict_count_encoding = {x:{} for x in alph}
dict_count_decoding = {x:{} for x in alph}
def to_index(string):
	list_of_chars = []
	for char in string:
		for c,zx in enumerate(alph):
			if  char==' ':
				list_of_chars.append(' ')
				break
			if zx ==char:
				list_of_chars.append(c)
				break
	return list_of_chars



def encoding(forKey,forWord):
	round_counter = 0
	encoded_message=''
	forKey=to_index(forKey)
	forWord= to_index(forWord)
	for index in forWord:
		if len(forKey)==round_counter:
			round_counter = 0
		if index == ' ':
			#print(j)
			encoded_message+=' '
			continue
		gg=(index+forKey[round_counter])#3+2
		char = alph[gg%len(alph)]
		try:
			dict_count_encoding[char][key[round_counter]] +=1

			
		except:
			dict_count_encoding[char][key[round_counter]] =1
		encoded_message+=char
		round_counter +=1
	return encoded_message

def decoding(forKey,forWord):
	round_counter = 0
	encoded_message=''
	key = forKey
	forKey=to_index(forKey)
	forWord= to_index(forWord)
	for index in forWord:
		if len(forKey)==round_counter:
			round_counter = 0
		if index == ' ':
			#print(j)
			encoded_message+=' '
			continue
		gg=(index-forKey[round_counter])#3+2
		char = alph[gg%len(alph)]
		try:
			dict_count_decoding[char][key[round_counter]] +=1

			
		except:
			dict_count_decoding[char][key[round_counter]] =1

		encoded_message+=char
		round_counter +=1
	return encoded_message


key=input('введите ключ\n')
key = key.split()
key = ''.join(key)
word=input('слово для зашиfровки\n')
message = (encoding(key,word))
print("Encrypted message: "+(message))
for i in dict_count_encoding:

	for z in dict_count_encoding[i]:

		print(f'{i} шифровался {z} - {dict_count_encoding[i][z]}')

print("Decrypted message: "+((decoding(key,message))))
print('\n')
for i in dict_count_decoding:

	for z in dict_count_decoding[i]:

		print(f'{i} дешифровался {z} - {dict_count_decoding[i][z]}')