def FECDEOVT_download_data(working_directory):
 import os
 import requests
 import zipfile
 import sys
 individual_file_URIs=[]
 individual_file_names=[]
 #Donation file lists
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2020/indiv20.zip")
 individual_file_names.append("indiv20.zip")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2018/indiv18.zip")
 individual_file_names.append("indiv18.zip")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2016/indiv16.zip")
 individual_file_names.append("indiv16.zip")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2014/indiv14.zip")
 individual_file_names.append("indiv14.zip")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2012/indiv12.zip")
 individual_file_names.append("indiv12.zip")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2010/indiv10.zip")
 individual_file_names.append("indiv10.zip")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2008/indiv08.zip")
 individual_file_names.append("indiv08.zip")
 #Candidate file lists
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2020/candidate_summary_2020.csv")
 individual_file_names.append("candidate_summary_2020.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2018/candidate_summary_2018.csv")
 individual_file_names.append("candidate_summary_2018.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2016/candidate_summary_2016.csv")
 individual_file_names.append("candidate_summary_2016.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2014/candidate_summary_2014.csv")
 individual_file_names.append("candidate_summary_2014.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2012/candidate_summary_2012.csv")
 individual_file_names.append("candidate_summary_2012.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2010/candidate_summary_2010.csv")
 individual_file_names.append("candidate_summary_2010.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2008/candidate_summary_2008.csv")
 individual_file_names.append("candidate_summary_2008.csv")
 #Election committee file lists
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2020/committee_summary_2020.csv")
 individual_file_names.append("committee_summary_2020.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2018/committee_summary_2018.csv")
 individual_file_names.append("committee_summary_2018.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2016/committee_summary_2016.csv")
 individual_file_names.append("committee_summary_2016.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2014/committee_summary_2014.csv")
 individual_file_names.append("committee_summary_2014.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2012/committee_summary_2012.csv")
 individual_file_names.append("committee_summary_2012.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2010/committee_summary_2010.csv")
 individual_file_names.append("committee_summary_2010.csv")
 individual_file_URIs.append("https://www.fec.gov/files/bulk-downloads/2008/committee_summary_2008.csv")
 individual_file_names.append("committee_summary_2008.csv")
 #Presidential election results
 individual_file_URIs.append("https://dataverse.harvard.edu/api/access/datafile/3444051?format=tab&gbrecs=true")
 individual_file_names.append("1976-2016-president.tab")
 #Senate election results
 individual_file_URIs.append("https://dataverse.harvard.edu/api/access/datafile/3440424?format=tab&gbrecs=true")
 individual_file_names.append("1976-2018-senate.tab")
 #House election Results
 individual_file_URIs.append("https://dataverse.harvard.edu/api/access/datafile/3561497?format=tab&gbrecs=true")
 individual_file_names.append("1976-2018-house.tab")
 
 for i in range(0, len(individual_file_URIs) ):
  URI=individual_file_URIs[i]
  filename=individual_file_names[i]
  file_path=os.path.join(working_directory,"working_data/" + filename)
  directory=os.path.join(working_directory,"working_data/")
  if not os.path.exists(directory):
   os.makedirs(directory)
  
  print("Downloading and saving file "+str(i)+"/"+str(len(individual_file_URIs))+":")
  print(filename)
  print(URI)
  print("to file: "+file_path)
  f=open(file_path,'wb')
  r=requests.get(URI, stream=True)
  total_length = r.headers.get('content-length')
  if total_length is None: # no content length header
   f.write(r.content)
   print("No content length header")
  else:
   dl = 0
   total_length = int(total_length)
   for data in r.iter_content(chunk_size=4096):
    dl += len(data)
    f.write(data)
    done = int(50 * dl / total_length)
    sys.stdout.write("\r[%s%s] %s" % ('=' * done, ' ' * (50-done), str(round(dl/total_length*100,1))+"%" ) )   
    sys.stdout.flush()
  f.close()
  print("\n")
  
  if filename[0:5]=='indiv' and filename[-3:]=='zip':
   new_unzipped_filepath= os.path.join(working_directory,"working_data/donation_data_20"+filename[5:7])
   print("Unzipping data from "+filename+" to "+new_unzipped_filepath)
   f=open(new_unzipped_filepath,'wb')
   z=zipfile.ZipFile(file_path,'r')
   f.write( z.read("itcont.txt") )
   f.close()
   z.close()
   os.remove(file_path)
    
  print("\n\n")
 return True


def FECDEOVT_read_election_data(working_directory):
 import os
 import sys
 election_campaign_data=[]
 problematic_data=[]
 data_files=[]
 data_files.append( os.path.join(working_directory,"working_data/1976-2016-president.tab") )
 data_files.append( os.path.join(working_directory,"working_data/1976-2018-senate.tab") )
 data_files.append( os.path.join(working_directory,"working_data/1976-2018-house.tab") )
 for _file in data_files:
  if not os.path.isfile( os.path.join(working_directory,_file) ):
   print("Error: File "+_file+" not found")
   return False
 for _file in data_files:
  f=open( os.path.join(working_directory,_file) ,'r')
  f.readline()
  
  if "house" in _file:
   for line in f:
     try:
      print(line)
      line_data=line.replace("\"","").split("\t")
      year=int(line_data[0])
      state=line_data[2]
      party=line_data[12]
      office=line_data[6][3:4]
      district=line_data[7]
      name=line_data[11]
      votes_earned=int( line_data[15].replace(",","") )
      total_votes=int( line_data[16].replace(",","") )
      if total_votes>1 and votes_earned/total_votes>0.01: #Must be careful about vote recounts and other such data distorting quirks
       election_campaign_data.append( 
	{"year":year, 
	"state":state, 
	"party":party, 
	"office":office, 
	"district":district,
	"name":name, 
	"votes_earned":votes_earned, 
	"total_votes":total_votes } )
      else:
       problematic_data.append(line)
     except:
      problematic_data.append(line)
      continue
      #print(sys.exc_info())
  
  elif "senate" in _file:
   for line in f:
     try:
      line_data=line.replace("\"","").split("\t")
      year=int(line_data[0])
      state=line_data[2]
      party=line_data[11]
      office=line_data[6][3:4]
      name=line_data[10]
      votes_earned=int( line_data[14].replace(",","") )
      total_votes=int( line_data[15].replace(",","") )
      if votes_earned/total_votes>0.01: #Must be careful about vote recounts and other such data distorting quirks
       election_campaign_data.append( 
	{"year":year, 
	"state":state, 
	"party":party, 
	"office":office, 
	"district":"",
	"name":name, 
	"votes_earned":votes_earned, 
	"total_votes":total_votes } )
      else:
       problematic_data.append(line)
     except:
      problematic_data.append(line)
      continue
      #print(sys.exc_info())
  
  elif "president" in _file:
   for line in f:
     try:
      line_data=line.replace("\"","").split("\t")
      year=int(line_data[0])
      state=line_data[2]
      party=line_data[8]
      office=line_data[6][3:4]
      name=line_data[7]
      votes_earned=int( line_data[10].replace(",","") )
      total_votes=int( line_data[11].replace(",","") )
      if votes_earned/total_votes>0.01: #Must be careful about vote recounts and other such data distorting quirks
       election_campaign_data.append( 
	{"year":year, 
	"state":state, 
	"party":party, 
	"office":office, 
	"district":"",
	"name":name, 
	"votes_earned":votes_earned, 
	"total_votes":total_votes } )
      else:
       problematic_data.append(line)
     except:
      problematic_data.append(line)
      continue
      #print(sys.exc_info())
  f.close()
 return election_campaign_data, problematic_data

def read_candidate_data(working_directory):
 import os
 candidate_data=[]
 candidate_file_list=[ "candidate_summary_2008.csv", "candidate_summary_2010.csv", 
	"candidate_summary_2012.csv", "candidate_summary_2014.csv", "candidate_summary_2016.csv", 
	"candidate_summary_2018.csv", "candidate_summary_2020.csv"]
 for file in candidate_file_list:
  year=int(file[18:22])
  f=open( os.path.join(working_directory, "working_data/"+file) ,'r')
  f.readline()
  for line in f:
   line_data=line.split("\",\"")
   if len(line_data[1].split(" "))>=2: #Must be careful about fake candidates with no last name
    candidate_data.append(
	{ "year":year, 
	"state":line_data[16], 
	"party":line_data[6], 
	"office":line_data[3], 
	"name":line_data[1], 	
	"candidate_ID":line_data[2]})
 return candidate_data

def create_map_between_committeeIDs_and_candidateIDs(working_directory):
 import os
 committee_candidate_map={} #Container for final data
 committee_file_list=[ "committee_summary_2008.csv", "committee_summary_2010.csv", "committee_summary_2012.csv",
	"committee_summary_2014.csv", "committee_summary_2016.csv", "committee_summary_2018.csv",
	"committee_summary_2020.csv"]
 for file in committee_file_list:
  f=open( os.path.join(working_directory,"working_data/"+file) ,'r') 
  f.readline()
  for line in f:
   line_data=line.split("\",\"")
   candidateID=line_data[12]
   committeeID=line_data[1]
   year=int(line_data[13])
   committee_candidate_map[candidateID] = [committeeID,year]
   #example: committee_data[ "H8Nx25105" ] = [ "C00675108", 2020 ]
 return committee_candidate_map



# This function takes time. O(n^2) complexity. 
def create_link_between_election_data_and_candidate_data(working_directory,
	election_campaign_data, candidate_data, committee_candidate_map):
 election_campaign_data_level_2=[]
 
# Start from the 20,000th entry in election_campaign_data since that data goes all the way back to 1976, 
# while the candidate_data only goes back to 2008
 for i in range( 0 , len(election_campaign_data) ):
  if i%200==0:
   #Give the patient user an update every 200 checks
   print("Currently testing candidate number " + str(i))
   
  #If the name is "NA" or some other sort of nonsense, then skip it and move on
  if len(election_campaign_data[i]["name"])<3:
   continue
   
  name_from_election_data = election_campaign_data[i]["name"].replace(",","").replace(".","").split(" ") 
  #Example: "John R. Smith" -> ["John", "R.", "Smith"]
  
  for j in range(0, len(candidate_data) ):
   name_from_candidate_data = candidate_data[j]["name"].split(" ") 
   #Example: "SMITH, JOHN R. MR" -> ["SMITH,", "JOHN", "R.", "MR"]
   
   nonpresident_name_does_match=( (name_from_election_data[0].upper() 
		in name_from_candidate_data[1].upper() ) 
		#Compare first name from election data to first name from candidate data
		and ( name_from_election_data[ len(name_from_election_data)-1 ].upper() 
		in name_from_candidate_data[0].upper() ) 
		#Compare last name from election data to last name from candidate data
		and election_campaign_data[i]["office"]!="P" )
	#For non-presidential candidates
   president_name_does_match=( (name_from_election_data[0].upper() 
		in name_from_candidate_data[0].upper() ) 
	#Compare first name from election data to first name from candidate data
		and ( name_from_election_data[1].upper() 
		in name_from_candidate_data[1].upper() ) 	
	#Compare last name from election data to last name from candidate data
		and election_campaign_data[i]["office"]=="P" )
	#For presidential candidates
        
   
   names_do_match = nonpresident_name_does_match or president_name_does_match
   years_do_match = ( election_campaign_data[i]["year"] == candidate_data[j]["year"] )
   parties_do_match = ( candidate_data[j]["party"] in election_campaign_data[i]["party"].upper() )
   offices_do_match = ( election_campaign_data[i]["office"] == candidate_data[j]["office"] )
   is_Running_for_President_or_states_do_match=( 
	(election_campaign_data[i]["state"] == candidate_data[j]["state"] ) 
	or election_campaign_data[i]["office"]=="P" )
   if (names_do_match 
	and years_do_match 
	and parties_do_match 
	and offices_do_match 
	and is_Running_for_President_or_states_do_match):
    #print("MATCH!!!")
    #print("Election campaign data: " + str(i)+"---->" + str(election_campaign_data[i]) )
    #print("Candidate data: " + str(j)+"---->" + str(candidate_data[j]) )
    #print("\n")
    
    committee_ID=""
    if candidate_data[j]["candidate_ID"] in committee_candidate_map.keys():
     #print("We also have a matching committee!!!")
     committee_ID=committee_candidate_map[ candidate_data[j]["candidate_ID"] ][0]  
         
    election_campaign_data_level_2.append( 
	{"year":election_campaign_data[i]["year"], 
	"state":election_campaign_data[i]["state"], 
	"district":election_campaign_data[i]["district"],
	"party":election_campaign_data[i]["party"], 
	"office":election_campaign_data[i]["office"], 
	"name":election_campaign_data[i]["name"], 
	"votes_earned":election_campaign_data[i]["votes_earned"], 
	"total_votes":election_campaign_data[i]["total_votes"], 
	"candidate_ID":candidate_data[j]["candidate_ID"], 
	"committee_ID":committee_ID,
	"Elec-Camp-Data-Index":i, 
	"Cand-Data-Index":j } )
        
 return election_campaign_data_level_2


def add_political_opponents_to_ECD(election_campaign_data_level_2):
 for i in range(0, len(election_campaign_data_level_2) ):
  election_campaign_data_level_2[i]["opponents"]={ "index_list":[] , "donations":{} }
  for j in range(0, len(election_campaign_data_level_2) ):
   if ( election_campaign_data_level_2[i]["year"]==election_campaign_data_level_2[j]["year"]
	and election_campaign_data_level_2[i]["state"]==election_campaign_data_level_2[j]["state"]
	and election_campaign_data_level_2[i]["office"]==election_campaign_data_level_2[j]["office"]
	and election_campaign_data_level_2[i]["district"]==election_campaign_data_level_2[j]["district"]
	and election_campaign_data_level_2[i]["total_votes"]==election_campaign_data_level_2[j]["total_votes"]
	and i!=j
	):
    election_campaign_data_level_2[i]["opponents"]["index_list"].append(j)
 return election_campaign_data_level_2





def create_map_between_committeeIDs_and_election_campaigns(election_campaign_data_level_2):
 committee_campaign_map={}
 for i in range(0, len(election_campaign_data_level_2) ):
  committee_ID=election_campaign_data_level_2[i]["committee_ID"]
  year=election_campaign_data_level_2[i]["year"]
  state=election_campaign_data_level_2[i]["state"]
  if len(committee_ID)>0:
   try:
    dummy_variable=committee_campaign_map[committee_ID]
   except:
    committee_campaign_map[committee_ID]={}
   try:
    dummy_variable=committee_campaign_map[committee_ID][year]
   except:
    committee_campaign_map[committee_ID][year]={}
   committee_campaign_map[committee_ID][year][state]=i
 return committee_campaign_map


def categorize_donations(working_directory,election_campaign_data_level_2,committee_campaign_map,donation_ranges):
 import os
 import codecs
 campaign_donation_file_list=["donation_data_2008", "donation_data_2010", "donation_data_2012", "donation_data_2014", "donation_data_2016", "donation_data_2018", "donation_data_2020"]
 election_campaign_and_donation_data=election_campaign_data_level_2
 donation_bucket_labels=[]
 for i in range(0, len(donation_ranges)-1 ):
  donation_bucket_labels.append( str( donation_ranges[i] )+"-"+str( donation_ranges[i+1]-1 ) )
 print(donation_bucket_labels)
 for election in election_campaign_and_donation_data:
  election["donation_data"]={}
  election["donation_data"]["number_of_donations"]=0
  election["donation_data"]["total_dollar_amount"]=0
  #election["opponents"]
  for bucket in donation_bucket_labels:
   election["donation_data"][bucket + "_N-O-D"]=0
   election["donation_data"][bucket + "_T-D-A"]=0
   election["donation_data"]["opposition_" + bucket + "_N-O-D"]=0
   election["donation_data"]["opposition_" + bucket + "_T-D-A"]=0
 
 file_number=0
 donation_number=0
 invalid_date_count=0
 for campaign_donation_file in campaign_donation_file_list:
  file_number+=1
  filepath=os.path.join(working_directory, "working_data/"+campaign_donation_file)
  f=codecs.open(filepath,'r', encoding='utf-8', errors='ignore')
  for row in f:
   donation_number+=1
   if (donation_number%500000==0):
    print(row)
   row_data=row.split("|")
   committeeID=row_data[0]
   donation_amount=int(row_data[14])	
   date=row_data[13]
   state=row_data[9]
   election_year=int(campaign_donation_file[-4:])		
   
   try:
    date=date[4:]+date[:4]   
    year=date[0:4]
    date=int(date)
    year=int(year)
   except:
    invalid_date_count+=1
    continue
   committee_donation_is_an_election_campaign=False
   election_campaign={}
   try:
    campaign_data_index=committee_campaign_map[committeeID][year][state]
    election_campaign=election_campaign_data_level_2[campaign_data_index] 
    committee_donation_is_an_election_campaign=True
   except:
    committee_donation_is_an_election_campaign=False
    continue    
   date_does_match=(   date < int( str(year)+str(1107) )  
	and date > int( str(year-2)+str(1107) )   )
   state_does_match=( state==election_campaign["state"] )
   if ( committee_donation_is_an_election_campaign 
	and date_does_match 
	and state_does_match ):
    if (donation_number%500==0):
     print(row)
     print(election_campaign_and_donation_data[campaign_data_index])
     print("\n")
    election_campaign_and_donation_data[campaign_data_index]["donation_data"]["number_of_donations"]+=1
    election_campaign_and_donation_data[campaign_data_index]["donation_data"]["total_dollar_amount"]+=donation_amount 
    for bucket_boundary in range(0, len(donation_ranges)-1 ):
     if ( donation_amount>=donation_ranges[ bucket_boundary ] 
	and donation_amount<donation_ranges[ bucket_boundary+1 ] ):
      donation_bucket_label=str( donation_ranges[bucket_boundary] )+"-"+str( donation_ranges[bucket_boundary+1] -1 )
      election_campaign_and_donation_data[campaign_data_index]["donation_data"][donation_bucket_label + "_N-O-D"]+=1
      election_campaign_and_donation_data[campaign_data_index]["donation_data"][donation_bucket_label + "_T-D-A"]+=donation_amount
      if (donation_number%500==0):
       print(election_campaign_and_donation_data[campaign_data_index])
       print("\n")
      for opponent_campaign_index in election_campaign_and_donation_data[campaign_data_index]["opponents"]["index_list"]:
       if (donation_number%500==0):
        print(election_campaign_and_donation_data[opponent_campaign_index])
        print("\n")
       election_campaign_and_donation_data[opponent_campaign_index]["donation_data"]["opposition_" + donation_bucket_label + "_N-O-D"]+=1
       election_campaign_and_donation_data[opponent_campaign_index]["donation_data"]["opposition_" + donation_bucket_label + "_T-D-A"]+=donation_amount
       if (donation_number%500==0):
        print(election_campaign_and_donation_data[opponent_campaign_index])
        print("\n\n\n")
 
 return election_campaign_and_donation_data


def create_linear_multilinear_plot(dir,election_campaign_and_donation_data, office=[],state=[],party=[],year=[]):
 import matplotlib.pyplot as plt
 from scipy import stats
 import numpy
 from pandas import DataFrame
 from sklearn import linear_model
 info_caption="Office(s):"
 need_comma=False
 if len(office)==0:
  info_caption=" President, Senate, House"
 if "P" in office:
  info_caption=info_caption+" President"
  need_comma=True
 if "S" in office:
  if need_comma:
   info_caption=info_caption+","
  info_caption=info_caption+" Senate"
  need_comma=True
 if "H" in office:
  if need_comma:
   info_caption=info_caption+","
  info_caption=info_caption+" House"
 info_caption=info_caption+";   Party:"
 if len(party)==0:
  info_caption=info_caption+" Democrats, Republicans"
 if "democrat" in party:
  info_caption=info_caption+" Democrats" 
  need_comma=True
 if "republican" in party: 
  if need_comma:
   info_caption=info_caption+","
  info_caption=info_caption+" Republicans"
 info_caption=info_caption+";   State(s): "
 if len(state)==0:
  info_caption=info_caption+" All states"
 for i in state:
  info_caption=info_caption+i+", "
 info_caption=info_caption+";   Years:"
 if len(year)==0:
  info_caption=info_caption+" 2008,2010,2012,2014,2016,2018"
 for i in year:
  info_caption=info_caption+i+", "
 print(info_caption)
 x0=[]
 x1=[]
 x2=[]
 x3=[]
 x4=[]
 y=[]
 for election in election_campaign_and_donation_data:
  election_committee_matches_office_criteria=False
  election_committee_matches_state_criteria=False
  election_committee_matches_party_criteria=False
  election_committee_matches_year_criteria=False
  election_committee_matches_criteria=False
  if len(office)==0:
   election_committee_matches_office_criteria=True  
  for j in office:
   if j in election['office']:
    election_committee_matches_office_criteria=True
  if len(state)==0:
   election_committee_matches_state_criteria=True
  for j in state:
   if j in election['state']:
    election_committee_matches_state_criteria=True
  if len(party)==0:
   election_committee_matches_party_criteria=True
  for j in party:
   if j in election['party']:
    election_committee_matches_party_criteria=True
  if len(year)==0:
   election_committee_matches_year_criteria=True
  for j in year:
   if j==election['year']:
    election_committee_matches_year_criteria=True
  #print(election)
  #print(election_committee_matches_office_criteria)
  #print(election_committee_matches_state_criteria)
  #print(election_committee_matches_party_criteria)
  #print(election_committee_matches_year_criteria)
  if election_committee_matches_office_criteria and election_committee_matches_state_criteria and election_committee_matches_party_criteria and election_committee_matches_year_criteria:
   election_committee_matches_criteria=True
  if election_committee_matches_criteria:
   election["donation_data"].update( {"votes_earned":election["votes_earned"] } )
   x0.append( election["donation_data"] )
   x1.append( election["donation_data"] )
 x0_columns=list( x0[0].keys() )
 print(x0_columns)
 df = DataFrame(x0,columns=x0_columns)
 print("test1")
 x0_columns.remove("votes_earned")
 X = df[x0_columns]
 print("test2")
 Y = df[['votes_earned']]
 print("test3")
 regr = linear_model.LinearRegression(fit_intercept=True)
 q=regr.fit(X, Y)
 print("R^2: " + str(q.score(X,Y)) )
 print("Intercept: " + str(q.intercept_) )
 for i in range(0,len(q.coef_[0])):
  print("Label: " + df.columns[i] + "\n\tregression coefficient: " + str(q.coef_[0][i]) + "")
 for i in range(0, len(x1)):
  for j in range(0, len(x1[0].keys()) ):
   key=list( x1[0].keys() )
   if key[j]!='votes_earned':
    x1[i][ key[j] ] = x1[i][ key[j] ]**2
 print("test1")
 x1_columns=list( x1[0].keys() )
 df = DataFrame(x1,columns=x1_columns)
 print("test2")
 x1_columns.remove("votes_earned")
 X = df[x1_columns]
 print("test3")
 Y = df[['votes_earned']]
 regr = linear_model.LinearRegression(fit_intercept=True)
 q=regr.fit(X, Y)
 print("R^2: " + str(q.score(X,Y)) )
 print("Intercept: " + str(q.intercept_) )
 for i in range(0,len(q.coef_[0])):
  print("Label: " + df.columns[i] + "\n\tregression coefficient: " + str(q.coef_[0][i]) + "")   
 return df, q



working_directory = "/home/dave/Desktop/bin"
election_campaign_data, problematic_data = FECDEOVT_read_election_data(working_directory)
candidate_data = read_candidate_data(working_directory)
committee_candidate_map = create_map_between_committeeIDs_and_candidateIDs(working_directory)
election_campaign_data_level_2 = create_link_between_election_data_and_candidate_data(working_directory,
	election_campaign_data, candidate_data, committee_candidate_map)
election_campaign_data_level_2 = add_political_opponents_to_ECD(election_campaign_data_level_2)
committee_campaign_map = create_map_between_committeeIDs_and_election_campaigns(election_campaign_data_level_2)
election_campaign_and_donation_data=categorize_donations(working_directory,election_campaign_data_level_2,committee_campaign_map,[200,800,2000,10000])
df, q = create_linear_multilinear_plot(dir,election_campaign_and_donation_data, office=[],state=[],party=[],year=[])


