import csv

class CreateContacts:

    numbers = []
    errorNumbers = []
    rows = []

    def __init__(self):
        self.readContacts()
        self.writeContacts()    

    def readContacts(self):
        with open("data.csv","r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if len(row['number'])==10:
                    self.numbers.append(row['number'])
                else:
                    self.errorNumbers.append(row['number'])
            
    def writeContacts(self):
        for i in self.numbers:
            self.rows.append([i,i,'','','','','','','','','','','','','','','','','','','','','','','','','','','event ::: * myContacts','',i])
        
        fields = ['Name','Given Name','Additional Name','Family Name','Yomi Name','Given Name Yomi','Additional Name Yomi','Family Name Yomi','Name Prefix','Name Suffix','Initials','Nickname','Short Name','Maiden Name','Birthday','Gender','Location','Billing Information','Directory Server','Mileage','Occupation','Hobby','Sensitivity','Priority','Subject','Notes','Language','Photo','Group Membership','Phone 1 - Type','Phone 1 - Value']
        
        with open("contacts.csv","w") as csvFile:
            csvwriter = csv.writer(csvFile)  
            csvwriter.writerow(fields)      
            csvwriter.writerows(self.rows)

CreateContacts()