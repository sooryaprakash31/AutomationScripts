import os, sys, csv


class CheckFile():
    def __init__(self):
        self.folderPath = input("Folder path: ")
        self.filePath = input("File Path: ")
        self.fileFormat = input("File Format without dot: ")
        self.folderPath = self.getPath(self.folderPath)
        self.filePath = self.getPath(self.filePath)
        self.verify()

    def verify(self):
        print(self.filePath, self.folderPath)

        with open(self.filePath,"r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                name = row["name"]
                fileNames = os.listdir(self.folderPath)
                #print(fileNames)
                if str(name+"."+self.fileFormat) in fileNames:
                    print(name," Present")
                else:
                    print(name," Not Present")

    def getPath(self,path):
        return os.path.join(os.path.dirname(__file__),path)

CheckFile()