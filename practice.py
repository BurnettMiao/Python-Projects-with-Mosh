from datetime import datetime

now = datetime.now()
format_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(format_str)