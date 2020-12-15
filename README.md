# Kredily Attendance Automation Script

This is an attemp towards automating the 'Clock-In' and 'Clock-Out' actions on Kredily.

## Dependencies
- schedule 0.6.0
- selenium 3.141.0
- chromium chrome-driver 1:85.0.4183.83

## Steps to use
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
