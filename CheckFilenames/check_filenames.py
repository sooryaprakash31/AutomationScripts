import os, sys, csv


class CheckFiles():
    def __init__(self):
        self.folderPath = input("Folder path: ")
        self.fileFormat = input("File Format without dot: ")
        self.filePath = input("csv File Path: ")
        self.column = input("Column name: ")
        self.folderPath = self.getPath(self.folderPath)
        self.filePath = self.getPath(self.filePath)
        self.verify()

    def verify(self):
        with open(self.filePath,"r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                name = row[self.column]
                fileNames = os.listdir(self.folderPath)
                if str(name+"."+self.fileFormat) not in fileNames:
                    print(name,"-Missing")

    def getPath(self,path):
        return os.path.join(os.path.dirname(__file__),path)

CheckFiles()