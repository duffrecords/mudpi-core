import os

""" Constants used by MudPi """
MAJOR_VERSION = 0
MINOR_VERSION = 10
PATCH_VERSION = "0"
__version__ = f'{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}'

""" PATHS """
DEFAULT_CONFIG_FILE = "mudpi.config"
PATH_MUDPI = os.getcwd() # /etc/mudpi
PATH_CORE = f"{PATH_MUDPI}/core/mudpi"
PATH_LOGS = f"{PATH_MUDPI}/logs"
PATH_CONFIG = f"{PATH_CORE}"

""" DEFAULTS """
DEFAULT_UPDATE_INTERVAL = 30

""" DATES / TIMES """
MONTHS = {
	'jan': 'January',
	'feb': 'February',
	'mar': 'March',
	'apr': 'April',
	'may': 'May',
	'jun': 'June',
	'jul': 'July',
	'aug': 'August',
	'sep': 'September',
	'oct': 'October',
	'nov': 'November',
	'dec': 'December' }
WEEKDAYS = {
	"mon": 'Monday',
	"tue": 'Tuesday',
	"wed": 'Wednesday',
	"thu": 'Thursday',
	"fri": 'Friday',
	"sat": 'Saturday',
	"sun": 'Sunday' }

""" EVENTS """
EVENT_MUDPI_CLOSE = "mudpi_close"
EVENT_MUDPI_START = "mudpi_start"
EVENT_MUDPI_STARTED = "mudpi_started"
EVENT_MUDPI_STARTING = "mudpi_starting"
EVENT_MUDPI_STOP = "mudpi_stop"
EVENT_MUDPI_STOPPING = "mudpi_stopping"
EVENT_STATE_CHANGED = "state_changed"
EVENT_TIME_CHANGED = "time_changed"
EVENT_SUNSET = "sunset"
EVENT_SUNRISE = "sunrise"
EVENT_CALL_SERVICE = "call_service"


#### Display Characters #####
FONT_RESET_CURSOR = "\x1b[1F"
FONT_RED = "\033[1;31m"
FONT_GREEN = '\033[1;32m'
FONT_YELLOW = "\033[1;33m"
FONT_RESET = "\x1b[0m"
RED_BACK = "\x1b[41;37m"
GREEN_BACK = "\x1b[42;30m"
YELLOW_BACK = "\x1b[43;30m"
FONT_PADDING = 52


""" COMPONENT CLASSIFIERS """
CLASSIFIER_BATTERY = "battery"
CLASSIFIER_CURRENT = "current"
CLASSIFIER_EC = "electrical_conductivity"
CLASSIFIER_ENERGY = "energy"
CLASSIFIER_FLOWMETER = "flowmeter"
CLASSIFIER_HUMIDITY = "humidity"
CLASSIFIER_ILLUMINANCE = "illuminance"
CLASSIFIER_SIGNAL_STRENGTH = "signal_strength"
CLASSIFIER_TEMPERATURE = "temperature"
CLASSIFIER_TIMESTAMP = "timestamp"
CLASSIFIER_MOISTURE = "moisture"
CLASSIFIER_PH = "ph"
CLASSIFIER_PRESSURE = "pressure"
CLASSIFIER_POWER = "power"
CLASSIFIER_POWER_FACTOR = "power_factor"
CLASSIFIER_VOLTAGE = "voltage"
CLASSIFIERS = [
	CLASSIFIER_BATTERY,
	CLASSIFIER_CURRENT,
	CLASSIFIER_EC,
	CLASSIFIER_ENERGY,
	CLASSIFIER_FLOWMETER,
	CLASSIFIER_HUMIDITY,
	CLASSIFIER_ILLUMINANCE,
	CLASSIFIER_SIGNAL_STRENGTH,
	CLASSIFIER_TEMPERATURE,
	CLASSIFIER_TIMESTAMP,
	CLASSIFIER_MOISTURE,
	CLASSIFIER_PH,
	CLASSIFIER_PRESSURE,
	CLASSIFIER_POWER,
	CLASSIFIER_POWER_FACTOR,
	CLASSIFIER_VOLTAGE
]

""" STATES """
STATE_UNKNOWN = "unknown"
STATE_OK = "ok"
STATE_ON = "on"
STATE_OFF = "off"
STATE_HOME = "home"
STATE_AWAY = "away"
STATE_OPEN = "open"
STATE_OPENING = "opening"
STATE_CLOSED = "closed"
STATE_CLOSING = "closing"
STATE_RUNNING = "running"
STATE_STOPPED = "stopped"
STATE_STOPPING = "stopping"
STATE_PAUSED = "paused"
STATE_IDLE = "idle"
STATE_STANDBY = "standby"
STATE_PENDING = "pending"
STATE_LOCKED = "locked"
STATE_UNLOCKED = "unlocked"
STATE_UNAVAILABLE = "unavailable"
STATE_PROBLEM = "problem"

""" ATTRIBUTE NAMES """
ATTR_FRIENDLY_NAME = "name"
ATTR_KEY = "key"
ATTR_ID = "uid"

""" UNITS OF MEASUREMENT """
IMPERIAL_SYSTEM = 1 
METRIC_SYSTEM = 2

# Degree units
DEGREE = "°"

# Temperature units
TEMP_CELSIUS = f"{DEGREE}C"
TEMP_FAHRENHEIT = f"{DEGREE}F"

# Conductivity units
CONDUCTIVITY = f"µS"

# Percentage units
PERCENTAGE = "%"


# #### API / SOCKET ####
SERVER_PORT = 8080

URL_ROOT = "/"
URL_API = "/api/"
URL_API_CONFIG = "/api/config"

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202
HTTP_MOVED_PERMANENTLY = 301
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_UNPROCESSABLE_ENTITY = 422
HTTP_TOO_MANY_REQUESTS = 429
HTTP_INTERNAL_SERVER_ERROR = 500
HTTP_BAD_GATEWAY = 502
HTTP_SERVICE_UNAVAILABLE = 503

HTTP_HEADER_X_REQUESTED_WITH = "X-Requested-With"

CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE_MULTIPART = "multipart/x-mixed-replace; boundary={}"
CONTENT_TYPE_TEXT_PLAIN = "text/plain"

