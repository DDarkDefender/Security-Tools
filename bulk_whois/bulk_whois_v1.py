from pathlib import Path
import sys
import whois

file_exists = False
run_script = True

while (file_exists != True):
	input_file_name = input('Enter filename with each whois value in separate line.. ')
	file_path = Path(input_file_name)
	
	if file_path.is_file():
		file_exists = True
	else:
		print('File doesn\'t exist!! Please enter correct the name and path of the file!')
		run_script = input('Do you want to try again? "(Type YES to continue)"')
		if run_script.casefold() != 'Y' or run_script.casefold() != 'YES':
			sys.exit()

output_file_name = input('Enter filename where you want to store the results.. ')
file_object = open(output_file_name, "a")

with open(input_file_name, 'r') as file:
	line = file.readline()

	while line:
		print('Performing whois for '+ line+ '...')
		result = whois.whois(line.rstrip())
		file_object.write("----- whois "+ line.rstrip() + " -----\n")
		file_object.write(result.text)
		file_object.write("\n")
		line = file.readline()
print('end')
