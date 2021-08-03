import re

class Preprocessor():
    """Preprocess some generalised formats."""
    def __init__(self):
        pass

    def preprocess(self, line):
        # IP Adresses
        line = re.sub('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*' , '<ip>', line)
        # Time
        line = re.sub('(\d{1,2}):(\d{1,2}):(\d{2}) ?([AaPp][Mm])', '<time>', line) 
        
        # Different formats of date, whichever matches
        # Taken from - 1. https://stackoverflow.com/questions/51224/regular-expression-to-match-valid-dates
        # 2. https://stackoverflow.com/questions/51122413/regex-for-extracting-all-complex-dates-formats-from-a-string-in-python/51122557
        
        # DDMMYY with any seperator
        line = re.sub('(0?[1-9]|[12]\d|30|31)[^\w\d\r\n:](0?[1-9]|1[0-2])[^\w\d\r\n:](\d{4}|\d{2})', '<date>', line)
        # Matches dates with month spelled out (first 3 letters)
        line = re.sub('^((31(?! (FEB|APR|JUN|SEP|NOV)))|((30|29)(?! FEB))|(29(?= FEB (((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00)))))|(0?[1-9])|1\d|2[0-8])-(JAN|FEB|MAR|MAY|APR|JUL|JUN|AUG|OCT|SEP|NOV|DEC)-((1[6-9]|[2-9]\d)\d{2})$', '<date>', line)
        line = re.sub('(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{2,4})+', '<date>', line)
        

        return line