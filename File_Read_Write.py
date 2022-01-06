
import wx

class Open_file():
    app = wx.App()
    def read_file(self):
        open_dialog = wx.FileDialog(None, u'読み込むセンテンスを選択', style=wx.FD_OPEN,pos = (600,100))
        open_dialog.ShowModal()
        #open_filename = open_dialog.GetFilename()
        open_filename = open_dialog.GetPath()
        #print(open_filename)
        return open_filename

    def save_file(self):
        save_dialog = wx.FileDialog(None, u'ファイルを選択してください', style=wx.FD_SAVE,pos = (600,100))
        save_dialog.ShowModal()
        save_filename = save_dialog.GetFilename()
        #print(save_filename)
        return save_filename

    def Set_file_name(self,Set_Title_mess,Set_field_mess):
        dialog = wx.TextEntryDialog(None, message = Set_field_mess,caption = Set_Title_mess,pos = (600,100))
        dialog.ShowModal()
        SET_NAME = dialog.GetValue()
        #print(SET_NAME)
        return SET_NAME

    def Dialog_Single(self,list_file):
        list_file = list(map(str, list_file))   #list　内部をSTR型に変換
        dialog = wx.SingleChoiceDialog(None,message = "Satellite Number", caption = "List Dialog",choices = list_file)
        dialog.ShowModal()
        SET_NAME = dialog.GetStringSelection()
        #print(SET_NAME)
        return SET_NAME


#**********************************************************************************
#---使用サンプル---******************************************************************
#**********************************************************************************
"""
import Read_Write_Lib as filelib

file_con = filelib.Open_file()
#str_list = list(map(str,setlist))
file_list = file_con.Dialog_Single(setlist)
print(file_list)
save_filename = file_con.Set_file_name("GNSS",u"保存ファイル名")
open_filename = file_con.read_file()
"""
#***********************************************************************************
#***********************************************************************************
#***********************************************************************************
"""
class MyFrame(wx.Frame):
    def Set_File_Name(self):
        self.frame = wx.Frame(None,-1, "textbox",size = (640,90))
        self.frame.SetTitle('Convert File Name')
        #self.CreateStatusBar()
        panel = wx.Panel(self.frame,-1,pos = (50,35))
        panel.SetBackgroundColour('#AFAFAF')

    # Button Set
        button_1 = wx.Button(panel, -1, 'File Name Set', size=(200, 40), pos=(415, 5))
    # Button_1 Event
        button_1.Bind(wx.EVT_BUTTON, self.ON_click)
        self.frame.Show(True)
    # TEXT WRITE LABEL
        self.frame.text_1 = wx.TextCtrl(panel,-1, 'GNSS Conbert File Name', size=(400, 20), pos=(10, 25))
    # TEXT LABEL SET
        self.frame.label = wx.StaticText(panel, -1, 'FILE NAME', pos=(15, 5))
    # Font size set
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
    # Set Custum Font Size
        self.frame.label.SetFont(font)
        return self.frame.text_1.GetValue()

# Button_1 Event
    def ON_click(self,event):
        text = self.frame.text_1.GetValue()
        print(text)
        self.frame.Close(True)

app = wx.App()
frame = MyFrame()
frame.Set_File_Name()
app.SetTopWindow(frame.frame)
app.MainLoop()
"""