'''
Desktop tool - Manages the DesktopTool class
'''

# ==================================================
# IMPORTS
# ==================================================

import pyautogui as pg

# ==================================================
# CLASS INIT
# ==================================================

class DesktopTool:
    # * CONSTRUCTOR
    def __init__(
            self,
            pause_threshold: int = 1,
            failsafe: bool = True
    ):
        '''
        Creates an Instance of DesktopTool class.
        Manages the keyboard and mouse movement.
        '''

        self.PAUSE_THRESHOLD = pause_threshold
        self.FAILSAFE = failsafe
        
        pg.PAUSE = self.PAUSE_THRESHOLD
        pg.FAILSAFE = self.FAILSAFE

    # * FUNCTION TO PRESS ANY KEY
    def press_key(self, key: str):
        pg.press(key)

    # * FUNCTION TO WRITE A STRING
    def write_text(self, text: str):
        pg.write(text)

    # * FUNCTION TO PRESS A KEY-COMBINATION
    def press_key_comb(self, *combs):
        pg.hotkey(*combs)