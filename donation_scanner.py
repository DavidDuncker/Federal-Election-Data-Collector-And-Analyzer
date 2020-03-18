import read_file


def read_line(working_directory):
	files = ["donation_data_2008", "donation_data_2010", "donation_data_2012", "donation_data_2014",
				"donation_data_2016", "donation_data_2018", "donation_data_2020"]
	for file in files:
		donation_data = read_file.generate_line_data(working_directory, file)
		for line_data in donation_data:
			donation_info = line_data[0]
			line_number = line_data[1]
			number_of_lines = line_data[2]
			if line_number % 20000 == 0:
				print("Reading line " + str(line_number) + " out of " + str(number_of_lines) + ".")
			yield donation_info
