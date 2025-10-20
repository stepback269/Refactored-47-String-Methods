#print(f'Date: 10/20_D3/2025   current editing line = search for "NEW"  = get_keystroke() function')

print(f'(3) The importation of Package_03 / funcs_02 into memory has begun')
# check out the Data Engineer: https://www.youtube.com/@GambillDataEngineering

from . import vars_01 as v  #-- google "python syntax of an import from statement"
from . import mssgs_01 as msg
import keyboard
import pyautogui as gu
import webbrowser
import pyshorteners
'''
Although the MAIN module imports all the necessary module codes, this module must import the name-space aspects
of those modules, namely, those of the vars_01 module plus those of the mssgs_01 module 
'''

# Use in PyCharm: Ctrl + Shft + x to insert hash tag (#) and advance to next line (was used immediately below)
# ----------------------------------------------

def get_keystroke(allowed: str = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))):
    '''
    This function waits for a key hit (lower case alpha) or time out
    :param allowed: is a string of the allowed alpha characters
    see https://www.geeksforgeeks.org/python/alphabet-range-in-python/ w respect to 'a-z'
    :return: the key stroke if allowed, other wise "None" if fail safe times out
    In the code, fail_safe_0 is the slow counter and fail_safe_0 is the faster down counter
    Due to hardware? issue, keyboard.read_event has to be invoked twice (key bounce problem?)
    '''

    wait_01 = True
    fail_safe_0 = 1000; fail_safe_1 = 1000
    while wait_01 == True and fail_safe_0 >=1:
        keyrd = keyboard.read_event(suppress = True)
        keyrd = keyboard.read_event(suppress=True)
        key_read = keyrd.name.lower()
        fail_safe_1 -= 1
        if fail_safe_1 == 0:
            fail_safe_1 = 1000
            fail_safe_0 -= 1
        if key_read in allowed:
            wait_01 = False
            break
        else:
            if fail_safe_0 == 0:
                key_read = 'None'
            continue
    return key_read