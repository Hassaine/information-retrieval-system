# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:11:02 2019

@author: Hassaine
"""
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from UiController import TestApp
from evaluation import Evaluation

from IndexManager import IndexManager
from modelVectorial import ModelVectorial
import time
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(6.4, 6.4))



def similaireDocs(index,modelVec,queryVec,choixSim):
        filesPoid=[]
        for file in index.index.keys():
        
            fileVec=modelVec.docToVecWeight(index.index,index.inverse,index.ponderer,file)
            
            similarite=modelVec.similarite(fileVec,queryVec,choixSim)
            
            if(similarite > 0.0):                
                filesPoid.append((file,similarite))
            
        filesPoid.sort(key=lambda tup: tup[1],reverse=True)  
        return filesPoid
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    interface = TestApp(dialog)
    dialog.show()
    sys.exit(app.exec_())
    

#     #index.loadIndex()
#     start_time = time.time()
#     index.loadIndex()
#     indexS=index.index
#     print("--- %s seconds ---" % (time.time() - start_time))
     
     
     
#     start_time = time.time()
#     index.createInverse()
#     print("--- %s seconds ---" % (time.time() - start_time))
#
#     start_time = time.time()
#    index.createPonderer()
#    print("--- %s seconds ---" % (time.time() - start_time))

     
#     index.loadIndex('indexs/inverse.p','inverse')
    
    
#    index=IndexManager('corpus')
#    index.loadIndex()
#    index.loadIndex('indexs/inverse.p','inverse')
#    index.loadIndex('indexs/ponderer.p','ponderer')
#    querys = index.loadIndexJson('indexs/queryIndex.json')
#    mv=ModelVectorial()
    
    #evaluer chaque requet donné dans le corpus avec le model vectorial en utilisent la mesure cos
#    queryDocs=[]
#    for queryId in querys:
#        queryVec=mv.reqToVecFromIndex(index.inverse,querys[queryId])
#        
#        queryDocs.append({queryId:similaireDocs(index,mv,queryVec,'cos')})
        
#    
#
#    evaluation = Evaluation('corpus')
#    
#    evaluation.createEvaluationFile('cos')
#    
#   creation du fichier     evaluation_cos.txt
#    for query in queryDocs:  
#        docsFormInit=list(query.values())    
#        evaluation.StoreEvaluationModel(docsFormInit[0],list(query.keys())[0],'cos')
    
    ## chargement des document pertinent pour les requetes
#    queryFile = open('corpus/qrels.text','r').readlines()
#    queryP = {}
#    qid="0"
#    for query in queryFile:
#        query=query.split()
#        if(query[0]!=qid):
#            queryP[query[0]]=[]
#            qid=query[0]
#        queryP[query[0]].append(query[1])

    # chargement des document retourner par le model
    
#    queryFile = open('indexs/evaluation_cos.txt','r').readlines()
#    queryD = {}
#    qid="0"
#    for query in queryFile[1:]:
#        query=query.split(',')
#        if(query[0]!=qid):
#            queryD[query[0]]=[]
#            qid=query[0]
#        queryD[query[0]].append(query[1])
    
    
    #fixer la taille max de resultat et la similarité
#    queryFile = open('corpus/qrels.text','r').readlines()
#    tailleMax = [i for i in range(1,31)]
#    similarites=[0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]   
#    percisionArray=np.zeros([len(queryP),len(tailleMax)])
#    recallArray=np.zeros([len(queryP),len(tailleMax)])
#    recall=[]
#    evaluation = open("indexs/evaluation.txt",'w')
#    evaluation.write("size,similarite,recall,precision\n")
#    
#    # for each size of solution
#    
#    j=0
#    
#    for taille in tailleMax:
#        
#        #for each similarite value
#        #for similarite in similarites:
#            #we construct the Qd ensemble 
#             queryD = {}
#             qid="0"
#             for query in queryFile[1:]:
#                 query=query.split(',')
#                 if(query[0]!=qid):
#                     queryD[query[0]]=[] 
#                     qid=query[0]
#                 if(len(queryD[query[0]])<taille and float(query[2])>=0.2):
#                     queryD[query[0]].append(query[1])
#        
#        
#             recall=0
#             precision=0
#             i=0
#             for query in queryP:
#                PetD=0
#                if(query.startswith("0")):
#                    
#                    queryTmp=query[1:]
#                else:
#                    queryTmp=query
#                        
#                for doc in queryP[query]:   
#                    if(doc in queryD[queryTmp]):                        
#                        PetD+=1
#                if(PetD>0):
#                    percisionArray[i,j]= (PetD)/len(queryD[queryTmp])
#                    recallArray[i,j]=(PetD)/len(queryD[queryTmp])
#                i+=1
#             j+=1
    
                    #precision+=(PetD)/len(queryD[queryTmp])
                    #recall+=(PetD)/len(queryP[query])
             #evaluation.write(str(taille)+','+str(similarite)+','+str(recall/len(queryP))+','+str(precision/len(queryP))+'\n')
    


    #plot the line chart of the avrege recall an precsion for each steps
        
#    avregePrecision =percisionArray.mean(axis=0)            
#    avregeRecall = recallArray.mean(axis=0)
#    plt.figure(figsize=(6.4, 6.4))
#    plt.figure(figsize=(6.4, 6.4))
#    plt.xlabel('recall')
#    plt.ylabel('precision')
#    plt.legend()
#    plt.plot(np.flip(avregeRecall), avregePrecision)
    
    
                 
            
            
        
    
#    evaluation.close()
#    
#    evaluationFile = open('indexs/evaluation.txt','r').readlines()
#    bestTaille=0
#    bestSimilarite=0
#    RdotP=0.0
#    for line in evaluationFile[1:]:
#        line = line.split(',')
#        
#        if(float(line[2])*float(line[3])>RdotP):
#            print('recall: '+line[2]+'precision:'+line[3])
#            bestTaille=int(line[0])
#            bestSimilarite=float(line[1])
#            #print(float(line[2])*float(line[3]))
#            RdotP=float(line[2])*float(line[3])
        
    # best taille 25   best similarite 0.2
    #recall: 0.16304706404411254  precision:0.20189480447577615
    
    


 
#    recall=0
#    precision=0
#    for query in queryP:    
#        PetD=0
#        if(query.startswith("0")):
#            queryTmp=query[1:]       
#        else:        
#            queryTmp=query   
#        for doc in queryP[query]:
#            
#            if(doc in queryD[queryTmp]):
#                PetD+=1
#        print("recall: "+   str((PetD)/len(queryD[queryTmp])))
#        print("precsion: "+   str((PetD)/len(queryP[query])))
#        recall+=(PetD)/len(queryD[queryTmp])
#        precision+=(PetD)/len(queryP[query])
#        
#    print(recall/len(queryP))
#    print(precision/len(queryP))
#        
#        
        
        
            
            
        
        
        
        
        

        #evaluation.StoreEvaluationModel(list(query.keys())[0],query.values())
        
        
#    ponderer=index.ponderer
#    inverse=index.inverse
#    

#    query=mv.reqToVec(index.inverse,"Digital Computers")
#    doc=mv.docToVecWeight(index.index,index.inverse,index.ponderer,'2')
##    print(mv.innerProduct(doc,query))
##    print(mv.coefDeDice(doc,query))
##    print(mv.cosSim(doc,query))
#    print(mv.similarite(doc,query))
#    print(mv.similarite(doc,query,'coefDeDice'))    
#    print(mv.similarite(doc,query,'cos'))
#    print(mv.similarite(doc,query,'Jaccard'))
 
#    evaluation = Evaluation('corpus')
#    evaluation.createQueryIndex()
#    indexManager=IndexManager('corpus')
#    indexqery=indexManager.loadIndexJson('indexs/queryIndex.json')
    
    
    
    