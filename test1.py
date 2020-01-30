from scopus_of_science import sos

# Import databases
ss = sos.SOS(sco=["datasets/20200128_scopus.csv"], wos=["datasets/20200129_wos1-500.txt", "datasets/20200129_wos501-526.txt"])

# Get DataFrame
data = ss.get()

# Print DataFrame
print(data.head()) #.sort_values(by="Title")

# Save data to excel file
data.to_excel("test.xlsx")