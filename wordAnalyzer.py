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
    
    def orderByFrequency(self):
        freqDict = self.freqAll()
        sorted_dict_by_values = {k: v for k, v in sorted(freqDict.items(), key=lambda x: x[1], reverse=True)}
        return sorted_dict_by_values
    
    def mostFrequentWord(self):
        sorted = self.orderByFrequency()
        keysIter = iter(sorted)
        mostFrequent = next(keysIter)
        frequency= sorted[mostFrequent]
        return f"The most frequent is {mostFrequent} with the frequency of {frequency}"

    def freqOf(self,word):
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0