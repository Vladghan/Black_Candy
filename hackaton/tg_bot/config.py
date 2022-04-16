import os
from dotenv import load_dotenv
load_dotenv()

token = str(os.getenv("token"))
admin_ids = os.getenv("admin_ids")[1:-1].replace(" ", "").split(',')
admin_ids = map(int, admin_ids)
admin_ids = list(admin_ids)

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
LOGS_DIR = os.path.join(BASE_DIR, "logs")
