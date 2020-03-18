import pickle
import os


def save_data(working_directory, filename, object):
	directory = os.path.join(working_directory, "saved_data/")
	if not os.path.exists(directory):
		os.makedirs(directory)
	savefile_path = os.path.join(working_directory, "saved_data/" + filename)
	savefile = open(savefile_path, 'wb')
	pickle.dump(object, savefile)
	savefile.close()
	return True


def check_for_saved_data(working_directory, filename):
	filepath = os.path.join(working_directory, "saved_data/" + filename)
	if os.path.exists(filepath):
		return True
	return False


def save_all_data(working_directory, all_data):
	list_of_campaigns = all_data[0]
	list_of_candidates = all_data[1]
	edge_cases = all_data[2]
	candidate_to_committee_map = all_data[3]
	committee_to_candidate_map = all_data[4]
	list_of_committees = all_data[5]
	save_data(working_directory, "list_of_campaigns.data", list_of_campaigns)
	save_data(working_directory, "list_of_candidates.data", list_of_candidates)
	save_data(working_directory, "edge_cases.data", edge_cases)
	save_data(working_directory, "candidate_to_committee_map.data", candidate_to_committee_map)
	save_data(working_directory, "committee_to_candidate_map.data", committee_to_candidate_map)
	save_data(working_directory, "list_of_committees.data", list_of_committees)
	return True


def all_saved_data_exists(working_directory):
	saved_data_exists = (check_for_saved_data(working_directory, "list_of_campaigns.data")
	                     and check_for_saved_data(working_directory, "list_of_candidates.data")
	                     and check_for_saved_data(working_directory, "edge_cases.data")
	                     and check_for_saved_data(working_directory, "candidate_to_committee_map.data")
	                     and check_for_saved_data(working_directory, "committee_to_candidate_map.data")
	                     and check_for_saved_data(working_directory, "list_of_committees.data")
	                     )
	return saved_data_exists

def load_saved_data(working_directory, filename):
	filepath = os.path.join(working_directory, "saved_data/" + filename)
	file = open(filepath, 'rb')
	object = pickle.load(file)
	file.close()
	return object
