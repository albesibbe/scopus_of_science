from scopus_of_science import sos, file_handler

f = file_handler.File_Handler()

s = sos.SOS(sco='datasets/20200128_scopus.csv', 
            wos=['datasets/20200129_wos1-500.txt', 'datasets/20200129_wos501-526.txt'])
data = s.get()

print(data)
# data.to_csv("holistic.csv")