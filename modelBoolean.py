# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 06:14:45 2019

@author: Hassaine
"""

class Boolean:
       def __init__(self,index):
           self.index=index
           
       def boolmodelRequest(self,request):
           from nltk.tokenize import word_tokenize
           request=request.lower()     
           requestWord = word_tokenize(request,language='english',preserve_line='true')      
           boolword=['or','not','and','(',')']
           listFile={}
           #requestWord=request.split()
           for file in self.index:
               fileRequest=request;
               for word in requestWord:
                   if(word not in boolword):
                       if(self.index[file].get(word,None) is not None):
                           fileRequest=fileRequest.replace(word,'True')
                       else:
                           fileRequest=fileRequest.replace(word,'False')
      
               listFile[file]=eval(fileRequest)
           return listFile            