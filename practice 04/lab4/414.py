from datetime import datetime, timedelta

def parse_datetime(line):
    date_part, tz_part = line.split()
    
    # Parse date
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    # Parse timezone offset
    sign = 1 if tz_part[3] == '+' else -1
    hours, minutes = map(int, tz_part[4:].split(":"))
    offset = timedelta(hours=hours, minutes=minutes) * sign
    
    # Convert local midnight to UTC
    return dt - offset


# Input
line1 = input().strip()
line2 = input().strip()

dt1 = parse_datetime(line1)
dt2 = parse_datetime(line2)

# Compute absolute difference in full days
diff_days = abs((dt2 - dt1).total_seconds()) // 86400

print(int(diff_days))