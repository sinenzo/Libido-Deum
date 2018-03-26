import sys,  random
from PyQt5 import QtCore,  QtGui, QtWidgets
from libidodeum_gui import Ui_MainWindow

class libidodeum_core(Ui_MainWindow):
    def __init__(self,  MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.pushButton_1.clicked.connect(self.GrandeAntico)
        self.pushButton_2.clicked.connect(self.Investigatori)
    
    def GrandeAntico(self):
        arkhamGA = ["Cthulu", "Yog-Sothoth", "Shub-Niggurath", "Ithaqua", "Azathoth", 
        "Hastur","Yig", "Nyarlathotep"]
        if self.innsmouth.isChecked() == True:
            innsmouthGA = ["Bokrug (I)", "Chaugnar Faugn (I)", "Cthugha (I)", "Ghatanothoa (I)", 
            "Nyogtha (I)", "Quachil Uttaus (I)", "Rhan-Tegoth (I)", "Zhar (I)"]
            arkhamGA = arkhamGA + innsmouthGA
        if self.kingsport.isChecked() == True:
            kingsportGA = ["Eihort (K)","Yibb-Tsill (K)","Y'Golonac (K)","Atlach-Nacha (K)"]
            arkhamGA = arkhamGA + kingsportGA
        if self.dunwich.isChecked() == True: 
            dunwichGA = ["Abhoth (D)","Glaaki (D)","Shudde M'ell (D)","Tsathoggua (D)"]
            arkhamGA = arkhamGA + dunwichGA 
        ga = random.choice(arkhamGA)
        self.textEdit_1.setText(ga)
       
    def Investigatori(self):
        arkhamIn = [" Kate Winthrop"," Carolyn Fern"," Monterey Jack"," Mandy Thompson",
        " Darrell Simmons"," Sorella Mary"," Vincent Lee"," Ashcan Pete"," Bob Jerkins",
        " Michael McGlen"," Amanda Sharpe"," Dexter Drake", " Harvey Walters",
        " Gloria Goldberg"," Genny Barnes"," Joe Diamond"]
        if self.innsmouth.isChecked() == True:
            innsmouthIn = [" Agnes Baker (I)"," Akachi Onyele (I)"," Finn Edwards (I)",
            " George Barnaby (I)"," Hank Samson (I)"," Minh Thi Phan (I)",
            " Norman Withers (I)", " Patrice Hathaway (I)"," Roland Banks (I)",
            " Silas Marsh (I)"," Skids O'Toole (I)", " Tommy Muldoon (I)",
            " Trish Scarborough (I)"," Ursula Downs (I)"," William Yorick (I)",
            " Zoey Samaras (I)"]
            arkhamIn = arkhamIn + innsmouthIn
        if self.kingsport.isChecked() == True:
            kingsportIn = [" Charlie Kane (K)"," Wendy Adams (K)"," Rex Murphy (K)",
            " Daisy Walker (K)"," Tony Morgan (K)"," Lola Hayes (K)"," Lily Chen (K)",
            " Luke Robinson (K)"]
            arkhamIn = arkhamIn + kingsportIn
        if self.dunwich.isChecked() == True:
            dunwichIn = [" Diana Stanley (D)"," Jacqueline Fine (D)"," Jim Culver (D)",
            " Leo Anderson (D)"," Marie Lambeau (D)"," Mark Harrigan (D)"," Rita Young (D)",
            " Wilson Richards (D)"]
            arkhamIn = arkhamIn + dunwichIn
        inv = ""
        inves = []
        i = 0
        while i <=  self.comboBox.currentIndex():
            inv = random.choice(arkhamIn)
            while inv not in inves:
                inves.append(inv)
            i += 1        
        self.textEdit_2.setText(", ".join(inves))
      

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    libidodeum = libidodeum_core(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
