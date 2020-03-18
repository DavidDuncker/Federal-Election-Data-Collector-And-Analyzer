def check_match(campaign, candidate):
	# Check if years match
	years_match = False
	if campaign.year == candidate.year:
		years_match = True

	# Check if states match
	states_match = False
	if campaign.state == candidate.state:
		states_match = True
	if campaign.office == "P":
		states_match = True

	# Check if parties match
	parties_match = False
	if campaign.party == candidate.party:
		parties_match = True

	# Check if offices match
	offices_match = False
	if campaign.office == candidate.office:
		offices_match = True

	# Check if names match
	names_match = False
	campaign_name = campaign.name.lower()
	campaign_name = campaign_name.replace(",", "").replace(".", "").split(" ")
	candidate_name = candidate.name.lower().replace(",", "").replace(".", "").split(" ")
	candidate_name = candidate_name.replace(",", "").replace(".", "").split(" ")
	if campaign.office == "P":
		if campaign_name[0] in candidate_name[0] and campaign_name[1] in candidate_name[1]:
			names_match = True
	if campaign.office != "P":
		if campaign_name[0] in candidate_name[1] and campaign_name[len(campaign_name) - 1] in candidate_name[0]:
			names_match = True

	if years_match and states_match and parties_match and offices_match and names_match:
		return True
	elif years_match and states_match and parties_match and offices_match:
		return 2
	else:
		return False
