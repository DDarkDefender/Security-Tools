from pathlib import Path
import socket
import ipaddress
import pandas as pd

file_exists = False
reverse_lookup = False

while (file_exists != True):
	input_file_name = input('Enter filename with each value in separate line.. ')
	file_path = Path(input_file_name)
	
	if file_path.is_file():
		file_exists = True

output_file_name = input('Enter filename where you want to store the results.. ')

excel_data = []

with open(input_file_name, 'r') as file:
	line = file.readline()
	while line:
		excel_row = []
		print('Performing dns lookup for '+ line+ '...')
		#excel_row.insert(0,line.rstrip())
		try:
       			# Validate the IP address
       			ipaddress.ip_address(line.rstrip())
       			# Perform the reverse lookup
       			host = socket.gethostbyaddr(line.rstrip())
       			#print(host)
       			excel_row.insert(0,line.rstrip())
       			excel_row.insert(1,host[0])
		except ValueError:
			excel_row.insert(1,line.rstrip())
			try:
       				host = socket.gethostbyname(line.rstrip())
       				excel_row.insert(0,host)
			except socket.gaierror:
				print("No host found for this domain")
				excel_row.insert(0,"No host found for this domain")
		except socket.herror:
			print("No host found for this IP")
			excel_row.insert(0,line.rstrip())
			excel_row.insert(1,"No host found for this IP")

		excel_data.append(excel_row)
		line = file.readline()

df = pd.DataFrame(excel_data,columns=['IP', 'Host'])
df.to_excel(output_file_name+ '.xlsx')
