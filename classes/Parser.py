import os
import re

class Parser:
    files = []
    classNames = []
    classesFound = 0
    
    # Main Parsing Class
    def parse(self, folder):
        files = os.listdir(folder)
        for file in files:
            if(file.startswith('.') or file.startswith('__')):
                continue
            
            with open(os.path.join(folder,file), "r") as phpFile:
                data = phpFile.read()
                
            className = self.findClassName(data)
            if not className :
                continue

            self.classesFound = self.classesFound + 1
            self.classNames.append(className)

        print '---------------------------'
        print('Total classes found: {0}'.format(self.classesFound))
        print '\n'.join(self.classNames)
        print '---------------------------'
            
    def findClassName(self, fileContents):
        result = re.search("class ([a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)", fileContents)
        if not result:
            return None

        name = result.group(0)
        name = name.replace('class ', '')

        return name