'''
Browser tool - Manages the BrowserTool class
'''

# ==================================================
# IMPORTS
# ==================================================

import webbrowser

# ==================================================
# CLASS INIT
# ==================================================

class BrowserTool:
    # * CONSTRUCTOR
    def __init__(self):
        '''
        Creates an Instance of BrowserTool class.
        Manages the browsing functionality of the software.
        '''

        self.engine = webbrowser

    # * FUNCTION TO OPEN A SITE
    def open_site(self, url: str):
        '''
        Opens a URL
        '''

        self.engine.open(url)

    def open_in_new_tab(self, url):
        '''
        Opens a URL in new tab.
        '''

        self.engine.open_new_tab(url)