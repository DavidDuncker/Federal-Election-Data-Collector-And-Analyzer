import read_file


def read_committee_data(working_directory):
    files = ["committee_summary_2020.csv", "committee_summary_2018.csv",
             "committee_summary_2016.csv", "committee_summary_2014.csv",
             "committee_summary_2012.csv", "committee_summary_2010.csv",
             "committee_summary_2008.csv"]

    list_of_committees = []
    for file in files:
        committee_info = read_file.generate_line_data(working_directory, file)
        for line in committee_info:
            dictionary_of_line_data = line[0]
            line_number = line[1]
            number_of_lines = line[2]
            if line_number % 200 == 0:
                print("Reading line " + str(line_number) + " out of " + str(number_of_lines) + ".")
            committee = Committee(dictionary_of_line_data)
            list_of_committees.append(committee)
    return list_of_committees


class Committee:
	FEC_web_link = ""
	committee_id = ""
	name = ""
	committee_type = ""
	committee_designation = ""
	filing_frequency = ""
	address_1 = ""
	address_2 = ""
	city = ""
	state = ""
	zip_code = ""
	treasurers_name = ""
	candidate_id = ""
	election_year = ""
	individual_contribution = ""
	party_committee_contribution = ""
	other_committee_contribution = ""
	total_contribution = ""
	transfer_from_other_authorized_committee = ""
	offsets_to_operating_expenditure = ""
	other_receipts = ""
	total_receipts = ""
	transfer_to_other_authorized_committee = ""
	other_loan_repayment = ""
	individual_refund = ""
	political_party_committee_refund = ""
	total_contribution_refund = ""
	other_disbursement = ""
	total_disbursement = ""
	net_contribution = ""
	net_operating_expenditure = ""
	cash_on_hand_beginning_of_period = ""
	coverage_start_date = ""
	cash_on_hand_closing_of_period = ""
	coverage_end_date = ""
	debt_owed_by_committee = ""
	debt_owed_to_committee = ""
	individual_itemized_contribution = ""
	individual_unitemized_contribution = ""
	other_loan = ""
	transfer_from_non_federal_account = ""
	transfer_from_non_federal_levin_account = ""
	total_nnon_federal_transfer = ""
	loan_repayments_received = ""
	offsets_to_fundraising_expenses_presidential_only = ""
	offsets_to_legalaccounting_expenses_presidential_only = ""
	federal_candidate_contribution_refund = ""
	total_federal_receipt = ""
	shared_federal_operating_expenditure = ""
	shared_nonfederal_operating_expenditure = ""
	other_federal_operating_expenditures = ""
	total_operating_expenditure = ""
	federal_candidate_committee_contribution = ""
	independent_expenditures_made = ""
	coordinated_expenditure_party_only = ""
	loan_made = ""
	federal_share_of_joint_federal_election_activity = ""
	nonfederal_share_of_joint_federal_election_activity = ""
	nonallocated_federal_election_activity_party_only = ""
	total_federal_election_activity = ""
	total_federal_disbursement = ""
	candidate_contribution = ""
	candidate_loan = ""
	total_loan = ""
	operating_expenditure = ""
	candidate_loan_repayment = ""
	total_loan_repayment = ""
	other_committee_refund = ""
	total_offsets_to_operating_expenditure = ""
	exempt_legalaccounting_disbursement_presidential_only = ""
	fundraising_disbursement = ""
	itemized_refunds_or_rebates = ""
	subtotal_refunds_or_rebates = ""
	unitemized_refunds_or_rebates = ""
	itemized_other_refunds_or_rebates = ""
	unitemized_other_refunds_or_rebates = ""
	subtotal_other_refunds_or_rebates = ""
	itemized_other_income = ""
	unitemized_other_income = ""
	expenditures_subject_to_limit_prior_year_presidential_only = ""
	expenditures_subject_to_limit = ""
	federal_funds = ""
	itemized_convention_expenditure_convention_committee_only = ""
	itemized_other_disbursement = ""
	subtotal_convention_expenses = ""
	total_expenditures_subject_to_limit_presidential_only = ""
	unitemized_convention_expenses = ""
	unitemized_other_disbursements = ""
	total_communication_cost = ""
	cash_on_hand_beginning_of_year = ""
	cash_on_hand_closing_of_year = ""
	organization_type = ""

	def __init__(self, dictionary={}):
		list_of_keys = dictionary.keys()
		list_of_attributes = ["link_to_committee_profle_page", "committee_id", "name", "committee_type",
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
                                  "shared_federal_operating_expenditure", "shared_non-federal_operating_expenditure",
                                  "other_federal_operating_expenditures", "total_operating_expenditure",
                                  "federal_candidate_committee_contribution", "independent_expenditures_made",
                                  "coordinated_expenditure_party_only", "loan_made",
                                  "federal_share_of_joint_federal_election_activity",
                                  "non-federal_share_of_joint_federal_election_activity",
                                  "non-allocated_federal_election_activity_party_only",
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

		for attribute in list_of_attributes:
			if attribute in list_of_keys:
				setattr(self, attribute, dictionary[attribute])
