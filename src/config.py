# ---- Modules ----
import os
from dotenv import load_dotenv

load_dotenv()   # Load the variables from the config.env file.

# ---- Variables ----
PROG_NAME = os.getenv("PROG_NAME")
PROG_VERSION = os.getenv("PROG_VERSION")