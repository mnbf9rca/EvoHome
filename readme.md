# EvohomeClient

A simple evohome client designed for my use case (capturing temperature and setpoint data).

## installing

From [PiPy](https://pypi.org/project/evohomeclient-mnbf9rca/)

'pip install evohomeclient-mnbf9rca'

## Usage

main data is retrieved by `get_thermostat_temperatures` which returns a JSON-formatted string:

```json
[
    {
        "datetime"  : "posix timestamp of response",
        "deviceId"  : "Identifier of the device",
        "name"      : "Device name",
        "data"      : { "heatSetpoint"      : "Current heating setpoint",
                        "indoorTemperature" : "Indoor temperature, only if indoorTemperatureStatus='measured'" }
    }
]
```

For example:

```python
# import module
from EvohomeClient import EvohomeClient

# initialise
c = EvohomeClient(username=eh_username, password=eh_password, appid=eh_appid)

# get all locaitons
all_locations = c.get_all_locations()

# get data for each location
for location in all_locations:
    this_location_data = c.get_thermostat_temperatures(location["locationID"])
    print(this_location_data)
```
