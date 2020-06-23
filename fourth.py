

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(lists):
	stringg=''
	for index,value in enumerate(lists):


		stringg+=value
		if  index != ((len(lists)-1) or (len(lists)-2)):
				stringg+=',' 
		if index==(len(lists)-2):

			stringg+='and '



		

	return stringg

print(comma(spam))