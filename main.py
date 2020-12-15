import clock
import schedule
import json
import time
from pprint import pprint

def main():

    data = json.load(open('credentials.json'))

    clockInTime = data["ClockIn"]
    clockOutTime = data["ClockOut"]
    clockDays = data["ClockDays"]

    for day in clockDays:
        exec("schedule.every()."+day+".at(clockInTime).do(clock.clockIn)")
        exec("schedule.every()."+day+".at(clockOutTime).do(clock.clockOut)")

    while True:

        schedule.run_pending()
        pprint(schedule.jobs)
        print()
        time.sleep(60)
                    
if __name__ == "__main__":
    main()