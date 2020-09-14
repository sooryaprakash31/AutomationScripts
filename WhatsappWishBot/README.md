# WhatsappWishBot
Sends a wish text to the specified contact at midnight through Whatsapp Web

## Setup

- Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in the folder
- Whatsapp Web must be synced with your account in Firefox browser
- Change Firefox default profile path [here](https://github.com/sooryaprakash31/AutomationScripts/blob/master/WhatsappWishBot/send_wish.py#L19)
  - `about:profiles` in Firefox will list the profiles and their paths

## Execution

1. `cd WhatsappWishBot`

2. `python3 send_wish.py`<br>
   
Enter the following data

3. `Contact Name: `<br>
   Exact contact name
4. `Wish Text: `<br>
   Message you want to send 
5. `Sending Date (yyyy-mm-dd): `<br>
   Date in the format yyyy-mm-dd<br>
   Example: <br> 
   `Sending Date (yyyy-mm-dd): 2020-09-14`

## Output
- The given Message will be sent to the Contact at midnight on the date automatically.
  
