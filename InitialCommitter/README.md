# Initial Committer

Automates Github Initial Commit by using Selenium Webdriver-Python
## Requirements
- [python3](https://www.python.org/downloads/)
- `pip install selenium`
- Clone of this repository

## SetUp

1. Add your Default Projects folder path in [.commands.sh](https://github.com/sooryaprakash31/InitialCommitter/blob/master/.commands.sh#L8) 
2. Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in the folder
3. `cd InitialCommitter`
4. `source .commands.sh`

## Execution
1. `cd InitialCommitter`
2. `createrepo <ProjectName>`

## Output
- A New folder with the `<Project-Name>` will be created in the default projects folder.
- The created folder will be initiated as git repository
- New repository will be created in GitHub with the `<Project-Name>`
- The local repository will be staged, committed "Initial Commit" and pushed to the GitHub repository
