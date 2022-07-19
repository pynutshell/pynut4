"""
>>> from datetime import datetime
>>> import zoneinfo
>>> d=datetime.now(tz=zoneinfo.ZoneInfo("America/Los_Angeles"))
>>> d
datetime.datetime(2021,10,21,16,32,23,96782,tzinfo=zoneinfo.ZoneInfo(key='America/Los_Angeles'))

# Update the timezone to a different one without changing other attributes
>>> dny=d.replace(tzinfo=zoneinfo.ZoneInfo("America/New_York"))
>>> dny
datetime.datetime(2021,10,21,16,32,23,96782,tzinfo=zoneinfo.ZoneInfo(key='America/New_York'))

# Convert a datetime instance to UTC
>>> dutc=d.astimezone(tz=zoneinfo.ZoneInfo("UTC"))
>>> dutc
datetime.datetime(2021,10,21,23,32,23,96782,tzinfo=zoneinfo.ZoneInfo(key='UTC'))

# Get an aware timestamp of current time in UTC:
>>> dutc=datetime.utcnow().replace(tzinfo=zoneinfo.ZoneInfo("UTC"))
>>> dutc
datetime.datetime(2021,10,21,23,32,23,96782,tzinfo=zoneinfo.ZoneInfo(key='UTC'))

# Convert the datetime instance into a different timezone:
>>> dutc.astimezone(zoneinfo.ZoneInfo("Europe/Rome"))
datetime.datetime(2021,10,22,1,32,23,96782,tzinfo=zoneinfo.ZoneInfo(key='Europe/Rome'))

# Get the local timezone:
>>> tz_local=datetime.now().astimezone().tzinfo
>>> tz_local
datetime.timezone(datetime.timedelta(days=-1, seconds=68400), 'Central Daylight Time')

# Get list of all timezones:
>>> tz_list=zoneinfo.available_timezones()
>>> sorted(tz_list)[0]
'Africa/Abidjan'

"""