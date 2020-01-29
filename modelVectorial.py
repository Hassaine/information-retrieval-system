# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 01:20:35 2019

@author: Hassaine
"""
import nltk


class ModelVectorial:
    def reqToVecFromIndex(self,inverse,request):
        
        requestVector=[]
        for word in inverse.keys():
            if(request.get(word,None) is not None):
                requestVector.append(request[word])
            else:
                requestVector.append(0)
        return requestVector
        
    
            
    def reqToVec(self,inverse,request):
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize    
        request=request.lower()
        words=word_tokenize(request,language='english',preserve_line='true')
        wd = nltk.FreqDist(words)
        requestVector=[]
        for word in inverse.keys():
            if(wd.get(word,None) is not None):
                requestVector.append(wd[word])
            else:
                requestVector.append(0)
            
       
        return requestVector
    
    def docToVecFreq(self,index,inverse,doc):
        wordlist=index[doc]
        docVector=[]
        for word in inverse.keys():
            if(wordlist.get(word,None) is not None):
                docVector.append(wordlist[word])
            else:
                docVector.append(0)
      
        return docVector
    
    def docToVecWeight(self,index,inverse,ponderer,doc):
        wordlist=index[doc]
        docVector=[]
        for word in inverse.keys():
            if(wordlist.get(word,None) is not None):
                docVector.append(ponderer[word][doc])
            else:
                docVector.append(0)
      
        return docVector
    
    def similarite(self,doc,request,mesure='innerProduct'):
        """
        mesure:   values= 'innerProduct' or 'coefDeDice' or 'cos' or 'Jaccard'
        
        """
        import math
        sommeQry2=0
        sommeDoc2=0
        sommeXY=0
        for i in range(len(doc)):
            sommeQry2+= math.pow(request[i],2) 
            sommeDoc2+= math.pow(doc[i],2)  
            sommeXY+=(doc[i]*request[i])
        if(mesure=='innerProduct'):
            return sommeXY;
        elif(mesure=='coefDeDice'):
            return 2*(sommeXY/(sommeQry2+sommeDoc2))
        elif(mesure=='cos'):
            return (sommeXY/(math.sqrt(sommeQry2*sommeDoc2)))
        elif(mesure=='Jaccard'):
            return (sommeXY/(sommeQry2 + sommeDoc2 - sommeXY))  
        
        
    def similaireDocs(self,index,modelVec,queryVec,choixSim,minSimilarite=0.0):
        filesPoid=[]
        for file in index.index.keys():
        
            fileVec=self.docToVecWeight(index.index,index.inverse,index.ponderer,file)
            
            similarite=self.similarite(fileVec,queryVec,choixSim)
            
            if(similarite > minSimilarite):                
                filesPoid.append((file,minSimilarite))
            
        filesPoid.sort(key=lambda tup: tup[1],reverse=True)  
        return filesPoid        
        


            
            
            
            
        

    

        
