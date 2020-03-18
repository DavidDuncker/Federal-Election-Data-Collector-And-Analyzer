# Federal-Election-Data-Collector-And-Analyzer
This Python script will:

1) Download data on U.S. federal elections from the FEC website (if it has not done so already)

2) Create Python classes representing a) individual election results, b) individual candidates, 
  and c) individual committees, and then save lists of all three types of data using the Python Pickle package 
  (if it has not done so already)
  
 3) Link together related yet separate parts of the dataset 
  (i.e. which candidate is associated with which political committee, or which election results are associated
  with which candidates)
  
 3) Create a local SQLite server containing all the data.
 
 To run, simply run main.py. After several hours of downloading data and crosslinking the data together, you will 
  have an SQLite database on your computer.
  
 "FECD-EOVT_old_legacy_code.py" is old legacy code that I used before I decided to clean up the code and add SQLite
  functionality. If it still works, then it will actually use Scipy and Numpy to automatically generate multivariate
  regression analyses on how well each donation amount is correlated with vote totals. This was the original purpose
  of the project.
