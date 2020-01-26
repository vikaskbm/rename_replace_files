
# IMporting os module
import os

def main():

	for original_name in os.listdir():
		index = len(original_name)-1
		new_name = ''
		for ch in original_name:
			# print(ch)
			if ch=='-':
				new_name+=' '
			else:
				new_name+=ch;

		print(original_name)
		print(new_name)
		os.rename(original_name,new_name)



if __name__ == '__main__': 
      
    # Calling main() function 
    main() 







# METHODS TO RENAME FILES
# text = 'abcdefg'
# new = list(text)
# new[6] = 'W'
# ''.join(new)


# text = 'abcdefg'
# print(text)
# text = text[:1] + 'Z' + text[2:]
# print(text)




# A different program altogether(not relevant, just kept here because it was more easier than  deleting my babyyyyyyy)
# word = input("Enter a word")
# last = len(word)-1
# rev = ''

# for w in range(last,-1,-1):
# 	rev+=word[w]
# 	print(rev)