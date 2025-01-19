from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "28132883"))
API_HASH = environ.get("API_HASH", "22eefd902a5b8edfceeeab1487ed60c8")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7052387929:AAEPC4KfaNiyXRxTXcHmyLP9xET0a2yAPZA")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "5601277336")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1001948462404")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
