import pytz, sys
from datetime import datetime
from pytz import timezone

def check_conflicts(zone1, zone2, exclusive_duration = 9, overlap=0):
    
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    time1 = datetime.now(timezone(zone1))
    time2 = datetime.now(timezone(zone2))
    hour1 = time1.hour + time1.minute/60.0
    hour2 = time2.hour + time2.minute/60.0
    
    if hour1 < hour2:
        if hour1 + exclusive_duration > hour2:
            return False
        else:
            return True
    else:
        if hour2 + exclusive_duration > hour1:
            return False
        else:
            return True

def generate_all_compatible_timezones():
    outFile = open('compatible_timezones.txt','w')
    for zone1 in pytz.common_timezones:
        for zone2 in pytz.common_timezones:
            if zone1 != zone2:
                if check_conflicts(zone1, zone2, 9):
                    outFile.write(zone1 + ' : '+zone2+'\n')

 
def get_compatible_timezones(from_timezone):
    result = []
    for zone in pytz.common_timezones:
        if from_timezone != zone:
            if check_conflicts(from_timezone, zone, 9):
                result.append(zone)
                

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print "USAGE:  python colocator.py  <<<TIME_ZONE>>>"
        return
    
    from_timezone = sys.argv
    print get_compatible_timezones(from_timezone)
    
#     # Usage for checking conflicts b/w 2 given timezones
#     zone2 = 'US/Pacific'
#     zone1 = 'Asia/Calcutta'
#     print check_conflicts(zone1, zone2, 9)
    

#     # Usage for generating all possible conflicts free timezones
#     generate_all_compatible_timezones()
