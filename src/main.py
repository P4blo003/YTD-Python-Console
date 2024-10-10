# ---- Modules ----
from config import *
from Utilities import PrintMessage, PrintProgramInfo
from datetime import datetime

# ---- Global variables ----
EXEC_TIME = None    # Time the program starts

# ---- Functions ----

# ---- Main ----
"""
Main program code.
"""
if __name__ == "__main__":
    
    # -- Main logic
    EXEC_TIME=datetime.now().strftime("%H:%M:%S")   # Gets the execution time.
    
    # Print information.
    print()
    PrintMessage("Running program.","INFO",2)
    PrintProgramInfo(PROG_NAME,PROG_VERSION,EXEC_TIME)