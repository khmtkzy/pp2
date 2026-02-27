import sys
from datetime import datetime, timedelta, timezone

def parse_line(line):
    # Format: YYYY-MM-DD HH:MM:SS UTC±HH:MM
    date_part, time_part, tz_part = line.strip().split()
    
    year, month, day = map(int, date_part.split('-'))
    hour, minute, second = map(int, time_part.split(':'))
    
    sign = 1 if tz_part[3] == '+' else -1
    tz_hour = int(tz_part[4:6])
    tz_min = int(tz_part[7:9])
    
    offset = timedelta(hours=tz_hour, minutes=tz_min) * sign
    tz = timezone(offset)
    
    dt = datetime(year, month, day, hour, minute, second, tzinfo=tz)
    return dt.astimezone(timezone.utc)

# Read input
start_line = sys.stdin.readline()
end_line = sys.stdin.readline()

start_utc = parse_line(start_line)
end_utc = parse_line(end_line)

# Compute duration in seconds
duration = int((end_utc - start_utc).total_seconds())
print(duration)