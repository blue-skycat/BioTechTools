import requests
import time
import os
import csv

starbaseurl = "https://starbase.sysu.edu.cn/api/miRNATarget/?assembly=hg19&geneType=mRNA&miRNA="
param = "&clipExpNum=5&degraExpNum=1&pancancerNum=10&programNum=5&program=None&target=all&cellType=all"

if not os.path.exists("mRNA"):
    os.mkdir("mRNA")

f = open('./miRNA.txt', 'r')

lines = f.readlines()
count=1
for line in lines:

    miRNA = line.strip()
    formatstr="共%d行，当前第%d行,miRNA: %s" %(len(lines), count, miRNA)
    print(formatstr)
    count += 1
    # res = requests.post(starbaseurl + miRNA + param)
    # if res.status_code == 200:
    #     create_file = open("./mRNA/" + miRNA + ".txt", "wb")
    #     create_file.write(res.content)
    #     print("获取的数据：", res.content)
    #     create_file.close()
    time.sleep(1.2)

f.close()

path = "./mRNA"
files = os.listdir(path)
for file in files:
    dfile = open(path + "/" + file, 'r')
    dlines = dfile.readlines()
    for dline in dlines[4:len(dlines)]:
        with open("miRNATargetingmRNA.csv", "a", newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            dlinetab = dline.strip().split('\t')
            print("当前数据行：", dlinetab)
            spamwriter.writerow(dlinetab)
    dfile.close()
