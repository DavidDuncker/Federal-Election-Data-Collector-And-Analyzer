import sqlite3
import os

import donation_scanner


def database_table_does_exist(working_directory, table):
	database = os.path.join(working_directory, "elections.db")
	try:
		connection = sqlite3.connect(database)
		cursor = connection.cursor()
		cursor.execute("select * from " + table)
		connection.close()
		print("Table " + table + " found")
		return True
	except:
		print("Table " + table + " not found")
		return False


def find_missing_database_tables(working_directory):
	required_databases = ["candidates", "campaigns", "committees", "donations"]
	missing_databases = []
	for database in required_databases:
		if database_table_does_exist(working_directory, database):
			continue
		else:
			missing_databases.append(database)
	return missing_databases


def iterate_list(_list):
	for item in _list:
		yield item


def create_all_database_tables(working_directory, list_of_committees, list_of_candidates, list_of_campaigns):
	required_tables = ["candidates", "campaigns", "committees", "donations"]
	table_columns = {}
	table_column_types = {}
	iterator = {}
	table_columns["candidates"] = ['FEC_web_link', 'name', 'year', 'id', 'office', 'state', 'district', 'party',
                                  'Cand_Incumbent_Challenger_Open_Seat', 'receipts', 'disbursement',
                                  'cash_on_hand', 'Debt_Owed_By_Committee', 'Coverage_End_Date', 'Cand_Street_1',
                                  'Cand_Street_2', 'city', 'zip_code', 'Individual_Itemized_Contribution',
                                  'Individual_Unitemized_Contribution', 'Individual_Contribution',
                                  'Other_Committee_Contribution', 'Party_Committee_Contribution',
                                  'Cand_Contribution', 'Total_Contribution', 'Transfer_From_Other_Auth_Committee',
                                  'Cand_Loan', 'Other_Loan', 'Total_Loan', 'Offsets_To_Operating_Expenditure',
                                  'Offsets_To_Fundraising', 'Offsets_To_Leagal_Accounting', 'Other_Receipts',
                                  'Operating_Expenditure', 'Exempt_Legal_Accounting_Disbursement',
                                  'Fundraising_Disbursement', 'Transfer_To_Other_Auth_Committee',
                                  'Cand_Loan_Repayment', 'Other_Loan_Repayment', 'Total_Loan_Repayment',
                                  'Individual_Refund', 'Party_Committee_Refund', 'Other_Committee_Refund',
                                  'Total_Contribution_Refund', 'Other_Disbursements', 'Net_Contribution',
                                  'Net_Operating_Expenditure', 'Cash_On_Hand_BOP', 'Debt_Owe_To_Committee',
                                  'Coverage_Start_Date']
	table_column_types["candidates"] = ['text', 'text', 'integer', 'text', 'text', 'text', 'text', 'text', 'text',
	                                    'real', 'real', 'real', 'real', 'text', 'text', 'text', 'text',
	                                    'text', 'real', 'real', 'real', 'real', 'real', 'real', 'real', 'real',
	                                    'real', 'real', 'real', 'real', 'real', 'real', 'real', 'real', 'real',
	                                    'real', 'real', 'real', 'real', 'real', 'real', 'real', 'real', 'real', 'real',
	                                    'real', 'real', 'real', 'real', 'text']
	iterator["candidates"] = iterate_list(list_of_candidates)
	table_columns["campaigns"] = ['year', 'state', 'state_po', 'state_fips', 'state_cen', 'state_ic', 'office',
	                              'district', 'stage', 'runoff', 'special', 'name', 'party', 'writein', 'mode',
	                              'candidatevotes', 'totalvotes', 'unofficial', 'version', 'candidate_id',
	                              'committee_id']
	table_column_types["campaigns"] = ['INTEGER', 'TEXT', 'TEXT', 'INTEGER', 'INTEGER', 'INTEGER', 'TEXT', 'INTEGER',
	                                   'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'INTEGER', 'INTEGER',
	                                   'TEXT', 'TEXT', 'TEXT', 'TEXT']
	iterator["campaigns"] = iterate_list(list_of_campaigns)
	table_columns["committees"] = ["FEC_web_link", "committee_id", "name", "committee_type",
	                "committee_designation",
                     "filing_frequency", "address_1", "address_2", "city", "state", "zip_code", "treasurers_name",
                     "candidate_id", "election_year", "individual_contribution", "party_committee_contribution",
                     "other_committee_contribution", "total_contribution", "transfer_from_other_authorized_committee",
                     "offsets_to_operating_expenditure", "other_receipts", "total_receipts",
                     "transfer_to_other_authorized_committee", "other_loan_repayment", "individual_refund",
                     "political_party_committee_refund", "total_contribution_refund", "other_disbursement",
                     "total_disbursement", "net_contribution", "net_operating_expenditure",
                     "cash_on_hand_beginning_of_period", "coverage_start_date", "cash_on_hand_closing_of_period",
                     "coverage_end_date", "debt_owed_by_committee", "debt_owed_to_committee",
                     "individual_itemized_contribution", "individual_unitemized_contribution", "other_loan",
                     "transfer_from_non_federal_account", "transfer_from_non_federal_levin_account",
                     "total_nnon_federal_transfer", "loan_repayments_received",
                     "offsets_to_fundraising_expenses_presidential_only",
                     "offsets_to_legalaccounting_expenses_presidential_only", "federal_candidate_contribution_refund",
                     "total_federal_receipt", "shared_federal_operating_expenditure",
                     "shared_nonfederal_operating_expenditure", "other_federal_operating_expenditures",
                     "total_operating_expenditure", "federal_candidate_committee_contribution",
                     "independent_expenditures_made", "coordinated_expenditure_party_only", "loan_made",
                     "federal_share_of_joint_federal_election_activity",
                     "nonfederal_share_of_joint_federal_election_activity",
                     "nonallocated_federal_election_activity_party_only", "total_federal_election_activity",
                     "total_federal_disbursement", "candidate_contribution", "candidate_loan", "total_loan",
                     "operating_expenditure", "candidate_loan_repayment", "total_loan_repayment",
                     "other_committee_refund", "total_offsets_to_operating_expenditure",
                     "exempt_legalaccounting_disbursement_presidential_only", "fundraising_disbursement",
                     "itemized_refunds_or_rebates", "subtotal_refunds_or_rebates", "unitemized_refunds_or_rebates",
                     "itemized_other_refunds_or_rebates", "unitemized_other_refunds_or_rebates",
                     "subtotal_other_refunds_or_rebates", "itemized_other_income", "unitemized_other_income",
                     "expenditures_subject_to_limit_prior_year_presidential_only", "expenditures_subject_to_limit",
                     "federal_funds", "itemized_convention_expenditure_convention_committee_only",
                     "itemized_other_disbursement", "subtotal_convention_expenses",
                     "total_expenditures_subject_to_limit_presidential_only", "unitemized_convention_expenses",
                     "unitemized_other_disbursements", "total_communication_cost", "cash_on_hand_beginning_of_year",
                     "cash_on_hand_closing_of_year", "organization_type"]
	table_column_types["committees"] = ['TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT',
                          'TEXT', 'TEXT', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                          'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                          'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                          'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                          'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                          'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                          'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                          'REAL', 'REAL', 'REAL', 'TEXT']
	iterator["committees"] = iterate_list(list_of_committees)





	iterator["donations"] = donation_scanner.read_line(working_directory)

	missing_tables = find_missing_database_tables(working_directory)
	database_filepath = os.path.join(working_directory, "elections.db")
	if not os.path.exists(database_filepath):
		print("Database not found, about to create it.")
		connection = sqlite3.connect(database_filepath)
	for table in missing_tables:
		if table == "donations":
			load_donation_data_into_database(working_directory, iterator["donations"])
		else:
			load_data_into_database_generalized(working_directory, table, table_columns[table], table_column_types[table],
		                                    iterator[table])
	return True


def create_database(working_directory):
	print("Creating database...")
	database = os.path.join(working_directory, "donation_database.db")
	connection = sqlite3.connect(database)
	table_creation_statement = "CREATE TABLE donations (committee_id text, amendment_indicator text, report_type text, " \
	                           "primary_general_indicator text, image_number text, transaction_type text, " \
	                           "entity_type text, name text, city text, state text, zip code text, employer text, " \
	                           "occupation text, date text, amount text, other_identification_number text, " \
	                           "transaction_ID text, report_ID text, memo_code text, memo_text text, " \
	                           "FEC_record_number text) "
	print(table_creation_statement)
	cursor = connection.cursor()
	cursor.execute(table_creation_statement)
	connection.commit()
	connection.close()


def load_donation_data_into_database(working_directory, donation_iterator):
	if not database_table_does_exist(working_directory, "donations"):
		create_database(working_directory)
	table_columns = ["committee_id", "amendment_indicator", "report_type", "primary_general_indicator",
	                 "image_number", "transaction_type", "entity_type", "name", "city", "state",
	                 "zip code", "employer", "occupation", "date", "amount", "other_identification_number",
	                 "transaction_ID", "report_ID", "memo_code", "memo_text", "" "FEC_record_number"]
	table_column_types = ["TEXT", "TEXT", "TEXT", "TEXT", "INTEGER", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "INTEGER",
	                      "TEXT", "TEXT", "INTEGER", "INTEGER", "INTEGER", "TEXT", "TEXT", "TEXT", "TEXT", "INTEGER"]
	database = os.path.join(working_directory, "elections.db")
	connection = sqlite3.connect(database)
	cursor = connection.cursor()
	table_creation_statement = f"CREATE TABLE donations ({table_columns[0]} {table_column_types[0]}"
	for index in range(1, len(table_columns)):
		table_creation_statement = table_creation_statement + ", " + table_columns[index] + " " \
		                           + table_column_types[index]
	table_creation_statement = table_creation_statement + ");"
	print(table_creation_statement)
	cursor.execute(table_creation_statement)
	connection.commit()
	for donation in donation_iterator:
		for key in table_columns:
			if key not in donation.keys():
				donation[key] = ''
			donation[key] = donation[key].replace("'", "")
		line_insertion_statement = "INSERT INTO donations VALUES ('" + donation['committee_id'] + "', '" \
		                           + donation['amendment_indicator'] + "', '" + donation['report_type'] + "', '" \
									+ donation['primary-general_indicator'] + "', '" + donation['image_number'] \
									+ "', '" + donation['transaction_type'] + "', '" + donation['entity_type'] \
									+ "', '" + donation['name'] + "', '" + donation['city'] + "', '" \
									+ donation['state'] + "', '" + donation['zip code'] + "', '" \
									+ donation['employer'] + "', '" + donation['occupation'] + "', '" \
									+ donation['date'] + "', '" + donation['amount'] + "', '" \
									+ donation['other_identification_number'] + "', '" + donation['transaction_ID'] \
									+ "', '" + donation['report_ID'] + "', '" + donation['memo_code'] + "', '" \
									+ donation['memo_text'] + "', '" + donation['FEC_record_number'] + "')"
		cursor.execute(line_insertion_statement)
	connection.commit()
	connection.close()
	return True


def sanitize_data(line, column, table_name):
	new_value = getattr(line, column)
	if column != "name" and column != "treasurers_name":
		if column not in list(vars(line).keys()):
			new_value = ''
		if column != "FEC_web_link":
			try:
				new_value = ''.join([character for character in getattr(line, column) if character.isalpha()])
			except TypeError:
				new_value = 0
	if column == "name" or column == "treasurers_name":
		name = getattr(line, column)
		name = name.replace(',', '').replace('\'', '')
		if table_name == "candidates":
			names = name.split(" ")
			new_name = ""
			for index in range(1, len(names)):
				new_name = new_name + names[index] + " "
			new_name = new_name + names[0]
			new_value = new_name
		else:
			new_value = name
	print(f"{column}: {getattr(line, column)}")
	return new_value


def load_data_into_database_generalized(working_directory, table_name, table_columns, table_column_types, iterator):
	print(f"Creating {table_name} table...")
	database = os.path.join(working_directory, "elections.db")
	connection = sqlite3.connect(database)
	cursor = connection.cursor()
	table_creation_statement = f"CREATE TABLE {table_name} ({table_columns[0]} {table_column_types[0]}"
	for index in range(1, len(table_columns)):
		table_creation_statement = table_creation_statement + ", " + table_columns[index] + " " + table_column_types[index]
	table_creation_statement = table_creation_statement + ");"
	print(table_creation_statement)
	cursor.execute(table_creation_statement)
	connection.commit()
	for line in iterator:
		print(line)
		for column in table_columns:
			new_value = sanitize_data(line, column, table_name)
			setattr(line, column, new_value)
		line_insertion_statement = "INSERT INTO " + table_name + " VALUES ('" + str(getattr(line, table_columns[0]))
		for column_index in range(1, len(table_columns)):
			line_insertion_statement = line_insertion_statement + "', '" + str(getattr(line, table_columns[column_index]))
		line_insertion_statement = line_insertion_statement + "')"
		print(line_insertion_statement)
		cursor.execute(line_insertion_statement)
	connection.commit()
	connection.close()
	return True


def table_does_exist(working_directory, table_name):
	database = os.path.join(working_directory, "donation_database.db")
	try:
		connection = sqlite3.connect(database)
		connection.execute("select * from " + table_name)
		connection.close()
		print("Table found")
		return True
	except:
		print("Database not found")
		return False


def create_table(working_directory, table_name, table_columns, table_column_types):
	print("Creating database...")
	database = os.path.join(working_directory, "donation_database.db")
	connection = sqlite3.connect(database)
	table_creation_statement = "CREATE TABLE donations (committee_id text, amendment_indicator text, report_type text, " \
	                           "primary_general_indicator text, image_number text, transaction_type text, " \
	                           "entity_type text, name text, city text, state text, zip code text, employer text, " \
	                           "occupation text, date text, amount text, other_identification_number text, " \
	                           "transaction_ID text, report_ID text, memo_code text, memo_text text, " \
	                           "FEC_record_number text) "
	print(table_creation_statement)
	cursor = connection.cursor()
	cursor.execute(table_creation_statement)
	connection.commit()
	connection.close()