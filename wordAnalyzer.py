class TextAnalyzer(object):
    
    def __init__ (self, text):
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')      
        formattedText = formattedText.lower()    
        self.fmtText = formattedText

    def freqAll(self):        
        wordList = self.fmtText.split(' ')
        freqMap = {}
        for word in set(wordList): 
            freqMap[word] = wordList.count(word)   
        return freqMap
    