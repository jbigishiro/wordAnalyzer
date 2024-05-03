class TextAnalyzer(object):
    
    def __init__ (self, text):
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')      
        formattedText = formattedText.lower()    
        self.fmtText = formattedText