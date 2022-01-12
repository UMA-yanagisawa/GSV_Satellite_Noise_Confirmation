import matplotlib.pyplot as plt

class Plot():
    def CNo_Plot(self,CNo,Sec):
        plt.plot(CNo)
        #plt.plot(Sec,CNo)
        plt.xlabel("Sec")
        plt.ylabel("C/No")
        plt.ylim(0,60)
        plt.yticks([0,10,20,30,40,50,60])
        #plt.text(10,10,"test")
        plt.show()

    def CNo_Plot_AX(self,CNo,Sec):
        fig = plt.figure()          #figureを設定
        ax = fig.add_subplot(111)   #Axesを追加
        x = Sec
        y = CNo
        ax.set_title("GNSS Noise",fontsize = 14)            # タイトル追加
        ax.set_xlabel("Sec",size = 12,weight = "light")     #　軸ラベル設定
        ax.set_ylabel("CNo",size = 12,weight = "light")     #　軸ラベル設定

        #ax.set_xticks([0, 100, 200])                       # X軸のメモリ設定
        #ax.set_yticks([0, 60])                             # Y軸のメモリ設定
        plt.plot(CNo)
        ax.grid(which="major", axis="x", color="blue", alpha=0.3, linestyle="--", linewidth=1)
        ax.grid(which="major", axis="y", color="green", alpha=0.3,linestyle="--", linewidth=1)
        plt.show()