
#with open(r"C:\Users\IanAK\Desktop\Rutgers_Data_boot_camp\Py_Poll_Class_3\Class_stuff_3\Election_Analysis\Resources\election_results.csv") as ftl:
#     eld = csv.reader(ftl, delimiter = ',')
#     for row in eld:
#        print(', '.join(row))
# ftl = file_to_load
# eld = election data 
# Be careful all the data was deleted after using this script
#open(r"C:\Users\IanAK\Desktop\Rutgers_Data_boot_camp\Py_Poll_Class_3\Class_stuff_3\Election_Analysis\Resources\election_results.csv",'r')
# <_io.TextIOWrapper name='election_results.csv' mode='r' encoding='cp1252'>
# To do: performance analysis
# Close the file
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
#    txt_file.write("Counties in the Election\n ---------------\n Arapahoe\n Denver \n Jefferson\n")

    # Print the file object.
#     print(election_data) # <_io.TextIOWrapper name='election_results.csv' mode='r' encoding='cp1252'>



import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)