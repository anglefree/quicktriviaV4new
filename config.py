
import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "v4updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/94ecff937a040006cec9a.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Qtmusicv4")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "v4updatesdiscussion")
PROJECT_NAME = getenv("PROJECT_NAME", "quicktriviaV4")
SOURCE_CODE = getenv("SOURCE_CODE", "https://telegra.ph/file/776826cc26ba5897a9ec2.mp4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
