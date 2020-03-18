import sqlite3
import sys
import os

import data_crossmap
import downloader
import read_file
import campaign
import candidate
import committee
import save_data
import donation_scanner
import check_if_candidate_and_campaign_match
import sqlite_manager

# Get working directory - with user input
# directory_path = os.path.dirname(os.path.realpath(__file__))
directory_path = os.getcwd()
sys.path.append(directory_path)

working_directory = input(f"Current working directory is {directory_path}. "
                          f"\nPress Enter to accept, \nor type in new working directory for storing election data")
if working_directory == "":
    working_directory = directory_path

saved_data_exists = (save_data.check_for_saved_data(working_directory, "list_of_campaigns.data")
                     and save_data.check_for_saved_data(working_directory, "list_of_candidates.data")
                     and save_data.check_for_saved_data(working_directory, "edge_cases.data")
                     and save_data.check_for_saved_data(working_directory, "candidate_to_committee_map.data")
                     and save_data.check_for_saved_data(working_directory, "committee_to_candidate_map.data")
                     and save_data.check_for_saved_data(working_directory, "list_of_committees.data")
                     )
if saved_data_exists:
    print("Detected saved data")
    list_of_campaigns = save_data.load_saved_data(working_directory, "list_of_campaigns.data")
    list_of_candidates = save_data.load_saved_data(working_directory, "list_of_candidates.data")
    edge_cases = save_data.load_saved_data(working_directory, "edge_cases.data")
    candidate_to_committee_map = save_data.load_saved_data(working_directory, "candidate_to_committee_map.data")
    committee_to_candidate_map = save_data.load_saved_data(working_directory, "committee_to_candidate_map.data")
    list_of_committees = save_data.load_saved_data(working_directory, "list_of_committees.data")


elif not saved_data_exists:
    print("Did not detect saved data, reloading data")
    # Check for necessary files and download them
    print("Checking for Federal Election Commission files")
    downloader.download_data(working_directory)
    print("Reading election files and creating data structures")
    # Create list of election campaign objects
    list_of_campaigns = campaign.read_election_data(working_directory)
    list_of_candidates = candidate.read_candidate_data(working_directory)
    list_of_committees = committee.read_committee_data(working_directory)
    # Cross-link the data
    print("Crosslinking all the data files together")
    list_of_campaigns, list_of_candidates, edge_cases, candidate_to_committee_map, committee_to_candidate_map = \
        data_crossmap.link_campaigns_candidates_and_committees_together(list_of_campaigns, list_of_candidates,
                                                                        list_of_committees)
    print("Saving the data structures")
    all_data = [list_of_campaigns, list_of_candidates, edge_cases, candidate_to_committee_map,
              committee_to_candidate_map, list_of_committees]
    save_data.save_all_data(working_directory, all_data)

print("About to check database status")
sqlite_manager.create_all_database_tables(working_directory, list_of_committees, list_of_candidates, list_of_campaigns)
import sqlite3
database_file = "/home/dave/PycharmProjects/FECD-EOVT/elections.db"
connection = sqlite3.connect(database_file)
cursor = connection.cursor()
statement1 = "select name from sqlite_master where type = 'table';"


def get_col_names(tablename):
    conn = sqlite3.connect("/home/dave/PycharmProjects/FECD-EOVT/elections.db")
    c = conn.cursor()
    c.execute("select * from " + tablename)
    return [member[0] for member in c.description]
