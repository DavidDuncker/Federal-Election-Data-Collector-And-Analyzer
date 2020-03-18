def do_the_names_match(campaign, candidate):
	name_from_campaign_data = campaign.name.replace(",", "").replace(".", "").split(" ")
	name_from_candidate_data = candidate.name.replace(",", "").replace(".", "").split(" ")
	if len(name_from_campaign_data) < 2 or len(name_from_candidate_data) < 2:
		return False
	if campaign.office == "P":
		first_names_match = (name_from_campaign_data[0].upper() in name_from_candidate_data[0].upper() )
		last_names_match = (name_from_campaign_data[1].upper() in name_from_candidate_data[1].upper() )
		names_match = first_names_match and last_names_match
	elif campaign.office != "P":
		first_names_match = (name_from_campaign_data[0].upper() in name_from_candidate_data[1].upper())
		last_names_match = (name_from_campaign_data[len(name_from_campaign_data) - 1].upper() in name_from_candidate_data[0].upper())
		names_match = first_names_match and last_names_match
	return names_match


def are_the_names_close(campaign, candidate):
	name_from_campaign_data = campaign.name.replace(",", "").replace(".", "").lower()
	name_from_candidate_data = candidate.name.replace(",", "").replace(".", "").lower()
	if len(name_from_campaign_data) < 2 or len(name_from_candidate_data) < 2:
		return False
	if name_from_campaign_data[0:3] in name_from_candidate_data:
		return True
	return False


def do_the_years_match(campaign, candidate):
	return campaign.year == candidate.year


def do_the_offices_match(campaign, candidate):
	return campaign.office == candidate.office


def do_the_parties_match(campaign, candidate):
	return campaign.party == candidate.party


def do_the_states_match(campaign, candidate):
	return (campaign.state == candidate.state) or (campaign.office == "P")


def do_the_districts_match(campaign, candidate):
	if campaign.office == "H":
		return campaign.district == candidate.district
	else:
		return True


def does_everything_match(names_do_match, years_do_match, offices_do_match, districts_do_match, states_do_match):
	return names_do_match and years_do_match and offices_do_match and districts_do_match and states_do_match


def update_data(campaign, campaign_number, candidate, candidate_number, candidate_and_committee_map):
	campaign.candidate_id = candidate.id
	campaign.candidate_index = candidate_number
	#print(f"Campaign name: {campaign.name}; Candidate name: {candidate.name}; Year: {campaign.year},{candidate.year}; "
	#      f"Candidate ID: {candidate.id}")
	try:
		campaign.committee_id = candidate_and_committee_map[candidate.id][str(campaign.year)][0]
		campaign.committee_index = candidate_and_committee_map[candidate.id][str(campaign.year)][1]
		candidate.campaign_indices.append(campaign_number)
		candidate.committee_ids.update({str(campaign.year):
		                                [candidate_and_committee_map[candidate.id][str(campaign.year)][0],
		                                 candidate_and_committee_map[candidate.id][str(campaign.year)][1]]}
	                               )
	except KeyError:
		pass
	return campaign, candidate


def link_campaigns_candidates_and_committees_together(list_of_campaigns, list_of_candidates, list_of_committees):
	print("Cross-linking data between campaigns, candidates, and committees")
	candidate_to_committee_map, committee_to_candidate_map = create_map_between_candidates_and_committees(list_of_committees)
	edge_cases = []
	for campaign_number in range(0, len(list_of_campaigns)):
		if campaign_number % 200 == 0:
			print(f"Working on campaign number {campaign_number} / {len(list_of_campaigns)}")
		for candidate_number in range(0, len(list_of_candidates)):
			names_do_match = do_the_names_match(list_of_campaigns[campaign_number], list_of_candidates[candidate_number])
			names_are_close = are_the_names_close(list_of_campaigns[campaign_number], list_of_candidates[candidate_number])
			years_do_match = do_the_years_match(list_of_campaigns[campaign_number], list_of_candidates[candidate_number])
			parties_do_match = do_the_parties_match(list_of_campaigns[campaign_number], list_of_candidates[candidate_number])
			offices_do_match = do_the_offices_match(list_of_campaigns[campaign_number], list_of_candidates[candidate_number])
			states_do_match = do_the_states_match(list_of_campaigns[campaign_number], list_of_candidates[candidate_number])
			districts_do_match = do_the_districts_match(list_of_campaigns[campaign_number], list_of_candidates[candidate_number])
			everything_matches = does_everything_match(names_do_match, years_do_match,
			                                           offices_do_match, districts_do_match, states_do_match)
			level_of_matching = names_do_match + years_do_match + parties_do_match + offices_do_match \
			                    + states_do_match + districts_do_match
			if everything_matches:
				print(list_of_campaigns[campaign_number])
				print(list_of_candidates[candidate_number])
				list_of_campaigns[campaign_number], list_of_candidates[candidate_number] = \
					update_data(list_of_campaigns[campaign_number], campaign_number, list_of_candidates[candidate_number],
							candidate_number, candidate_to_committee_map)
			elif names_are_close and level_of_matching >= 3:
				edge_cases.append([list_of_campaigns[campaign_number], list_of_candidates[candidate_number]])
	return list_of_campaigns, list_of_candidates, edge_cases, candidate_to_committee_map, committee_to_candidate_map


def create_map_between_candidates_and_committees(list_of_committees):
	print("Creating map between candidates and committees for faster computation")
	candidate_to_committee_map = {}
	committee_to_candidate_map = {}
	for committee_index in range(0, len(list_of_committees)):
		if committee_index % 200 == 0:
			print(f"Working on committee number {committee_index} / {len(list_of_committees)}")
		committee = list_of_committees[committee_index]
		year = str(committee.election_year)
		candidate_id = committee.candidate_id
		committee_id = committee.committee_id
		if len(candidate_id) < 4:
			continue
		committee_to_candidate_map[committee_id] = candidate_id
		try:
			candidate_to_committee_map[candidate_id][year] = [committee_id, committee_index]
		except KeyError:
			candidate_to_committee_map[candidate_id] = {}
			candidate_to_committee_map[candidate_id][year] = [committee_id, committee_index]
	return candidate_to_committee_map, committee_to_candidate_map


def display_random_edge_case(edge_cases):
	from random import randint
	q = randint(0, len(edge_cases))
	print(f"Name: {edge_cases[q][0].name},{edge_cases[q][1].name};\n"
	      f"Office: {edge_cases[q][0].office},{edge_cases[q][1].office};\n"
	      f"District: {edge_cases[q][0].district},{edge_cases[q][1].district};\n"
	      f"State: {edge_cases[q][0].state},{edge_cases[q][1].state};\n"
	      f"Party: {edge_cases[q][0].party},{edge_cases[q][1].party};\n"
	      f"Year: {edge_cases[q][0].year},{edge_cases[q][1].year};\n")
	return True
