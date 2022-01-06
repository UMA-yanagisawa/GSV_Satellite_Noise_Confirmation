import File_Read_Write

SetFile = File_Read_Write.Open_file()
GGA_FileName = SetFile.read_file()

GGA_Read = open(GGA_FileName)               # ファイル終端まで全て読んだデータを返す
GGA_file = GGA_Read.read()
GGA_Read.close()                            # ファイルクローズ
GGA_file = GGA_file.split("$")

GGA = [i for i in GGA_file]                 #ファイル分のリストを作る。

for i in range(len(GGA_file)):
    GGA[i] = GGA_file[i].split(",")
    #print(GGA[i])

listfile = []
print(len(GGA_file))
for i in range(len(GGA_file)):
    #if (GGA[i][0]) == "GPGSV" or (GGA[i][0]) == "GNGSV" or (GGA[i][0]) == "GLGSV" or (GGA[i][0]) == "GAGSV" or (GGA[i][0]) == "GBGSV":
    if ((GGA[i][0]) == ("GPGSV")):
        try:
            target = "*"
            idx = GGA[i][19].find(target)
            GGA[i][19] = GGA[i][19][:idx]
            """
            print("衛星番号 = " + str(GGA[i][4]) + " 衛星仰角 = " + str(GGA[i][5]) + " 衛星方位 = " + str(GGA[i][6]) + " C/No = " + str(GGA[i][7]))
            print("衛星番号 = " + str(GGA[i][8]) + " 衛星仰角 = " + str(GGA[i][9]) + " 衛星方位 = " + str(GGA[i][10]) + " C/No = " + str(GGA[i][11]))
            print("衛星番号 = " + str(GGA[i][12]) + " 衛星仰角 = " + str(GGA[i][13]) + " 衛星方位 = " + str(GGA[i][14]) + " C/No = " + str(GGA[i][15]))
            print("衛星番号 = " + str(GGA[i][16]) + " 衛星仰角 = " + str(GGA[i][17]) + " 衛星方位 = " + str(GGA[i][18]) + " C/No = " + str(GGA[i][19]))
            """
            listfile.append(GGA[i][4])
            listfile.append(GGA[i][8])
            listfile.append(GGA[i][12])
            listfile.append(GGA[i][16])

        except:
            pass

#print(set(listfile))
#***************************************************
Dailog = SetFile.Dialog_Single(set(listfile))           #　抽出するサテライトナンバーを選択する
print(Dailog)
#***************************************************

for i in range(len(GGA)):
    if (GGA[i][0]) == "GPGGA" or (GGA[i][0]) == "GNGGA":
        target = "."
        #idx = GGA[i][1].find(target)
        #data = GGA[i][1][:idx]
        data = GGA[i][1]
        h = int(data[1:2]) + 9
        m = int(data[3:4])
        s = (data[5:9])
        if (h >= 24):
            h = h - 24

    #if (GGA[i][0]) == "GPGSV" or (GGA[i][0]) == "GNGSV" or (GGA[i][0]) == "GLGSV" or (GGA[i][0]) == "GAGSV" or (GGA[i][0]) == "GBGSV":
    if ((GGA[i][0]) == ("GPGSV")):
        #print(len(GGA[i]))
        lit_size = (int(len(GGA[i]) - 1))
        SignalID = GGA[i][lit_size].split("*")
        #print("Signal ID + " + str(SignalID[0]))
        if SignalID[0] == "1":
            #print(GGA[i])
            try:
                if (GGA[i][4] == Dailog):
                    print("衛星番号 = " + str(GGA[i][4]) + " 衛星仰角 = " + str(GGA[i][5]) + " 衛星方位 = " + str(GGA[i][6]) + " C/No = " + str(GGA[i][7])
                          + " " + str(h) + "時" + str(m) + "分" + str(s) +"秒　" +  " Signal_ID = " + str(SignalID[0]))
                elif (GGA[i][8] == Dailog):
                    print("衛星番号 = " + str(GGA[i][8]) + " 衛星仰角 = " + str(GGA[i][9]) + " 衛星方位 = " + str(GGA[i][10]) + " C/No = " + str(GGA[i][11])
                          + " " + str(h) + "時" + str(m) + "分" + str(s) +"秒　" +  " Signal_ID = " + str(SignalID[0]))
                elif (GGA[i][12] == Dailog):
                    print("衛星番号 = " + str(GGA[i][12]) + " 衛星仰角 = " + str(GGA[i][13]) + " 衛星方位 = " + str(GGA[i][14]) + " C/No = " + str(GGA[i][15])
                          + " " + str(h) + "時" + str(m) + "分" + str(s) +"秒　" +  " Signal_ID = " + str(SignalID[0]))
                elif (GGA[i][16] == Dailog):
                    print("衛星番号 = " + str(GGA[i][16]) + " 衛星仰角 = " + str(GGA[i][17]) + " 衛星方位 = " + str(GGA[i][18]) + " C/No = " + str(GGA[i][19])
                          + " " + str(h) + "時" + str(m) + "分" + str(s) +"秒　" +  " Signal_ID = " + str(SignalID[0]))
                else:
                    pass
            except:
                pass