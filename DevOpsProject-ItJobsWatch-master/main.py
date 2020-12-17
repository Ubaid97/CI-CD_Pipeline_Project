# from src.cmd_user_interface import CmdUserInterface

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'src'))
import cmd_user_interface

if __name__ == '__main__':
    cmd_user_interface.CmdUserInterface()
