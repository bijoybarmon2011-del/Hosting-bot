"""
╔═══════════════════════════════════════════════════════════╗
║  🌟BIJOY HOSTING PANEL — Premium Edition v6.0 🌟         ║
║  Developer: @bijoy_vai2                               ║
║  Config File — All Settings Here                          ║
╚═══════════════════════════════════════════════════════════╝
"""


import os
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════════════════
# BOT TOKENS
# ═══════════════════════════════════════════════════
# Keep all credentials in the hosting provider's Environment Variables.
# Never commit Telegram tokens to GitHub.

BOT_TOKEN = "9083606771:AAFdVRbnkUXaI1cT7Wx6zCuqsnr38Yanfsk"

OWNER_ID_VALUE = "8817321100"

TOKEN = BOT_TOKEN.strip()
ERROR_BOT_TOKEN = os.environ.get("ERROR_BOT_TOKEN", "").strip()

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

# ═══════════════════════════════════════════════════
# MONGODB — PRIMARY + SECONDARY FALLBACK
# ═══════════════════════════════════════════════════
MONGO_URL = os.environ.get('MONGO_URL', '')
MONGO_URL_BACKUP = os.environ.get('MONGO_URL_BACKUP', '')
DB_NAME = '@premium_vps_hosting_bot'

# Storage alert thresholds (MB)
DB_STORAGE_WARN_MB = int(
    os.environ.get('DB_STORAGE_WARN_MB', '400')
)
DB_STORAGE_LIMIT_MB = int(
    os.environ.get('DB_STORAGE_LIMIT_MB', '490')
)

# ═══════════════════════════════════════════════════
# OWNER & ADMIN
# ═══════════════════════════════════════════════════
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID_VALUE))

# Set the numeric Telegram user ID here.
ADMIN_ID = int(os.environ.get('ADMIN_ID', str(OWNER_ID)))

BOT_USERNAME = 'premium_vps_hosting_bot'
YOUR_USERNAME = '@bijoy_vai2'
UPDATE_CHANNEL = 'https://t.me/bijoy_bhai_ff'

# ═══════════════════════════════════════════════════
# DIRECTORIES
# ═══════════════════════════════════════════════════

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Railway/Render: attach a persistent disk at /data and set DATA_DIR=/data.
# Local development falls back to the project directory.
_DEFAULT_DATA_DIR = '/data' if os.path.isdir('/data') and os.access('/data', os.W_OK) else os.path.join(BASE_DIR, 'premium_data')
DATA_DIR = os.path.abspath(os.environ.get('DATA_DIR') or _DEFAULT_DATA_DIR)
UPLOAD_DIR = os.path.join(DATA_DIR, 'upload_bots')
LOGS_DIR = os.path.join(DATA_DIR, 'logs')
BACKUP_DIR = os.path.join(DATA_DIR, 'backups')

for _d in [UPLOAD_DIR, DATA_DIR, LOGS_DIR, BACKUP_DIR]:
    os.makedirs(_d, exist_ok=True)

# Safely migrate the old project-local runtime directory into a newly attached
# persistent volume. Existing files on the volume are never overwritten.
_LEGACY_DATA_DIR = os.path.join(BASE_DIR, 'premium_data')
if os.path.isdir(_LEGACY_DATA_DIR) and os.path.realpath(_LEGACY_DATA_DIR) != os.path.realpath(DATA_DIR):
    import shutil
    for _root, _dirs, _files in os.walk(_LEGACY_DATA_DIR):
        _rel = os.path.relpath(_root, _LEGACY_DATA_DIR)
        _target_root = DATA_DIR if _rel == '.' else os.path.join(DATA_DIR, _rel)
        os.makedirs(_target_root, exist_ok=True)
        for _filename in _files:
            _src_file = os.path.join(_root, _filename)
            _dst_file = os.path.join(_target_root, _filename)
            if not os.path.exists(_dst_file):
                try:
                    shutil.copy2(_src_file, _dst_file)
                except OSError:
                    pass

# One-time migration of legacy uploads into persistent storage.
_LEGACY_UPLOAD_DIR = os.path.join(BASE_DIR, 'upload_bots')
if os.path.isdir(_LEGACY_UPLOAD_DIR) and os.path.realpath(_LEGACY_UPLOAD_DIR) != os.path.realpath(UPLOAD_DIR):
    import shutil
    for _name in os.listdir(_LEGACY_UPLOAD_DIR):
        _src = os.path.join(_LEGACY_UPLOAD_DIR, _name)
        _dst = os.path.join(UPLOAD_DIR, _name)
        if not os.path.exists(_dst):
            try:
                if os.path.isdir(_src):
                    shutil.copytree(_src, _dst)
                elif os.path.isfile(_src):
                    shutil.copy2(_src, _dst)
            except OSError:
                pass

# ═══════════════════════════════════════════════════
#  BRANDING
# ═══════════════════════════════════════════════════
BRAND        = "🌟 PREMIUM VPS PANEL"
BRAND_SHORT  = "MS"
BRAND_VER    = "v6.0"
BRAND_TAG    = f"{BRAND} {BRAND_VER}"
BRAND_FOOTER = f"\n━━━━━━━━━━━━━━━━━━━━\n{BRAND_TAG}"

# ═══════════════════════════════════════════════════
#  FORCE SUBSCRIBE
# ═══════════════════════════════════════════════════
DEFAULT_FORCE_CHANNELS = {'bijoy_vai2': 'Developer Bijoy Updates'}

# ═══════════════════════════════════════════════════
#  PLAN LIMITS
# ═══════════════════════════════════════════════════
PLAN_LIMITS = {
    'free':       {'name': '🆓 Free',        'max_bots': 1,  'ram': 128,  'auto_restart': False, 'price': 0},
    'starter':    {'name': '🟢 Starter',     'max_bots': 2,  'ram': 256,  'auto_restart': False,  'price': 99},
    'basic':      {'name': '⭐ Basic',        'max_bots': 5,  'ram': 512,  'auto_restart': False,  'price': 199},
    'pro':        {'name': '💎 Pro',          'max_bots': 15, 'ram': 2048, 'auto_restart': False,  'price': 499},
    'enterprise': {'name': '🏢 Enterprise',   'max_bots': 50, 'ram': 4096, 'auto_restart': False,  'price': 999},
    'lifetime':   {'name': '👑 Lifetime',     'max_bots': -1, 'ram': 8192, 'auto_restart': False,  'price': 1999},
}

# ═══════════════════════════════════════════════════
#  PAYMENT METHODS
# ═══════════════════════════════════════════════════
PAYMENT_METHODS = {
    'bkash':   {'name': 'bKash',       'number': '01749454422',            'type': 'Send Money',       'icon': '🟪'},
    'nagad':   {'name': 'Nagad',       'number': '',            'type': 'Send Money',       'icon': '🟧'},
    'rocket':  {'name': 'Rocket',      'number': '',            'type': 'Send Money',       'icon': '🟦'},
    'upay':    {'name': 'Upay',        'number': '',            'type': 'Send Money',       'icon': '🟩'},
    'binance': {'name': 'Binance Pay', 'number': 'Binance ID: not id⛔', 'type': 'Binance Pay/USDT', 'icon': '🟡'},
    'bank':    {'name': 'Bank',        'number': 'Contact Admin',          'type': 'Transfer',         'icon': '🏦'},
}

# ═══════════════════════════════════════════════════
#  REFERRAL SETTINGS
# ═══════════════════════════════════════════════════
REF_BONUS_DAYS = 3
REF_COMMISSION = 20

# ═══════════════════════════════════════════════════
#  MODULE MAP (for auto-install)
# ═══════════════════════════════════════════════════
MODULES_MAP = {
    # import name -> pip package name
    'telebot': 'pyTelegramBotAPI', 'telegram': 'python-telegram-bot',
    'pyrogram': 'pyrogram', 'telethon': 'telethon', 'aiogram': 'aiogram',
    'PIL': 'Pillow', 'cv2': 'opencv-python-headless', 'sklearn': 'scikit-learn',
    'bs4': 'beautifulsoup4', 'dotenv': 'python-dotenv', 'yaml': 'pyyaml',
    'aiohttp': 'aiohttp', 'numpy': 'numpy', 'pandas': 'pandas',
    'requests': 'requests', 'flask': 'flask', 'fastapi': 'fastapi',
    'motor': 'motor', 'pymongo': 'pymongo', 'httpx': 'httpx',
    'cryptography': 'cryptography',
    'Crypto': 'pycryptodome', 'Cryptodome': 'pycryptodomex',
    'jwt': 'PyJWT', 'dateutil': 'python-dateutil', 'psycopg2': 'psycopg2-binary',
    'MySQLdb': 'mysqlclient', 'serial': 'pyserial', 'discord': 'discord.py',
    'googleapiclient': 'google-api-python-client', 'google': 'google-api-python-client',
    'redis': 'redis', 'yt_dlp': 'yt-dlp', 'youtube_dl': 'youtube_dl',
    'speech_recognition': 'SpeechRecognition', 'gtts': 'gTTS', 'pytz': 'pytz',
    'qrcode': 'qrcode', 'pyfiglet': 'pyfiglet', 'colorama': 'colorama',
    'termcolor': 'termcolor', 'tqdm': 'tqdm', 'aiofiles': 'aiofiles',
    'aiosqlite': 'aiosqlite', 'lxml': 'lxml', 'uvicorn': 'uvicorn',
    'websockets': 'websockets', 'websocket': 'websocket-client',
    'socks': 'PySocks', 'nacl': 'PyNaCl', 'OpenSSL': 'pyOpenSSL',
    'attr': 'attrs', 'magic': 'python-magic', 'docx': 'python-docx',
    'pptx': 'python-pptx', 'fitz': 'PyMuPDF', 'PyPDF2': 'PyPDF2',
    'matplotlib': 'matplotlib', 'scipy': 'scipy', 'openai': 'openai',
    'anthropic': 'anthropic', 'schedule': 'schedule', 'apscheduler': 'APScheduler',
    'pyshorteners': 'pyshorteners', 'faker': 'Faker', 'emoji': 'emoji',
    'flask_cors': 'flask-cors', 'flask_sqlalchemy': 'Flask-SQLAlchemy',
    'sqlalchemy': 'SQLAlchemy', 'pydantic': 'pydantic', 'jinja2': 'Jinja2',
    'telegraph': 'telegraph', 'instaloader': 'instaloader', 'tgcrypto': 'TgCrypto',
    'psutil': 'psutil', 'pymysql': 'PyMySQL', 'bson': 'pymongo',
    'dns': 'dnspython', 'ujson': 'ujson', 'orjson': 'orjson',
}

# Maximum number of automatic "install missing module, then start again"
# rounds for a single start request. A big bot can need many packages.
MAX_DEP_RETRIES = int(os.environ.get('MAX_DEP_RETRIES', '25'))

# Host protection: a child bot using more than RAM_HARD_FACTOR x its plan RAM
# is stopped so one heavy upload cannot take the whole hosting panel down.
# Set RAM_HARD_FACTOR=0 to disable.
RAM_HARD_FACTOR = float(os.environ.get('RAM_HARD_FACTOR', '3'))

# ═══════════════════════════════════════════════════
#  FLASK PORT
# ═══════════════════════════════════════════════════
FLASK_PORT = int(os.environ.get("PORT", 8080))

# ═══════════════════════════════════════════════════
#  DAILY REPORT (24h format, server time)
# ═══════════════════════════════════════════════════
DAILY_REPORT_HOUR   = int(os.environ.get('DAILY_REPORT_HOUR',   '0'))   # 0 = midnight
DAILY_REPORT_MINUTE = int(os.environ.get('DAILY_REPORT_MINUTE', '0'))

# ═══════════════════════════════════════════════════
#  FREE PLAN BOT LIMIT
# ═══════════════════════════════════════════════════
# Free plan bots auto-stop after this many hours (0 = disabled)
FREE_BOT_MAX_HOURS  = int(os.environ.get('FREE_BOT_MAX_HOURS', '0'))

# ═══════════════════════════════════════════════════
#  MAIN BOT AUTO-RESTART (every 24h)
# ═══════════════════════════════════════════════════
# Set MAIN_BOT_AUTO_RESTART_HOURS to 0 to keep scheduled restarts disabled.
MAIN_BOT_AUTO_RESTART_HOURS = int(os.environ.get('MAIN_BOT_AUTO_RESTART_HOURS', '0'))
