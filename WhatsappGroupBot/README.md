# Whatsapp Group Bot


## Requirements
- [python3](https://www.python.org/downloads/)
- `pip install selenium`
- Clone of this repository

## SetUp

1. `cd WhatsappGroupBot`
2. Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in the folder
3. Get your FireFox profile path using `about:profiles` and paste it in the `config.ini` file as the value for `PROFILE_PATH`
4. Whatsapp Web must be synced with your account in Firefox browser
5. Enter the exact group name in the `config.ini` file as the value for `GROUP_NAME`
6. Place the `.csv` file with phone number in the column `number` and rename it as `data.csv`

## Execution
1. `cd WhatsappGroupBot`
2. `python3 create_contact_list.py`
   -  `contacts.csv` file will be created
   -  Visit [contacts.google.com](https://contacts.google.com/) and import the `contacts.csv` in the google account which contains contacts visible to your Whatsapp 
3. `python3 add_to_group.py`


## Output
- The `create_contact_list.py` creates `contacts.csv` by converting the numbers in `data.csv` to a valid format that can be imported in Google Contacts.
- The contacts are imported under label `event` 
- `add_to_group.py` uses `data.csv` to add the numbers to the specified Whatsapp group.



