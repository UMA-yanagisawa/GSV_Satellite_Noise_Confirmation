import File_Read_Write
import CNo_Plot

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

while True: #NMEA Protocol 4.1以上か確認
    for i in range (len(GGA)):
        if GGA[i][0] == "GNGSV" or GGA[i][0] == "GPGSV":
            print(len(GGA[i]))
            if len(GGA[i]) == 21:
                break
            elif len(GGA[i]) == 20:
                SetFile.Mess()
                exit()
    break

listfile = []
print(len(GGA_file))

for i in range(len(GGA_file)):      #サテライトナンバー検出

    #if (GGA[i][0]) == "GPGSV" or (GGA[i][0]) == "GNGSV" or (GGA[i][0]) == "GLGSV" or (GGA[i][0]) == "GAGSV" or (GGA[i][0]) == "GBGSV":
    if ((GGA[i][0]) == ("GPGSV")):
        try:
            target = "*"
            idx = GGA[i][19].find(target)
            GGA[i][19] = GGA[i][19][:idx]
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

CNo_LIST = []
SEC_LIST = []

fast = 0
for i in range(len(GGA)):
    if (GGA[i][0]) == "GPGGA" or (GGA[i][0]) == "GNGGA":
        target = "."

        data = float(GGA[i][1])
        """
        h = float(int(data[1:2]) + 9)
        m = float(data[3:4])
        s = float(data[5:9])
        if (h >= 24):
            h = h - 24
        """
        h=0
        m=0
        s=0
        if fast == 0:
            STD_time = round(data,3)
            fast = 1
        else:
            elapsed_time = round(data - STD_time,3)

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
                    CNo_LIST.append(int(GGA[i][7]))
                    SEC_LIST.append(float(elapsed_time))
                elif (GGA[i][8] == Dailog):
                    CNo_LIST.append(int(GGA[i][7]))
                    SEC_LIST.append(float(elapsed_time))
                elif (GGA[i][12] == Dailog):
                    CNo_LIST.append(int(GGA[i][7]))
                    SEC_LIST.append(float(elapsed_time))
                elif (GGA[i][16] == Dailog):
                    #print("衛星番号 = " + str(GGA[i][16]) + " 衛星仰角 = " + str(GGA[i][17]) + " 衛星方位 = " + str(GGA[i][18]) + " C/No = " + str(GGA[i][19])
                     #     + " " + str(h) + "時" + str(m) + "分" + str(s) +"秒　" +  " Signal_ID = " + str(SignalID[0]) + " 経過時間 = " + str(elapsed_time))
                    CNo_LIST.append(int(GGA[i][7]))
                    SEC_LIST.append(float(elapsed_time))
                else:
                    pass
            except:
                pass

print("CNo_LIST " + str(len(CNo_LIST)))
print("SEC_LIST " + str(len(SEC_LIST)))

while True: #listサイズ比較
    if len(CNo_LIST) < len(SEC_LIST):
        del SEC_LIST[len(SEC_LIST)-1]
    if len(SEC_LIST) < len(CNo_LIST):
        del CNo_LIST[len(CNo_LIST)-1]
    else:
        break

Noise_plot = CNo_Plot.Plot()
#Noise_plot.CNo_Plot(CNo_LIST,SEC_LIST)
Noise_plot.CNo_Plot_AX(CNo_LIST,SEC_LIST)

exit()
