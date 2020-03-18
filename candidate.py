import read_file


def sanitize_line_data(dictionary_of_line_data):
    dictionary_of_line_data['name'] = dictionary_of_line_data['name'].replace('"', '')
    dictionary_of_line_data['FEC_web_link'] = dictionary_of_line_data['FEC_web_link'].replace('"', '')
    if dictionary_of_line_data['district'] == "00" or dictionary_of_line_data['district'] == '"statewide"':
        dictionary_of_line_data['district'] = ""
    try:
        if dictionary_of_line_data['district'][0] == "0":
            dictionary_of_line_data['district'] = dictionary_of_line_data['district'][1:]
    except IndexError:
        pass

    # Need to convert a bunch of string-types into float-types to represent cash amounts,
    # but we need to be careful, since some of the data has an empty string in lieu of
    # the number zero
    list_of_strings_to_convert_to_floats = ['receipts', 'disbursement', 'cash_on_hand', 'Debt_Owed_By_Committee',
                                            'Individual_Itemized_Contribution', 'Individual_Unitemized_Contribution',
                                            'Individual_Contribution', 'Other_Committee_Contribution',
                                            'Party_Committee_Contribution', 'Cand_Contribution', 'Total_Contribution',
                                            'Transfer_From_Other_Auth_Committee', 'Cand_Loan', 'Other_Loan',
                                            'Total_Loan', 'Offsets_To_Operating_Expenditure', 'Offsets_To_Fundraising',
                                            'Offsets_To_Leagal_Accounting', 'Other_Receipts', 'Operating_Expenditure',
                                            'Exempt_Legal_Accounting_Disbursement', 'Fundraising_Disbursement',
                                            'Transfer_To_Other_Auth_Committee', 'Cand_Loan_Repayment',
                                            'Other_Loan_Repayment', 'Total_Loan_Repayment', 'Individual_Refund',
                                            'Party_Committee_Refund', 'Other_Committee_Refund',
                                            'Total_Contribution_Refund', 'Other_Disbursements', 'Net_Contribution',
                                            'Net_Operating_Expenditure', 'Cash_On_Hand_BOP', 'Debt_Owe_To_Committee']
    for string in list_of_strings_to_convert_to_floats:
        try:
            dictionary_of_line_data[string] = float(dictionary_of_line_data[string])
        except:
            pass
    try:
        dictionary_of_line_data['party'] = dictionary_of_line_data['party'][0].upper()
    except:
        pass
    return dictionary_of_line_data


def read_candidate_data(working_directory):
    files = ["candidate_summary_2020.csv", "candidate_summary_2018.csv",
             "candidate_summary_2016.csv", "candidate_summary_2014.csv",
             "candidate_summary_2012.csv", "candidate_summary_2010.csv",
             "candidate_summary_2008.csv"]

    list_of_candidates = []
    for file in files:
        year = file[18:22]
        candidate_info = read_file.generate_line_data(working_directory, file)
        for line in candidate_info:
            dictionary_of_line_data = line[0]
            dictionary_of_line_data = sanitize_line_data(dictionary_of_line_data)
            line_number = line[1]
            number_of_lines = line[2]
            if line_number % 200 == 0:
                print("Reading line " + str(line_number) + " out of " + str(number_of_lines) + ".")
            candidate = Candidate(dictionary_of_line_data)
            candidate.year = int(year)
            list_of_candidates.append(candidate)
    return list_of_candidates


class Candidate:
    year = ""
    FEC_web_link = ""
    name = ""
    id = ""
    office = ""
    state = ""
    district = ""
    party = ""
    Cand_Incumbent_Challenger_Open_Seat = ""
    receipts = ""
    disbursement = ""
    cash_on_hand = ""
    Debt_Owed_By_Committee = ""
    Coverage_End_Date = ""
    Cand_Street_1 = ""
    Cand_Street_2 = ""
    city = ""
    state = ""
    zip_code = ""
    Individual_Itemized_Contribution = ""
    Individual_Unitemized_Contribution = ""
    Individual_Contribution = ""
    Other_Committee_Contribution = ""
    Party_Committee_Contribution = ""
    Cand_Contribution = ""
    Total_Contribution = ""
    Transfer_From_Other_Auth_Committee = ""
    Cand_Loan = ""
    Other_Loan = ""
    Total_Loan = ""
    Offsets_To_Operating_Expenditure = ""
    Offsets_To_Fundraising = ""
    Offsets_To_Leagal_Accounting = ""
    Other_Receipts = ""
    Operating_Expenditure = ""
    Exempt_Legal_Accounting_Disbursement = ""
    Fundraising_Disbursement = ""
    Transfer_To_Other_Auth_Committee = ""
    Cand_Loan_Repayment = ""
    Other_Loan_Repayment = ""
    Total_Loan_Repayment = ""
    Individual_Refund = ""
    Party_Committee_Refund = ""
    Other_Committee_Refund = ""
    Total_Contribution_Refund = ""
    Other_Disbursements = ""
    Net_Contribution = ""
    Net_Operating_Expenditure = ""
    Cash_On_Hand_BOP = ""
    Debt_Owe_To_Committee = ""
    Coverage_Start_Date = ""
    candidate_id = ""
    committee_ids = {}
    campaign_indices = []
    opponent_IDs = []
    votes_earned = ""
    total_votes = ""
    number_of_donors = 0
    amount_of_donations = 0
    donation_breakdown = []
    opponents_number_of_donors = 0
    opponents_amount_of_donations = 0
    opponents_donation_breakdown = []

    def __init__(self, dictionary={}):
        list_of_keys = dictionary.keys()
        list_of_attributes = ['FEC_web_link', 'name', 'id', 'office', 'state', 'district', 'party',
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
        for attribute in list_of_attributes:
            if attribute in list_of_keys:
                setattr(self, attribute, dictionary[attribute])

