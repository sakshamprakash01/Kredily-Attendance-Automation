import clock
import schedule
import json
import time
from pprint import pprint

def main():
    sec = 1800
    data = json.load(open('credentials.json'))

    for person in data:
        clockInTime = person["ClockIn"]
        clockOutTime = person["ClockOut"]
        clockDays = person["ClockDays"]
        for day in clockDays:
            exec("schedule.every()."+day+".at(clockInTime).do(clock.clockIn, person)")
            exec("schedule.every()."+day+".at(clockOutTime).do(clock.clockOut, person)")
        
    pprint(schedule.jobs)
    print("Total People = ",len(data))
    print("Total Jobs = ",len(schedule.jobs))
    print("Frequency = "+str(sec)+"s")
    print("SCRIPT RUNNING")

    while True:

        schedule.run_pending()
        # pprint(schedule.jobs)
        # print()
        time.sleep(sec)
                    
if __name__ == "__main__":
    main()
