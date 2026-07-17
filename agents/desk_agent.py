'''
Works on the desktop on the behalf of the user.
'''

# ==================================================
# IMPORTS
# ==================================================

import logging

from tools.app_tool import AppTool
from tools.desktop_tool import DesktopTool
from tools.browser_tool import BrowserTool

# ==================================================
# SETUP
# ==================================================

logging.basicConfig(level=logging.ERROR)

# ==================================================
# CLASS INIT
# ==================================================

class DeskAgent:
    # * CONSTRUCTOR
    def __init__(self):
        '''
        Manages the desktop operations.
        '''

        self.app_tool = AppTool()
        self.desk_tool = DesktopTool()
        self.web_tool = BrowserTool()

    # * FUNCTION TO EXECUTE A TASK
    def execute_task(self, action: str, data: str):
        '''
        Executes a desktop task.
        '''

        if (action == "open_app"):
            self.app_tool.open_app(data)

        elif (action == "close_app"):
            self.app_tool.close_app(data)

        elif (action == 'open_site'):
            self.web_tool.open_site(data)