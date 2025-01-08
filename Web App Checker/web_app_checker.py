from pathlib import Path
import sys
import webbrowser

file_exists = False

while (file_exists != True):
	input_file_name = input('Enter filename with each domain name in a separate line.. ')
	file_path = Path(input_file_name)
	
	if file_path.is_file():
		file_exists = True
	else:
		print('File doesn\'t exist!! Please enter correct the name and path of the file!')
		run_script = input('Do you want to try again? "(Type YES to continue)"')
		if run_script.casefold() != 'Y' or run_script.casefold() != 'YES':
			sys.exit()

print('Redirecting..')
with open(input_file_name, 'r') as file:
	line = file.readline()
	
	while line:
		webbrowser.open_new_tab("http://"+line.rstrip())
		line = file.readline()
	
print('-end-')
