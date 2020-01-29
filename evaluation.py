# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:04:05 2019

@author: Hassaine
"""
from IndexManager import IndexManager
from modelVectorial import ModelVectorial

class  Evaluation:
    def __init__(self,corpusdirname):
         self.dirname=corpusdirname
         
         self.indexManager=IndexManager(self.dirname)
         self.querys=self.indexManager.loadIndexJson('indexs/queryIndex.json')
         self.indexManager.loadIndex()
         self.indexManager.loadIndex('indexs/inverse.p','inverse')
         self.indexManager.loadIndex('indexs/ponderer.p','ponderer')
         
         
         
         
    def createQueryIndex(self,indexouput="indexs/queryIndex.json"):
        import string
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        from nltk import defaultdict
        import nltk
        
        defaultindex = defaultdict(int)
        corpus = open(self.dirname+'/'+'query.text','r',encoding='utf8')
        stopWords=set(stopwords.words('english'))
        for line in corpus:
            if(line.startswith('.I')):
                outofDoc=False
                queryid = nltk.re.findall('([\d]+)',line)[0]
                defaultindex[queryid]={}
               
                for line in corpus:
                    if(line.startswith('.W')):
                        for line in corpus:
                            if(line.startswith('.N') or line.startswith('.A')):
                                outofDoc=True
                                break
                            line =line.translate(str.maketrans(' ', ' ', string.punctuation))
                            words=word_tokenize(line,language='english',preserve_line='true')  
                            for word in words:
                                word=word.lower()
                                if(word not in stopWords):       
                                    if(defaultindex[queryid].get(word,None) is None):                                
                                        defaultindex[queryid][word]=0
                                    defaultindex[queryid][word]+=1
                    if(outofDoc):
                        break;
                            
        indexManager = IndexManager(self.dirname)
        indexManager.saveIndexjson(defaultindex,indexouput)
    def StoreEvaluationModel(self,docs,queryId,mesure):
        f = open("indexs\evaluation_"+mesure+".txt",'a+')
        for doc in docs: 
            f.write(queryId+','+str(doc[0])+','+str(doc[1])+'\n')
        f.close()
        

          
    def createEvaluationFile(self,mesure):
        f = open("indexs\evaluation_"+mesure+".txt",'w')
        f.write('queryId,docId,similarite\n')
        f.close()
        
    def similarDocsToQuerys(self,similarite):
        mv = ModelVectorial()
        queryDocs=[]
        for queryId in self.querys:
            queryVec=mv.reqToVecFromIndex(self.indexManger.inverse,self.querys[queryId])
        
            queryDocs.append({queryId:mv.similaireDocs(self.indexManger,mv,queryVec,similarite)})
        return queryDocs
        
    
        
        
        
            
            
        
        
        
        
        
                    
                        
                   
                    
                    
                
                    
            
           
        
        
        
        
        
    
    