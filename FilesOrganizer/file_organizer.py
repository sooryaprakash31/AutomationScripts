import os
from pathlib import Path
class FileOrganizer():
    def __init__(self):
        stop=0
        while stop==0:
            self.folder = input("Folder Path: ")
            self.folderPath = self.getPath(self.folder)
            if os.path.exists(self.folderPath):
                stop=1
                self.organize()
            else:
                print("Invalid Path")
    
    def organize(self):
        
        folderNames={    
            "HTML": [".html5", ".html", ".htm", ".xhtml"], 
            "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
                    ".heif", ".psd"], 
            "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
                    ".qt", ".mpg", ".mpeg", ".3gp"], 
            "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                        ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                        ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                        ".pptx",".csv"], 
            "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
                        ".dmg", ".rar", ".xar", ".zip"], 
            "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
                    ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
            "PLAINTEXT": [".txt", ".in", ".out"], 
            "PDF": [".pdf"], 
            "PYTHON": [".py"], 
            "XML": [".xml"], 
            "EXE": [".exe"], 
            "SHELL": [".sh"] 
            }
        
        #assigns every file format with the folder name from the above dict
        fileFormats = {fileFormat: folderName 
                for folderName, file_formats in folderNames.items() 
                for fileFormat in file_formats} 
        #print(fileFormats)
        for i in os.scandir(self.folderPath):
            if i.is_dir():
                continue
            if os.path.isfile(Path(i)):
                filePath=Path(i)
                fileType = filePath.suffix.lower()
                if fileType in fileFormats:
                    newPath = os.path.join(self.folderPath,Path(fileFormats[fileType]))
                else:
                    newPath = os.path.join(self.folderPath,Path("OTHERS"))                
                if not os.path.exists(newPath):
                    os.mkdir(newPath)
                newPath=newPath+"/"+i.name
                filePath.rename(Path(newPath))

    def getPath(self,path):
        return os.path.join(os.path.dirname(__file__),path)

FileOrganizer()