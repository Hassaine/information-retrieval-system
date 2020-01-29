import sys

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from IndexManager import IndexManager
from modelBoolean import Boolean
from modelVectorial import ModelVectorial
from ipykernel.kernelapp import IPKernelApp

class TestApp(Ui_MainWindow):


    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.manager = IndexManager('corpus')
        self.manager.loadIndex('indexs/ponderer.p','ponderer')
        self.manager.loadIndex('indexs/inverse.p','inverse')
        self.manager.loadIndex()
        
        
        
        
        self.DisplayInvFile.clicked.connect(self.FDisplayInvFile)
        self.DisplayWInvFile.clicked.connect(self.FDisplayWInvFile)
        self.accesTermButton.clicked.connect(self.FDisplayDocs)                
        self.accesDocsButton.clicked.connect(self.FDisplayTermes)
        self.ModeleBoolButton.clicked.connect(self.FModeleBoolean)
        self.ModeleVectButton.clicked.connect(self.FModeleVectorial)
#        self.ech.clicked.connect(self.RemplirEchantillon)
#        self.ModeleProba.clicked.connect(self.FModeleProba)
    def FDisplayInvFile(self):
#        self.manager.loadIndex()
#        self.manager.loadIndex('indexs/inverse.p','inverse')

        self.tableWidgetInvFile.setRowCount(0)
        
        fichierInverse = self.manager.inverse
        Termes = list(fichierInverse.keys())
        Fichiers= list(self.manager.index.keys())
                
        # Create a empty row at bottom of table
        numRows = self.tableWidgetInvFile.rowCount()
        self.tableWidgetInvFile.insertRow(numRows)
        
        # Add the files name
        i=0
        for f in Fichiers:
            self.tableWidgetInvFile.setItem(numRows,i+1 , QtWidgets.QTableWidgetItem(f))
            i= i+1
        
        for terme in Termes[500:1000]:            
            self.AddRowInvFile(terme,fichierInverse,Fichiers)
            
    def AddRowInvFile(self,terme,fichierInverse,Fichiers):
        
        # Create a empty row at bottom of table
                
        numRows = self.tableWidgetInvFile.rowCount()
        self.tableWidgetInvFile.insertRow(numRows)                    
#        # Add text to the row
        self.tableWidgetInvFile.setItem(numRows,0 , QtWidgets.QTableWidgetItem(terme))
        for j in range(len(Fichiers)):         
            if Fichiers[j] in list(fichierInverse[terme].keys()):
                val = str(fichierInverse[terme][Fichiers[j]])
            else:
                val = "0"
            self.tableWidgetInvFile.setItem(numRows, j+1 , QtWidgets.QTableWidgetItem(val))

               
    def FDisplayWInvFile(self):
        self.tableWidgetInvFile.setRowCount(0)
#        self.manager.loadIndex('indexs/ponderer.p','ponderer')               
        Termes = list( self.manager.ponderer.keys())
        Fichiers= list(self.manager.index.keys())
       
        
        # Create a empty row at bottom of table
        numRows = self.tableWidgetInvFile.rowCount()
        self.tableWidgetInvFile.insertRow(numRows)
        
        # Add the files name
        i=0
        for f in Fichiers:
            self.tableWidgetInvFile.setItem(numRows,i+1 , QtWidgets.QTableWidgetItem("d"+str(f)))
            i= i+1
        
        for terme in Termes[500:800]:            
            self.AddRowInvFile(terme,self.manager.ponderer,Fichiers)
            
    def FDisplayDocs(self):
        self.tableWidgetDocs.setRowCount(0);
        term=self.accesTerm.text()
        term=term.lower()
#        self.manager.loadIndex('indexs/ponderer.p','ponderer')
#        self.manager.loadIndex('indexs/inverse.p','inverse')
        listfileFreq=self.manager.getFilesByWordFreq(term)
        listfilePoid=self.manager.getFilesByWordWeight(term)
        numrows=self.tableWidgetDocs.rowCount()
        self.tableWidgetDocs.insertRow(numrows)   
        if(listfileFreq is not None):
            
            for file in listfileFreq.keys():
                self.tableWidgetDocs.setItem(numrows,0,QtWidgets.QTableWidgetItem(file))
                self.tableWidgetDocs.setItem(numrows,1,QtWidgets.QTableWidgetItem(str(listfileFreq[file])))
                self.tableWidgetDocs.setItem(numrows,2,QtWidgets.QTableWidgetItem(str(listfilePoid[file])))
                numrows = self.tableWidgetDocs.rowCount()        
                self.tableWidgetDocs.insertRow(numrows)
                
        else:
                self.tableWidgetDocs.setItem(numrows,0,QtWidgets.QTableWidgetItem("term dont exist in the corpus"))
                self.tableWidgetDocs.setItem(numrows,1,QtWidgets.QTableWidgetItem("0"))
                self.tableWidgetDocs.setItem(numrows,2,QtWidgets.QTableWidgetItem('0'))
                numrows = self.tableWidgetDocs.rowCount()      
                self.tableWidgetDocs.insertRow(numrows)
   
    
    def FDisplayTermes(self):
        
        self.tableWidgetDocs.setRowCount(0)
        doc=self.accesdocs.text()
       
        listwords=self.manager.index[doc]
        numrows=self.tableWidgetTermes.rowCount()
        self.tableWidgetTermes.insertRow(numrows)   
        if(listwords is not None):
            
            for word in listwords.keys():
                self.tableWidgetTermes.setItem(numrows,0,QtWidgets.QTableWidgetItem(word))
                self.tableWidgetTermes.setItem(numrows,1,QtWidgets.QTableWidgetItem(str(self.manager.inverse[word][doc])))
                self.tableWidgetTermes.setItem(numrows,2,QtWidgets.QTableWidgetItem(str(self.manager.ponderer[word][doc])))
                numrows = self.tableWidgetTermes.rowCount()        
                self.tableWidgetTermes.insertRow(numrows)
                
        else:
                self.tableWidgetTermes.setItem(numrows,0,QtWidgets.QTableWidgetItem("term dont exist in the corpus"))
                self.tableWidgetTermes.setItem(numrows,1,QtWidgets.QTableWidgetItem("0"))
                self.tableWidgetTermes.setItem(numrows,2,QtWidgets.QTableWidgetItem('0'))
                numrows = self.tableWidgetTermes.rowCount()      
                self.tableWidgetTermes.insertRow(numrows)
    def FModeleBoolean(self):
        self.tableWidgetDocsBool.setRowCount(0)
#        self.manager.loadIndex()
        boolObject = Boolean(self.manager.index)
        files=boolObject.boolmodelRequest(self.requetBool.text())
        numrows=self.tableWidgetDocsBool.rowCount()
        self.tableWidgetDocsBool.insertRow(numrows) 
        for file in files.keys():
            if(files[file]):               
                self.tableWidgetDocsBool.setItem(numrows,0,QtWidgets.QTableWidgetItem(file))
                numrows = self.tableWidgetDocsBool.rowCount()        
                self.tableWidgetDocsBool.insertRow(numrows)



    def similaireDocs(self,modelVec,queryVec,choixSim):
        filesPoid=[]
        for file in self.manager.index.keys():
        
            fileVec=modelVec.docToVecWeight(self.manager.index,self.manager.inverse,self.manager.ponderer,file)
            
            similarite=modelVec.similarite(fileVec,queryVec,choixSim)
            
            if(similarite >= 0.2):                
                filesPoid.append((file,similarite))
           
            
        filesPoid.sort(key=lambda tup: tup[1],reverse=True)  
        return filesPoid

    def FModeleVectorial(self):
        
        self.tableWidgetDocsVect.setRowCount(0);
        choixSim = str(self.comboBox.currentText())
#        self.manager.loadIndex('indexs/ponderer.p','ponderer')
#        self.manager.loadIndex('indexs/inverse.p','inverse')
#        self.manager.loadIndex()
        
        query=self.requetVec.text()
        mv=ModelVectorial()
        
        queryVec=mv.reqToVec(self.manager.inverse,query)
        numrows=self.tableWidgetDocsVect.rowCount()  
        self.tableWidgetDocsVect.insertRow(numrows)        
        
        filesPoid =self.similaireDocs(mv,queryVec,choixSim)
        for element in filesPoid:            
            self.tableWidgetDocsVect.setItem(numrows,0,QtWidgets.QTableWidgetItem(element[0]))
            self.tableWidgetDocsVect.setItem(numrows,1,QtWidgets.QTableWidgetItem(str(element[1])))
            numrows=self.tableWidgetDocsVect.rowCount()  
            self.tableWidgetDocsVect.insertRow(numrows)
            
    def Evaluation(self):
        return 0
        
        
            
            
        
        
        
            
            
            
        
        
        
        
        
        
                    
        
        
        
#
#if __name__ == '__main__':
#    app = QtWidgets.QApplication(sys.argv)
#    dialog = QtWidgets.QMainWindow()
#
#    interface = TestApp(dialog)
#
#    dialog.show()
#    sys.exit(app.exec_())