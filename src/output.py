import sys
import re

class Output():
    """Class to output the clustered log files"""
    def __init__(self):
        self.CRED = '\33[31m'
        self.CYELLOW = '\33[33m'
        self.CEND = '\033[0m'
        self.placeholder = '----'

    def color_placeholders(self, word):
        """Color the placeholder or converted generalised values"""
        if word == self.placeholder or re.match(r'<\w+>', word):
            word = self.CRED + word + self.CEND
        return word

    def print_results(self, clusters):
        """Clean the data and print to the console"""
        print_data = []

        for line in clusters:
            count = self.CYELLOW + str(line[1]) + ' ' + self.CEND
            
            # Color the placeholders with red
            line[0] = map(self.color_placeholders, line[0])
            
            line = count + (' '.join(line[0]))
            print_data.append(line)
        
        for line in print_data:
            print(line)
        

    