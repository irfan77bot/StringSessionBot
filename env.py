import os
from dotenv import load_dotenv

load_dotenv()

API_ID = "10956858"
API_HASH = "cceefd3382b44d4d85be2d83201102b7"
BOT_TOKEN = "5472138111:AAH-6tavposQ8F8lLSNg7iq_PY_EchlcFCc"
DATABASE_URL = "postgres://lnjrloky:Mpx29iR45y-R8d-R_2SRkAa7VMdSCrEw@rosie.db.elephantsql.com/lnjrloky"
MUST_JOIN = "DS_Botz"

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
