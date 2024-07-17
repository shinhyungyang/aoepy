import datetime as dt
import locale
import pytz
import sys
import time

# https://stackoverflow.com/a/13218990/936369
def localTzname():
  if time.daylight:
    offsetHour = time.altzone / 3600
  else:
    offsetHour = time.timezone / 3600
  return 'Etc/GMT%+d' % offsetHour

'''
Expects an RFC 3339 date string. E.g., on Linux:
$ ./AoE.py "`date --rfc-email`"
'''

locale.setlocale(locale.LC_ALL, "")

if len(sys.argv) != 2:
  print("{}\n{}\n{}\n{}\n{}\n{}".format(
      "Error:",
      "  AoE.py expects one command-line argument as a date string.",
      "Usage:",
      "  $ python3 ./AoE.py \"2024-08-19 23:59:59\"",
      "  Anywhere on Earth: 2024-08-19 23:59:59-12:00",
      "  System's Timezone: 2024-08-20 13:59:59+02:00"))
  sys.exit(1)

# For example:
# 2006-08-14 02:34:56-12:00
# Convrt an RFC 3339 string w/o tzinfo to an ISO 8601 string w/ AoE
AoE="-12:00"
AoEDateStr="{}{}".format(sys.argv[1].replace(" ", "T"), AoE)
now = dt.datetime.fromisoformat(AoEDateStr)
print("Anywhere on Earth: {}".format(now))
print("System's Timezone: {}".format(now.astimezone(pytz.timezone(localTzname()))))
#print(now.strftime("%a %d. %b %H:%M:%S %Z %Y"))
