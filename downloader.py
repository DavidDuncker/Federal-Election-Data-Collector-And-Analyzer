#!/usr/bin/python3
import requests


def generate_download_list():
    individual_file_uris = []
    individual_file_names = []

    # Donation file lists
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2020/indiv20.zip")
    individual_file_names.append("indiv20.zip")

    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2018/indiv18.zip")
    individual_file_names.append("indiv18.zip")

    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2016/indiv16.zip")
    individual_file_names.append("indiv16.zip")

    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2014/indiv14.zip")
    individual_file_names.append("indiv14.zip")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2012/indiv12.zip")
    individual_file_names.append("indiv12.zip")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2010/indiv10.zip")
    individual_file_names.append("indiv10.zip")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2008/indiv08.zip")
    individual_file_names.append("indiv08.zip")
    # Candidate file lists
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2020/candidate_summary_2020.csv")
    individual_file_names.append("candidate_summary_2020.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2018/candidate_summary_2018.csv")
    individual_file_names.append("candidate_summary_2018.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2016/candidate_summary_2016.csv")
    individual_file_names.append("candidate_summary_2016.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2014/candidate_summary_2014.csv")
    individual_file_names.append("candidate_summary_2014.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2012/candidate_summary_2012.csv")
    individual_file_names.append("candidate_summary_2012.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2010/candidate_summary_2010.csv")
    individual_file_names.append("candidate_summary_2010.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2008/candidate_summary_2008.csv")
    individual_file_names.append("candidate_summary_2008.csv")
    # Election committee file lists
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2020/committee_summary_2020.csv")
    individual_file_names.append("committee_summary_2020.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2018/committee_summary_2018.csv")
    individual_file_names.append("committee_summary_2018.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2016/committee_summary_2016.csv")
    individual_file_names.append("committee_summary_2016.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2014/committee_summary_2014.csv")
    individual_file_names.append("committee_summary_2014.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2012/committee_summary_2012.csv")
    individual_file_names.append("committee_summary_2012.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2010/committee_summary_2010.csv")
    individual_file_names.append("committee_summary_2010.csv")
    individual_file_uris.append("https://www.fec.gov/files/bulk-downloads/2008/committee_summary_2008.csv")
    individual_file_names.append("committee_summary_2008.csv")
    # Presidential election results
    individual_file_uris.append("https://dataverse.harvard.edu/api/access/datafile/3444051?format=tab&gbrecs=true")
    individual_file_names.append("1976-2016-president.tab")
    # Senate election results
    individual_file_uris.append("https://dataverse.harvard.edu/api/access/datafile/3440424?format=tab&gbrecs=true")
    individual_file_names.append("1976-2018-senate.tab")
    # House election Results
    individual_file_uris.append("https://dataverse.harvard.edu/api/access/datafile/3561497?format=tab&gbrecs=true")
    individual_file_names.append("1976-2018-house.tab")
    return individual_file_uris, individual_file_names


def check_for_required_downloads(working_directory, individual_file_names):
    import os
    indexed_list_of_required_downloads = []
    for i in range(0, len(individual_file_names)):
        file_path = os.path.join(working_directory, "working_data/" + individual_file_names[i])
        if (not os.path.exists(file_path)) and ("indiv" not in individual_file_names[i]):
            print("File path " + file_path + " not found, adding to download list")
            indexed_list_of_required_downloads.append(i)
    donation_data_files_and_affiliated_zipfiles = {}
    donation_data_files_and_affiliated_zipfiles.update({"donation_data_2008": "indiv08.zip"})
    donation_data_files_and_affiliated_zipfiles.update({"donation_data_2010": "indiv10.zip"})
    donation_data_files_and_affiliated_zipfiles.update({"donation_data_2012": "indiv12.zip"})
    donation_data_files_and_affiliated_zipfiles.update({"donation_data_2014": "indiv14.zip"})
    donation_data_files_and_affiliated_zipfiles.update({"donation_data_2016": "indiv16.zip"})
    donation_data_files_and_affiliated_zipfiles.update({"donation_data_2018": "indiv18.zip"})
    donation_data_files_and_affiliated_zipfiles.update({"donation_data_2020": "indiv20.zip"})
    for filename in donation_data_files_and_affiliated_zipfiles.keys():
        file_path = os.path.join(working_directory, "working_data/" + filename)
        if not os.path.exists(os.path.join(working_directory, "working_data/"+filename)):
            print("File path " + file_path + " not found, adding to download list")
            donation_zipfile = donation_data_files_and_affiliated_zipfiles[filename]
            indexed_location = individual_file_names.index(donation_zipfile)
            indexed_list_of_required_downloads.append(indexed_location)

    return indexed_list_of_required_downloads


def make_file_path(filename, working_directory):
    import os
    directory = os.path.join(working_directory, "working_data/")
    if not os.path.exists(directory):
        os.makedirs(directory)
    return


def display_progress_bar(web_response, file):
    import sys
    import requests
    total_length = web_response.headers.get('content-length')
    if total_length is None:  # no content length header
        file.write(web_response.content)
        print("No content length header")
    else:
        dl = 0
        total_length = int(total_length)
        for data in web_response.iter_content(chunk_size=4096):
            dl += len(data)
            file.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write(
                "\r[%s%s] %s" % ('=' * done, ' ' * (50 - done), str(round(dl / total_length * 100, 1)) + "%"))
            sys.stdout.flush()
    file.close()
    print("\n")
    return True


def fetch_data(file_path, fraction_done, uri):
    print("Downloading and saving file " + str(fraction_done))
    print(file_path)
    print(uri)
    print("to file: " + file_path)
    file = open(file_path, 'wb')
    web_request = requests.get(uri, stream=True)
    display_progress_bar(web_request, file)


def unzip_zipfile(filename, working_directory, file_path):
    import zipfile
    import os
    if filename[0:5] == 'indiv' and filename[-3:] == 'zip':
        new_unzipped_filepath = os.path.join(working_directory, "working_data/donation_data_20" + filename[5:7])
        print("Unzipping data from " + filename + " to " + new_unzipped_filepath)
        f = open(new_unzipped_filepath, 'wb')
        z = zipfile.ZipFile(file_path, 'r')
        f.write(z.read("itcont.txt"))
        f.close()
        z.close()
        os.remove(file_path)
    return True


def download_data(working_directory):
    import os
    import requests
    import zipfile
    import sys

    individual_file_uris, individual_file_names = generate_download_list()
    indexed_list_of_required_downloads = check_for_required_downloads(working_directory,
                                                                      individual_file_names)
    number_of_files_downloaded = 0
    for i in indexed_list_of_required_downloads:
        number_of_files_downloaded += 1
        uri = individual_file_uris[i]
        filename = individual_file_names[i]
        file_path = os.path.join(working_directory, "working_data/" + filename)
        make_file_path(filename, working_directory)
        fraction_done = str(number_of_files_downloaded) + "/" + str(len(indexed_list_of_required_downloads))
        fetch_data(file_path, fraction_done, uri)
        unzip_zipfile(filename, working_directory, file_path)

        print("\n\n")
    return True
