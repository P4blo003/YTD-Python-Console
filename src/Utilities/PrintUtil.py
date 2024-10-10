# ---- Modules ----
import os
from colorama import Fore, Style

# ---- Functions ----
"""
Prints the given message with the label with color.
_msg: Message to print.
_msgLabel: Label of the message.
_msgType: Type of the message.
    0: Error message: Color red.
    1: Warning message: Color yellow.
    2: Info message: Color cyan.
    3: Validation message: Color green.
    Default value is -1: Non color message.
"""
def PrintMessage(_msg : str, _msgLabel : str = "", _msgType : int = -1):
    # -- Local variables
    color = None
    
    # -- Main logic
    if _msgType == -1:  # If the message is default.
        print(f"[{_msgLabel}] : {_msg}")    # Print the message.
        return  # Finish the method.
    
    # Sets the label color.
    if _msgType == 0:
        color = Fore.RED
    elif _msgType == 1:
        color = Fore.YELLOW
    elif _msgType == 2:
        color = Fore.CYAN
    elif _msgType == 3:
        color = Fore.GREEN
    else:
        raise Exception("_msgType is not valid.")   # Raise an exception.

    print(f"[{color}{_msgLabel}{Style.RESET_ALL}] : {_msg}")    # Print the message.
"""
Prints the program information.
_progName: Name of the program.
_progVersion: Version of the program.
_execTime: Time when the program starts.
""" 
def PrintProgramInfo(_progName : str, _progVersion : str, _execTime : str):
    # -- Main logic
    print("-"*os.get_terminal_size().columns)
    print(f"Program name: {_progName}")
    print(f"Program version: {_progVersion}")
    print(f"Execution time: {_execTime}")
    print("-"*os.get_terminal_size().columns)