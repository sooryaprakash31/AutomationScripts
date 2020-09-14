# TakeABreak
Notifies you and suspends your screen for the specified break time periodically.
## Requirements
- `pip install notify2`

## Setup 
1. `cd TakeABreak`

2. `sudo chmod a+x .break_script.sh`<br>
    The script requires root access for execution (suspending/waking the screen).<br>   
3. `source .break_script.sh`
## Execution

1. `cd TakeABreak`
2. `breakmode <Work-interval> <Break-interval>`<br>
   Example:<br>
    >breakmode 40m 10m
   <table>
   <tr>
   <td>20 seconds </td>
   <td> 20s</td>
   </tr>
   <tr>
   <td>
   20 minutes</td>
   <td>20m</td>
   </tr>
   <tr>
   <td>2 hours</td>
   <td>20h</td>
   </tr>
   </table>

   - Work interval > 10s

## Output

>Carry on. I will notify you when it's break time...

A notification will pop up 10 seconds before the end of work interval and your screen will be suspended for break interval.