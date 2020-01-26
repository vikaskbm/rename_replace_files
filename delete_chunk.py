
# IMporting os and re modules
import re
import os

def main():
	cwd=os.getcwd()
	print(os.listdir())
	for original_name in os.listdir():
		new_name=''
		index = len(original_name)-1

		if original_name.endswith("(z lib.org).pdf"):
			new_name = original_name[:-15]+'.pdf'
			os.path.join(cwd,new_name)
			os.rename(os.path.join(cwd,original_name),os.path.join(cwd,new_name))

		if original_name.endswith("(z lib.org).epub"):
			new_name = original_name[:-16]+'.epub'
			os.path.join(cwd,new_name)
			os.rename(os.path.join(cwd,original_name),os.path.join(cwd,new_name))

		print(original_name)
		print(new_name)


if __name__ == '__main__': 
      
    # Calling main() function 
    main()




### removing '[' and ']'


# IMporting os and re modules
# import re
# import os

# def main():
# 	cwd=os.getcwd()
# 	print(os.listdir())
# 	for original_name in os.listdir():
# 		new_name=''
# 		index = len(original_name)-1

# 		for ch in range(1,index):

# 			if original_name[ch]==']':
# 				new_name = original_name[:ch]+original_name[ch+1:]
# 				os.rename(os.path.join(cwd,original_name),os.path.join(cwd,new_name))

# 		print(original_name)
# 		print(new_name)


# if __name__ == '__main__': 
      
#     # Calling main() function 
#     main()




# url = 'abcdc.com'
# if url.endswith('.com'):
#     url = url[:-4]
# Or using regular expressions:

# import re
# url = 'abcdc.com'
# url = re.sub('\.com$', '', url)