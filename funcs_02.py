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

def get_keystroke():
    key_read = ''
    keyrd = keyboard.read_event(suppress = True)
    keyrd = keyboard.read_event(suppress=True)
    key_read = key_read.join(keyrd.name.lower())
    return key_read

def get_allowed_keystroke(allowed: str = ''.join(chr(i) for i in range(ord('A'), ord('z') + 1))):
    '''
    This function waits for a key hit (e.g. A-Z and a-z)
    :param allowed: is a string of the allowed alpha characters
    see https://www.geeksforgeeks.org/python/alphabet-range-in-python/ w respect to 'a-z'
    :return: the key stroke if allowed, other wise type Try Again
    '''

    valid_hit = False
    while valid_hit == False:
        keyrd = keyboard.read_event(suppress = True)
        keyrd = keyboard.read_event(suppress=True)
        key_read = keyrd.name
        if key_read in allowed:
            valid_hit = True
            break
        else:
            valid_hit = False
            print(f'{v.r_}The typed key, {v.yy_}{key_read}{v.r_} is not valid. Try again{v.z_}')
    return key_read


def enum_var_methods_dict(var= str):
    ''' The built-in dir(object) function generates a list of methods recognized by the specified object.
    The present enumerating function (above, named "enum_var_methods_dict" associates a method number (1-47 for string methods)
        with each found method and appends them into a dictionary ("var_meths_dict"), the number being the key of
        the KV pair and the method name being the 'value'. It also generates a reverse dictionary and RETURNS both dicts in a tuple.
        Additionally, it prints the KV pairs as a tabular list, where "n_cols" is the number of columns, "w_pCol" is the width of
        each column and "var" is the ID of the object. We use modulo math (%) to determine when to include a CRLF. '''

    stepper: int = 1;   #-- steps through the columns of each row by incrementing +1
    n_cols =3           #-- number of printed out columns
    w_pCol = 70         #-- width per column
    var_meths_dict = {}    #<-- start with an empty dictionary and add each found to it
    reverse_var_dict = {}
    print(f'\t\tBelow is a listing of methods for the data type: {var}\n')

    for found_method in dir(var):
        if '__' not in found_method:        #<-- leave out the Dunder methods
            key = 'var_meth_#' + str(stepper)
            var_meths_dict[key] = found_method   # goggle "python add kv pair to dict"
            reverse_var_dict[found_method] = key
            outp_str = f'>> {key} : {v.yy_}{found_method}{v.z_}'
            if stepper % n_cols != 0:
                print(f'{outp_str:<{w_pCol}}', end="")  #<-- a colon plus space is inserted as separator for each item
            else:
                print(f'{outp_str}')

            stepper += 1
    return var_meths_dict, reverse_var_dict

n=1 #-- this declaration needed for below --vvv-- function
def study(*samps, subject = 'String Methods', sMethod = 'capitalize', meth_ID= n):
    sMethod_ = sMethod + '()'

    print(f'\t\t\t\t\t\tFIRST, we are studying {v.yy_}{subject.upper()}{v.z_}\n\n')
    print(f'({n})\t\tBelow example shows the {v.yy_}{sMethod_} method{v.z_} applied to a set of input string samples\n\n')
    for samp in samps:
        print(f'The input string sample is this:\n\t\t{v.yy_}{samp}{v.z_}')
        samp_dot_attr = getattr(samp, sMethod, None)
        #Note the addition of parens to samp_dot_attr in the line below !!!!
        print(f'The resulting output of applying the {sMethod_} method is this:\n\t\t{v.g_}{samp_dot_attr()}{v.z_}')
    print(f'Note that only the first letter has been capitalized irrespective of punctuation\n')
    print(f'What are some practical uses for the {sMethod_} function of python?\n')

    q_Google_1 = f'What are some practical uses for the {sMethod_} function of Python?'
    # q_Google_2 = f'Using the pyperclip module of Python'
    # q_Google_3 = f'Using the {sMethod} method of Python'

    q_W3School_1 = f'https://www.w3schools.com/python/ref_string_{sMethod}.asp'

    url_tail1 = f'/search?q={q_Google_1}'
    url_full = f'https://www.google.com' + url_tail1
    print(f'\n\nEnter a valid 1-Hit key stroke')
    test_01 = get_allowed_keystroke()
    print(f'This is a test of the keystroke function in f2. Hit key name = {test_01}')
    reponse1 = input(f'Would you like to dig deeper via Google? (y/n)\n')

    if reponse1 == 'y':
        print(f'{v.M_}Get a Notebook and take Handwritten Notes !!!{v.z_}')
        webbrowser.open(url_full)
        print(f'LOOK inside the browser for {v.yy_}New TAB (Google result) for {sMethod_}', '-=' * 20, f'>{v.z_}')
    fn.skip()
    reponse2 = input(f'Would you like to dig deeper via W3 Schools? (y/n)\n')
    if reponse2 == 'y':
        print(f'{v.r_}Get a Notebook and take Handwritten Notes !!!{v.z_}')
        webbrowser.open(q_W3School_1)
        print(f'LOOK inside the browser for {v.yy_}New TAB (W3 Schools result) for {sMethod_}', '-=' * 20, f'>{v.z_}')
    fn.skip()
    return None
