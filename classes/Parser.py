import os

class Parser:
    files = []
    
    # Main Parsing Class
    def parse(self, folder):
        files = os.listdir(folder)
        for file in files:
            if(file == '.DS_Store'):
                continue
            
            with open (os.path.join(folder,file), "r") as phpFile:
                data = phpFile.read()
                
            className = self.findClassName(data)
            print(className)
            
    def findClassName(self, fileContents):
        return 'this is a file'