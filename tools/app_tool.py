'''
App tool - Manages the AppTool class
'''

# ==================================================
# IMPORTS
# ==================================================

import AppOpener

# ==================================================
# CLASS INIT
# ==================================================

class AppTool:
    # * CONSTRUCTOR
    def __init__(self):
        '''
        Creates an Instance of AppTool class.
        Manages the app opening/closing functionality of the software.
        '''

        self.engine = AppOpener

    # * FUNCTION TO OPEN AN APP
    def open_app(self, app: str):
        '''
        Opens an app.

        :param app: App name to open.
        '''

        self.engine.open(app)
    
    # * FUNCTION TO CLOSE AN APP
    def close_app(self, app: str):
        '''
        Closes an app.

        :param app: App name to close.
        '''

        self.engine.close(app)