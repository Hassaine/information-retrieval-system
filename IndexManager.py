# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 04:49:20 2019

@author: Hassaine
"""

from nltk import defaultdict
import math
class IndexManager:
    
    def __init__(self,corpusdirname):
         self.index=defaultdict(int)
         self.inverse=defaultdict(int)
         self.ponderer=defaultdict(int)
         self.dirname=corpusdirname
         

#        self.index=self.loadIndex('indexs/index.p')
#        self.inverse=self.loadIndex('indexs/inverse.p')
        
    
    def createIndex(self,indexouput="indexs/index.p"):
        """
        method for creating the index file a store it into a binary file
        input { dirnmame : directoryName,
               indexouptut : the index output file name
               }
        
        """
        import os
        import string
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        
        import nltk
        listfiles=os.listdir(self.dirname)
        defaultindex = defaultdict(int)
        corpus = open(self.dirname+'/'+listfiles[0],'r',encoding='utf8')
        stopWords=set(stopwords.words('english'))

        for line in corpus:
            #print(line)
        
            if(len(nltk.re.findall('([a-zA-Z]+)',line))==0):
                continue
            if(line.startswith('.I')):
            
                docid = nltk.re.findall('([\d]+)',line)[0]
            
                defaultindex[docid]={}
                for line in corpus:
                
                    
                    if(line.startswith('.T')):
                           
                        for line in corpus:
                        
                        
                            if(line.startswith('.B') or line.startswith('.W')):
                                break
                        
                            line =line.translate(str.maketrans(' ', ' ', string.punctuation))
                            words=word_tokenize(line,language='english',preserve_line='true')                      
                            for word in words:
                                word=word.lower()
                                if(word not in stopWords):
                                    
                                    if(defaultindex[docid].get(word,None) is None):                                
                                        defaultindex[docid][word]=0
                                    defaultindex[docid][word]+=1
                       
            if(line.startswith('.W')):
               
                    for line in corpus:
                   
                        if(line.startswith('.B')):
                            break                        
                        line =line.translate(str.maketrans(' ', ' ', string.punctuation))
                        words=word_tokenize(line,language='english',preserve_line='true')
              
                    for word in words:
                        
                        word=word.lower()
                        if(word not in stopWords):                        
                            if(defaultindex[docid].get(word,None) is None):                           
                                defaultindex[docid][word]=0
                            defaultindex[docid][word]+=1
                        
            if(line.startswith('.X')):
                    break
              
        self.index=defaultindex
        self.saveIndex(defaultindex,indexouput)
    

    def loadIndexJson(self,index='indexs/dataV1.json'):
        """
        loading data methods
        """
        import simplejson as json
        with open(index, 'r') as f:
            return json.load(f)
    
    
    def saveIndexjson(self,index,output='indexs/dataV1.json'):
        """
        loading data methods
        """        
        import simplejson as json
        with open(output, 'w') as fp:
            json.dump(index, fp,sort_keys=True, indent=' ')

    def saveIndex(self,index,output='indexs/data.p'):
        """
        loading data methods
        binary file
        """        
        import pickle
        with open(output, 'wb') as fp:      
            pickle.dump(index, fp, protocol=pickle.HIGHEST_PROTOCOL)
    

    def loadIndex(self,fileName="indexs/index.p",typeToLoad='index'):
        """
        loading data methods
        binary file
        """
        import pickle
        with open(fileName, 'rb') as fp:
            if(typeToLoad=='index'):
                self.index=pickle.load(fp)
            elif(typeToLoad=='inverse'):
                self.inverse=pickle.load(fp)
            else:
                self.ponderer=pickle.load(fp)



    def getFilesByWordFreq(self,word):  

        listfile = defaultdict(int) 
        if( self.inverse.get(word,None) is not None):
            
            for file in self.inverse[word].keys():
                listfile[file]=self.inverse[word][file]
            return listfile
        else:
            return None
        
        
    def getFilesByWordWeight(self,word):  
        if(self.ponderer.get(word,None) is not None):
            
            listfile = defaultdict(int) 
            for file in self.ponderer[word].keys():
                listfile[file]=self.ponderer[word][file]
            return listfile    
        else:
            return None

    def getWordByFileFreq(self,file):

        if(self.index.get(file,None) is not None):
            return self.index[file]
        else:
            return None
      
    def createInverse(self,output='indexs/inverse.p'):         
        inverse=defaultdict(int)
        for file in self.index:       
            for term in self.index[file]:
                if(inverse.get(term,None) is None):
                    inverse[term]={}              
                if(inverse[term].get(file,None) is None):
                    inverse[term][file]=0
                inverse[term][file]+=1       
        self.inverse=inverse
        self.saveIndex(self.inverse,output)
        
    def maxFreque(self,listfreq):
        maxfreq=0
        for item in listfreq.values():
            if(int(item)>maxfreq):
                maxfreq=int(item)
        return maxfreq
    
    
    def createPonderer(self,output='indexs/ponderer.p'):
        dict_inverse_pondere=defaultdict(float)
        N=len(self.index.keys())
        for term in self.inverse.keys():
            dict_inverse_pondere[term]={}
            ni=len(self.inverse[term].keys())
        
            for file in self.inverse[term].keys():
                wordlist = self.getWordByFileFreq(file)  
            
                maxfreq=self.maxFreque(wordlist)          
            
                freqi= int(self.inverse[term][file])    
        
                formule = (freqi/maxfreq)*math.log10((N/ni) +1)
        
                dict_inverse_pondere[term][file] = formule
                
        self.ponderer=dict_inverse_pondere   
        self.saveIndex(self.ponderer,output)

      
      



