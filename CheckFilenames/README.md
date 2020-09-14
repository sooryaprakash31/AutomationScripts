# CheckFileNames
Checks if the files in a folder have names same as the specified column data in the .csv file.

## Execution

1. `cd CheckFilenames`

2. `python3 check_filenames.py`

Enter the following required data 
 
1. `Folder path: `<br>
Path to folder that contains the files. <br>
2. `File Format without dot: `<br>
File format without dot.<br>
3. `File path: `<br>
Path to the **.csv** file. <br>
4. `Column name: `<br>
Column whose data you want to compare with the files.<br>

## Output
The names in the .csv file that don't have associated files in the folder will be listed. <br>
`<name> Missing`