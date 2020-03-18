import os

import read_file


def convert_state_format(state_name):
    sanitized_state_name = state_name.replace('"', '').replace("'", '').replace(' ', '').upper()
    conversion_dictionary = {'ALABAMA': 'AL', 'ALASKA': 'AK', 'ARIZONA': 'AZ', 'ARKANSAS': 'AR', 'CALIFORNIA': 'CA',
                             'COLORADO': 'CO', 'CONNECTICUT': 'CT', 'DELAWARE': 'DE', 'FLORIDA': 'FL', 'GEORGIA': 'GA',
                             'HAWAII': 'HI', 'IDAHO': 'ID', 'ILLINOIS': 'IL', 'INDIANA': 'IN', 'IOWA': 'IA',
                             'KANSAS': 'KS', 'KENTUCKY': 'KY', 'LOUISIANA': 'LA', 'MAINE': 'ME', 'MARYLAND': 'MD',
                             'MASSACHUSETTS': 'MA', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN', 'MISSISSIPPI': 'MS',
                             'MISSOURI': 'MO', 'MONTANA': 'MT', 'NEBRASKA': 'NE', 'NEVADA': 'NV', 'NEWHAMPSHIRE': 'NH',
                             'NEWJERSEY': 'NJ', 'NEWMEXICO': 'NM', 'NEWYORK': 'NY', 'NORTHCAROLINA': 'NC',
                             'NORTHDAKOTA': 'ND', 'OHIO': 'OH', 'OKLAHOMA': 'OK', 'OREGON': 'OR', 'PENNSYLVANIA': 'PA',
                             'RHODEISLAND': 'RI', 'SOUTHCAROLINA': 'SC', 'SOUTHDAKOTA': 'SD', 'TENNESSEE': 'TN',
                             'TEXAS': 'TX', 'UTAH': 'UT', 'VERMONT': 'VT', 'VIRGINIA': 'VA', 'WASHINGTON': 'WA',
                             'WESTVIRGINIA': 'WV', 'WISCONSIN': 'WI', 'WYOMING': 'WY'}
    return conversion_dictionary[sanitized_state_name]


def sanitize_line_data(dictionary_of_line_data):
    dictionary_of_line_data['office'] = dictionary_of_line_data['office'][4]
    dictionary_of_line_data['candidatevotes'] = int(dictionary_of_line_data['candidatevotes'].replace('"', '').replace(',', ''))
    dictionary_of_line_data['name'] = dictionary_of_line_data['name'].replace('"', '')
    dictionary_of_line_data['party'] = dictionary_of_line_data['party'].replace('"', '')
    try:
        dictionary_of_line_data['party'] = dictionary_of_line_data['party'][0].upper()
    except IndexError:
        pass
    dictionary_of_line_data['state'] = dictionary_of_line_data['state_po'].replace('"', '')
    dictionary_of_line_data['state_cen'] = int(dictionary_of_line_data['state_cen'])
    dictionary_of_line_data['state_fips'] = int(dictionary_of_line_data['state_fips'])
    dictionary_of_line_data['state_ic'] = int(dictionary_of_line_data['state_ic'].replace('\'', ''))
    try:
        dictionary_of_line_data['totalvotes'] = int(dictionary_of_line_data['totalvotes'].replace('\'', ''))
    except ValueError:
        dictionary_of_line_data['totalvotes'] = int(round(float(dictionary_of_line_data['totalvotes'])))
    dictionary_of_line_data['year'] = int(dictionary_of_line_data['year'])
    if "district" in dictionary_of_line_data.keys():
        if dictionary_of_line_data['district'] == "00" or dictionary_of_line_data['district'] == '"statewide"':
            dictionary_of_line_data['district'] = ""
    elif "district" not in dictionary_of_line_data.keys():
        dictionary_of_line_data['district'] = ""
    return dictionary_of_line_data








def read_election_data(working_directory):
    files = ["1976-2016-president.tab",
             "1976-2018-senate.tab",
             "1976-2018-house.tab"]
    list_of_campaigns = []
    for file in files:
        election_info = read_file.generate_line_data(working_directory, file)
        for line in election_info:
            dictionary_of_line_data = line[0]
            dictionary_of_line_data = sanitize_line_data(dictionary_of_line_data)
            line_number = line[1]
            number_of_lines = line[2]
            if line_number % 200 == 0:
                print("Reading line " + str(line_number) + " out of " + str(number_of_lines) + ".")
            campaign = Campaign(dictionary_of_line_data)
            list_of_campaigns.append(campaign)
    return list_of_campaigns


class Campaign:
    year = ""
    state = ""
    state_po = ""
    state_fips = ""
    state_cen = ""
    state_ic = ""
    office = ""
    district = ""
    stage = ""
    runoff = ""
    special = ""
    name = ""
    party = ""
    writein = ""
    mode = ""
    candidatevotes = ""
    totalvotes = ""
    unofficial = ""
    version = ""
    notes = ""
    candidate_id = ""
    candidate_index = ""
    committee_id = ""
    committee_index = ""
    opponent_IDs = []
    number_of_donors = 0
    amount_of_donations = 0
    donation_breakdown = []
    opponents_number_of_donors = 0
    opponents_amount_of_donations = 0
    opponents_donation_breakdown = []

    def __init__(self, dictionary={}):
        list_of_keys = dictionary.keys()
        list_of_attributes = ['year', 'state', 'state_po', 'state_fips', 'state_cen', 'state_ic',
                                  'office', 'district', 'stage', 'runoff', 'special', 'name', 'party',
                                  'writein', 'mode', 'candidatevotes', 'totalvotes', 'unofficial', 'version', 'notes']
        for attribute in list_of_attributes:
            if attribute in list_of_keys:
                setattr(self, attribute, dictionary[attribute])

