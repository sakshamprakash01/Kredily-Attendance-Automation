# Kredily Attendance Automation 

This is an attemp towards automating the 'Clock-In' and 'Clock-Out' actions on Kredily.

## Dependencies
- schedule 0.6.0                        ``` pip install schedule==0.6.0``` 
- selenium 3.141.0                      ``` pip install selenium==3.141.0```
- chromium chrome-driver 1:85.0.4183.83 ```sudo apt-get install chromium-chromedriver```

## Steps to use
- clone the repository and make sure all dependencies are installed.
- edit credentials.json to include the necessary details-
```
{
    "Email": "<Enter your email here>",
    "Password": "<Enter your password here>",
    "ClockIn": "<Enter clock-In time in 24-hrs format>",
    "ClockOut": "Enter clock-Out time in 24-hrs format",
    "ClockDays":["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] //Make sure all days are in lowercase letters with no abbreviations
}
```
- run main.py
