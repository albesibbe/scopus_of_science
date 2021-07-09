from scopus_of_science import sos

s = sos.SOS(sco=['datasets/scopus.csv'], wos=['datasets/wos.txt'])
data = s.get()

# s = sos.WOS(['datasets/20200129_wos1-500.txt'], convert=False)
# data = s.get()

# print(data.info())
data.to_csv("holistic.csv", index=False)