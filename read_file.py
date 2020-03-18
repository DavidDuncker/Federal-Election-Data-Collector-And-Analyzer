#!/usr/bin/python3
import os
import codecs


def get_delimiter(delimited_file):
    delimited_data_columns = []
    delimiter = ""
    if "1976-2016-president.tab" in delimited_file:
        delimited_data_columns = ['year', 'state', 'state_po', 'state_fips', 'state_cen', 'state_ic', 'office',
                                  'name', 'party', 'writein', 'candidatevotes', 'totalvotes', 'version', 'notes']
        delimiter = "\t"
    elif "1976-2018-senate.tab" in delimited_file:
        delimited_data_columns = ['year', 'state', 'state_po', 'state_fips', 'state_cen', 'state_ic', 'office',
                                  'district', 'stage', 'special', 'name', 'party', 'writein', 'mode',
                                  'candidatevotes', 'totalvotes', 'unofficial', 'version']
        delimiter = "\t"
    elif "1976-2018-house.tab" in delimited_file:
        delimited_data_columns = ['year', 'state', 'state_po', 'state_fips', 'state_cen', 'state_ic',
                                  'office', 'district', 'stage', 'runoff', 'special', 'name', 'party',
                                  'writein', 'mode', 'candidatevotes', 'totalvotes', 'unofficial', 'version']
        delimiter = "\t"
    elif "candidate_summary_20" in delimited_file:
        delimited_data_columns = ['FEC_web_link', 'name', 'id', 'office', 'state', 'district', 'party',
                                  'Cand_Incumbent_Challenger_Open_Seat', 'receipts', 'disbursement',
                                  'cash_on_hand', 'Debt_Owed_By_Committee', 'Coverage_End_Date', 'Cand_Street_1',
                                  'Cand_Street_2', 'city', 'state', 'zip_code', 'Individual_Itemized_Contribution',
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
        delimiter = "\",\""
    elif "committee_summary_20" in delimited_file:
        delimited_data_columns = ["link_to_committee_profle_page", "committee_id", "name", "committee_type",
                                  "committee_designation", "filing_frequency", "address_1", "address_2", "city",
                                  "state", "zip_code", "treasurers_name", "candidate_id", "election_year",
                                  "individual_contribution", "party_committee_contribution",
                                  "other_committee_contribution", "total_contribution",
                                  "transfer_from_other_authorized_committee", "offsets_to_operating_expenditure",
                                  "other_receipts", "total_receipts", "transfer_to_other_authorized_committee",
                                  "other_loan_repayment", "individual_refund", "political_party_committee_refund",
                                  "total_contribution_refund", "other_disbursement", "total_disbursement",
                                  "net_contribution", "net_operating_expenditure", "cash_on_hand_beginning_of_period",
                                  "coverage_start_date", "cash_on_hand_closing_of_period", "coverage_end_date",
                                  "debt_owed_by_committee", "debt_owed_to_committee",
                                  "individual_itemized_contribution", "individual_unitemized_contribution",
                                  "other_loan", "transfer_from_non_federal_account",
                                  "transfer_from_non_federal_levin_account", "total_nnon_federal_transfer",
                                  "loan_repayments_received", "offsets_to_fundraising_expenses_presidential_only",
                                  "offsets_to_legalaccounting_expenses_presidential_only",
                                  "federal_candidate_contribution_refund", "total_federal_receipt",
                                  "shared_federal_operating_expenditure", "shared_nonfederal_operating_expenditure",
                                  "other_federal_operating_expenditures", "total_operating_expenditure",
                                  "federal_candidate_committee_contribution", "independent_expenditures_made",
                                  "coordinated_expenditure_party_only", "loan_made",
                                  "federal_share_of_joint_federal_election_activity",
                                  "nonfederal_share_of_joint_federal_election_activity",
                                  "nonallocated_federal_election_activity_party_only",
                                  "total_federal_election_activity", "total_federal_disbursement",
                                  "candidate_contribution", "candidate_loan", "total_loan", "operating_expenditure",
                                  "candidate_loan_repayment", "total_loan_repayment", "other_committee_refund",
                                  "total_offsets_to_operating_expenditure",
                                  "exempt_legalaccounting_disbursement_presidential_only", "fundraising_disbursement",
                                  "itemized_refunds_or_rebates", "subtotal_refunds_or_rebates",
                                  "unitemized_refunds_or_rebates", "itemized_other_refunds_or_rebates",
                                  "unitemized_other_refunds_or_rebates", "subtotal_other_refunds_or_rebates",
                                  "itemized_other_income", "unitemized_other_income",
                                  "expenditures_subject_to_limit_prior_year_presidential_only",
                                  "expenditures_subject_to_limit", "federal_funds",
                                  "itemized_convention_expenditure_convention_committee_only",
                                  "itemized_other_disbursement", "subtotal_convention_expenses",
                                  "total_expenditures_subject_to_limit_presidential_only",
                                  "unitemized_convention_expenses", "unitemized_other_disbursements",
                                  "total_communication_cost", "cash_on_hand_beginning_of_year",
                                  "cash_on_hand_closing_of_year", "organization_type"]

        delimiter = "\",\""
    elif "donation_data_20" in delimited_file:
        delimited_data_columns = ['committee_id', 'amendment_indicator', 'report_type', 'primary-general_indicator',
                                  'image_number', 'transaction_type', 'entity_type', 'name', 'city',
                                  'state', 'zip code', 'employer', 'occupation', 'date', 'amount', 'other_identification_number',
                                  'transaction_ID', 'report_ID', 'memo_code', 'memo_text', 'FEC_record_number']
        delimiter = "|"
    return delimited_data_columns, delimiter


def read_line_data(line, text_delimiter, data_columns):
    line_data_values = line.split(text_delimiter)
    for line_data_value in line_data_values:
        line_data_value = line_data_value.replace("\"", "")
    dictionary_of_line_data = {}
    for i in range(0, len(data_columns)-1):
        dictionary_of_line_data.update({data_columns[i]: line_data_values[i]})
    return dictionary_of_line_data
 

def generate_line_data(working_directory, filename):
    file_path = os.path.join(working_directory, "working_data/" + filename)
    file = codecs.open(file_path, 'r', 'utf-8', errors='replace')
    number_of_lines = sum(1 for line in file)
    file.close()
    file = codecs.open(file_path, 'r', 'utf-8', errors='replace')
    print(file.readline())
    line_number = 1
    data_columns, text_delimiter = get_delimiter(filename)
    for line in file:
        line_number += 1
        dictionary_of_line_data = read_line_data(line, text_delimiter, data_columns)
        yield [dictionary_of_line_data, line_number, number_of_lines]
    file.close()
    return


def generate_line_data_as_generator(working_directory, filename):
    file_path = os.path.join(working_directory, "working_data/" + filename)
    file = open(file_path, 'r')
    number_of_lines = sum(1 for line in file)
    file.close()
    file = open(file_path, 'r')
    file.readline()
    line_number = 1
    data_columns, text_delimiter = get_delimiter(filename)
    for line in file:
        line_number += 1
        dictionary_of_line_data = read_line_data(line, text_delimiter, data_columns)
        yield [dictionary_of_line_data, line_number, number_of_lines]
    file.close()
    return



def read_election_data(working_directory, filename):
    from campaign import Campaign
    list_of_campaigns = []
    election_info = generate_line_data(working_directory, filename)
    for line in election_info:
        dictionary_of_line_data = line[0]
        line_number = line[1]
        number_of_lines = line[2]
        if line_number % 200 == 0:
            print("Reading line " + str(line_number) + " out of " + str(number_of_lines) + ".")
        campaign = Campaign(dictionary_of_line_data)
        list_of_campaigns.append(campaign)
    return list_of_campaigns


def generate_list_of_candidate_files(working_directory):
    # Candidate files
    candidate_files = []
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2020.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2018.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2016.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2014.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2012.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2010.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2008.csv")
    candidate_files.append(file_)

    return candidate_files


def read_candidate_data(filename):
    from campaign import Campaign
    list_of_candidates = []
    for line in generate_line_data(filename):
        dictionary_of_line_data = line[0]
        line_number = line[1]
        number_of_lines = line[2]
        if line_number % 200 == 0:
            print("Reading line " + str(line_number) + " out of " + str(number_of_lines) + ".")
        list_of_candidates.append(dictionary_of_line_data)
    return list_of_candidates


def generate_list_of_required_files(working_directory):
    # Candidate files
    candidate_files = []
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2020.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2018.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2016.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2014.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2012.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2010.csv")
    candidate_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/candidate_summary_2008.csv")
    candidate_files.append(file_)

    # Election committee file lists
    committee_files=[]
    file_ = os.path.join(working_directory, "working_data/committee_summary_2020.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2018.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2016.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2014.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2012.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2010.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2008.csv")
    committee_files.append(file_)

    # Election results
    election_files=[]
    file_ = os.path.join(working_directory, "working_data/1976-2016-president.tab")
    election_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/1976-2018-senate.tab")
    election_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/1976-2018-house.tab")
    election_files.append(file_)

    # Donation files
    donation_files = []
    file_ = os.path.join(working_directory, "working_data/donation_data_2008")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2010")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2012")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2014")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2016")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2018")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2020")
    election_files.append(file_)

    return candidate_files, committee_files, election_files, donation_files


def generate_list_of_committee_files(working_directory):
    # Election committee file lists
    committee_files = []
    file_ = os.path.join(working_directory, "working_data/committee_summary_2020.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2018.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2016.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2014.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2012.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2010.csv")
    committee_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/committee_summary_2008.csv")
    committee_files.append(file_)
    return committee_files


def generate_list_of_election_files(working_directory):
    # Election results
    election_files = []
    file_ = os.path.join(working_directory, "working_data/1976-2016-president.tab")
    election_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/1976-2018-senate.tab")
    election_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/1976-2018-house.tab")
    election_files.append(file_)
    return election_files


def generate_list_of_donation_files(working_directory):
    # Donation files
    donation_files = []
    file_ = os.path.join(working_directory, "working_data/donation_data_2008")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2010")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2012")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2014")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2016")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2018")
    donation_files.append(file_)
    file_ = os.path.join(working_directory, "working_data/donation_data_2020")
    donation_files.append(file_)

    return donation_files

