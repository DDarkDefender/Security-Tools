from pathlib import Path
import sys
import whois
import re
import pandas as pd

file_exists = False
run_script = True
extract_info = False

while (file_exists != True):
	input_file_name = input('Enter filename with each whois value in separate line.. ')
	file_path = Path(input_file_name)
	
	if file_path.is_file():
		file_exists = True
	else:
		print('File doesn\'t exist!! Please enter correct the name and path of the file!')
		run_script = input('Do you want to try again? (Type YES to continue)')
		if run_script.upper() != 'Y' or run_script.upper() != 'YES':
			sys.exit()

output_file_name = input('Enter filename where you want to store the results.. ')
file_object = open(output_file_name+ ".txt", "a")

extract_info_input = input('Do you want to extract ASN in excel? (Type YES to continue)')
print(extract_info_input)
if extract_info_input.upper() == 'Y' or extract_info_input.upper() == 'YES':
	extract_info = True
	excel_data = []

with open(input_file_name, 'r') as file:
	line = file.readline()

	while line:
		print('Performing whois for '+ line+ '...')
		result = whois.whois(line.rstrip())

		file_object.write("----- whois "+ line.rstrip() + " -----\n")
		file_object.write(result.text)
		file_object.write("\n")
		excel_row = []
		if extract_info == True:
			origin_data = ''
			orgName_data = ''
			excel_row.insert(0,line.rstrip())
			for ln in result.text.splitlines():
				if re.search('origin', ln):
					origin = ln.split()
					origin_data = ' '.join(origin[1:])

				if re.search('OrgName', ln):
					orgName = ln.split()
					orgName_data = ' '.join(orgName[1:])

			excel_row.insert(1,origin_data)
			excel_row.insert(2,orgName_data)
			excel_data.append(excel_row)
				
		line = file.readline()
#print(excel_data)
if extract_info == True:
	df = pd.DataFrame(excel_data,columns=['Input', 'ASN', 'Oranisation Name'])
	df.to_excel(output_file_name+ '.xlsx')

print('end')
file_object.close()