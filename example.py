from os import getenv

from dotenv import load_dotenv
from EvohomeClient import EvohomeClient


def getEnvVar(var_name):
    """
    fetches an environment variable or raises an exception if not found
    """
    val = getenv(var_name)
    if not val:
        raise Exception(f"can't find envvar {var_name}")
    return val


load_dotenv()
eh_username = getEnvVar("EH_USERNAME")
eh_password = getEnvVar("EH_PASSWORD")
eh_appid = getEnvVar("EH_APPID")

c = EvohomeClient(username=eh_username, password=eh_password, appid=eh_appid)
all_data = c.get_all_locations()
for location in all_data:
    this_location_data = c.get_thermostat_temperatures(location["locationID"])
    print(this_location_data)
