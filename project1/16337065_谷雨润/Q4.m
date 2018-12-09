path = "/Users/guyurun/Desktop/data_selected"
files = os.listdir(path)
csv_files = list(filter(lambda x: x[-4:] == '.csv', files))
file_list = []
for file in csv_files:
    file_list.append(pd.read_csv(path+file))
 

M1, P1 = corr(filelist,'type','pearson')
M2, P2 = corr(filelist,'type','spearman')
print("Pearson")
sort(M1, P1)
print("Spearman")
sort(M2, P2)
