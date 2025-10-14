print(f'Date: 10/12_B2/2025  \t\t updated Learn 47 String methods with new ideas to present See ##NEW !!!')
print(f'Copied from Idently 47 List methods 4/16/2025 and modified  https://www.youtube.com/watch?v=bnSYeYFRCaA&t=108s')
print(fr'Path = C:\Users\gideon\PycharmProjects\PythonProject\GG_Project-2_Strings_and-Files\.venv')

#Below copied from Scratch_01 on 10/12/2025: (and Package_03 copied into this venv)
import inspect
import sys
import os
import keyboard             #--- enable single key press inputs
import pyautogui as gu      #--- enable cursor control
import webbrowser           #--- enable opening up desired URL's for learning frames
import pyperclip            #--- enable use of clipboard
#import random
from random import choice   #--- enable random choice() method
from random import shuffle   #--- enable random shuffle() method

from Package_03 import vars_01 as v  #-- google "python syntax of an import from statement"
from Package_03 import mssgs_01 as msg
from Package_03 import funcs_01 as fn







##New : create an enumerated dictionary based on below, each string lesson becomes a callable function: def study_str_method(n)

# run below ## statements and then blocked them from 2nd time run
def enum_string_methods_dict():
    i: int = 1
    str_meths_dict = {}                     #<-- start with an empty dictionary
    for found_method in dir(str):
        if '__' not in found_method:        #<-- leave out the Dunder methods
            key = 'str_meth#_' + str(i)
            str_meths_dict[key] = found_method   # goggle "python add kv pair to dict"
            i += 1
            print('#', key, found_method, sep= ': ')  #<-- a colon plus space is inserted as separator for each item
    return str_meths_dict

fn.skip(5)
show_dict= enum_string_methods_dict()
fn.skip(2)
print(f'Here are the 47 methods in a first dictionary:\n{show_dict}')
breakpoint()

## get_string_methods_list()
fn.skip(5)

sample_1 = 'the quick Brown fox Beat the slow turtle.'
sample_2 = 'Every Good Boy Deserves Favor'


## create_example('capitalize', 'sample_1')
n=0
#: 1: capitalize  --> upper cases 1st letter of the string, lower case rest
n+=1;
sMethod = 'capitalize'
sMethod_ = sMethod + '()'

print(f'({n})\t\tBelow example shows the {v.yy_}{sMethod_} method{v.z_} applied to "the quick Brown fox Beat the slow turtle."')
print(f'\t\t{v.g_}{sample_1.capitalize()}{v.z_}')   # outputs: The quick brown fox beat the slow turtle.
print(f'Only the first letter has been capitalized. "Beat" has been lowered')
print(f'What are some practical uses for the {sMethod_} function of python?')

q_Google_1 = f'What are some practical uses for the {sMethod_} function of Python?'
# q_Google_2 = f'Using the pyperclip module of Python'
# q_Google_3 = f'Using the {sMethod} method of Python'

q_W3School_1 = f'https://www.w3schools.com/python/ref_string_{sMethod}.asp'

url_tail1 = f'/search?q={q_Google_1}'
url_full = f'https://www.google.com' + url_tail1
webbrowser.open(url_full)
webbrowser.open(q_W3School_1)

print(f'\nLOOK inside the browser for {v.yy_}Two new TABS (Google result + W3 School result) for {sMethod_}', '-='*20, f'>{v.z_}')

#: https://www.google.com/search?q=%22Stack+Exchange%22+OR+StackOverflow
# https://webapps.stackexchange.com/questions/39818/how-should-i-write-the-url-for-a-specific-google-search-queryhttps://webapps.stackexchange.com/questions/39818/how-should-i-write-the-url-for-a-specific-google-search-query

# https://www.w3schools.com/python/ref_string_capitalize.asp
#pyperclip.copy("This text will be copied to your clipboard.")
#pyperclip.copy(q_Google_1)
fn.skip(1)

#: 2: casefold      --> lower cases the string so it can be compared with other case folded string
n+=1;
sMethod = 'casefold'
sMethod_ = sMethod + '()'

print(f'({n})\t\tBelow example shows the {v.yy_}{sMethod_} method{v.z_} applied to "the quick Brown fox Beat the slow turtle."')
print(f'\t\t{v.g_}{sample_1.casefold()}{v.z_}')   # outputs: The quick brown fox beat the slow turtle.
print(f'All letters have been normalized to lower case')
print(f'What are some practical uses for the {sMethod_} function of Python?')

q_Google_1 = f'What are some practical uses for the {sMethod_} function of python?'
# q_Google_2 = f'Using the pyperclip module of Python'
# q_Google_3 = f'Using the {sMethod} method of Python'

q_W3School_1 = f'https://www.w3schools.com/python/ref_string_{sMethod}.asp'

url_tail1 = f'/search?q={q_Google_1}'
url_full = f'https://www.google.com' + url_tail1
webbrowser.open(url_full)
webbrowser.open(q_W3School_1)

print(f'\nLOOK inside the browser for {v.yy_}Two new TABS (Google result + W3 School result) for {sMethod_}', '-='*20, f'>{v.z_}')

fn.skip(5)

breakpoint()
#: 3: center        --> pads with n fill chars and centers sample_1 in whole
n+=1; print(n, ':', sample_1.center(60, '#')) # outputs: #########the quick Brown fox beat the slow turtle.##########

#: 4: count       --> counts the number of occurrences of arg in the sample_1
n+=1; print(n, ':', sample_1.count('t'))  # outputs: 5 (There are 5 T's in 'the quick Brown fox Beat the slow turtle.'

#: 5: encode       --> converts sample_1 into specified alternate coding, for example UTF-8
n+=1

#: 6: endswith      -->returns Boolean to test of whether sample_1 ends with any letters in tuple
n+=1; print(n, ':', sample_1.endswith(('.', '?', '!')))  #note 3 )'s at end outputs True because ends with period

#: 7: expandtabs    --> locates tabs (\t) inside sample_3 and makes them bigger
sample_3= 'hello\tthere\tmy\tpretty'
n+=1; print(n, ':', sample_3.expandtabs(10))  #outputs: hello     there     my        pretty

#: 8: find      --> locates arg substring in sample_1 and gives its starting index
n+=1; found = sample_3.find('\t')
print(n, ':', sample_3.find('\t'))  #outputs: 5 (1st place is index=0)
print(sample_3[found:])             #<-- using slice method tp print from found position to end
                                    # reminder: 'https://www.youtube.com/watch?v=bnSYeYFRCaA&t=108s'
#: 9: format    -->   inserts substitute substrings into main string
n+=1; sample_4 = 'The {subject} is {action}ing {adverb} {object}'
print(n, ':', sample_4.format(subject= 'elephant', action= 'work', adverb= 'very', object= 'hard' ))
sample_5 = 'The {} is {}ing {} {}'
print(n, ':', sample_5.format('elephant', 'work', 'very', 'hard' ))     #<-- same result using blank curly pairs
                        # both prints output: The elephant is working very hard
#: 10: format_map   --> uses a specified dictionary object and replaces in-string keys with their dictionary values
n+=1; map: dict = {'subject' : 'Elephant', 'action' : 'Work',  'adverb' : 'Very',  'object' : 'Well'}
print(n, ':', sample_4.format_map(map))   #<-- Note that map is a dictionary and keys are strings, as are their values

#: 11: index ---> similar to find except that it returns an error if substring not found as opposed to returning a -1 (False)
n+=1; found = sample_3.find('\t')
print(n, ':', sample_3.index('\t'))  #outputs: 5 as position of escape-Tab (1st place is index=0)
# print(n, ':', sample_3.index('\n'))  #outputs an error message in output window

#: 12: isalnum      --> Is the sample string purely Alpha-Numeric ? (Only A-Z, a-z, 0-9)
sample_6 = 'abcdefg123'
sample_7 = 'abcdefgH'
n+=1; print(n, ':', sample_5.isalnum())
print(n, ':', sample_6.isalnum())

#: 13: isalpha      --> Is the sample string purely Alpha (not even numbers allowed)
n+=1; print(n, ':', sample_6.isalpha())
print(n, ':', sample_7.isalpha())

#: 14: isascii      --> Is the sample string purely ASCII coded?
n+=1; print(n, ':', sample_6.isascii())

#: 15: isdecimal    --> Is the sample string purely 0-9?

#: 16: isdigit    --> Is the sample string purely numbers but in any form including funny fonts

#: 17: isidentifier    --> Can the sample string operate as valid Python variable name?

#: 18: islower      --> Is the sample string purely lower case a-z?
#: 19: isnumeric    ---> stick with is decimal

#: 20: isprintable  --> Is the sample string usable in a one-line print() statement?
#: 21: isspace      --> Only spaces
#: 22: istitle      --> 1st leter of each word is capital
#: 23: isupper

#: 24: join      -->  join the string arguments
joiner: str = '---'   #this will be inserted between the to-be-joined args
n+=10; print(n, ':', joiner.join([sample_1, sample_2, sample_3]))

#: 25: ljust    ---> pads to the right with filler
n+=1; print(n, ':', sample_6.ljust(30, '*'))  #outputs: abcdefg123********************

#: 26: lower    ---> converts all to LOWER case, no arg

#: 27: lstrip   --->  strip argument off of left side of sample
n+=2; print(n, ':', sample_6.lstrip('abc')) #outputs: defg123

#: 28: maketrans --> converts text into a translation table for use with translate() function
table = sample_3.maketrans('ht', '-=') #--> plan to replace EACH h and t with RESPECTIVE chars of 2nd arg of SAME length
n+=1; print(n, ':', table)               #---> creates an ascii coded translation dictionary -can use emoji's
print(sample_3.translate(table))        #---> Translate according to pre-made Table

#: 29: partition  #--> specify a partitioning substring that breaks sample into 3 LIST items with partitioner in middle
n+=1; print(n, ':', sample_6.partition('fg'))   #outputs: ('abcde', 'fg', '123')

#: 30: removeprefix #--> remove specified opening substring
n+=1; print(n, ':', sample_5.removeprefix('Th'))

#: 31: removesuffix     #---> same as prefix but from other end of sample
n+=1; print(n, ':', sample_5.removesuffix('{}'))

#: 32: replace  #--> remplace specified substring (1st arg) with 2nd arg, optional 3rd arg is number of times to do
n+=1; print(n, ':', sample_5.replace('{}', 'BRACKS'))

#: 33: rfind  #--> Starting from the RIGHT, find position in sample of arg text, position is counted from left !!!
n+=1; print(n, ':', sample_1.rfind('slow')) #outputs: 29 which is index of 's'  (rindex does same but returns error)

#: 34: rindex
n+=1; print(n, ':', sample_1.rindex('slow'))    #--> Breaks as an error if not found

#: 35: rjust    #--> Justifies to the RIGHT
n+=1; print(n, ':', sample_1.rjust(60, '_'))

#: 36: rpartition    #--> same as 3-part partition but looks for middle part from the RIGHT side of sample

#: 37: rsplit    #--> starting from RIGHT, split into LIST of substrings using the provided splitter upto max times
n+=2; print(n, ':', sample_1.rsplit(' ', maxsplit=4)) #outputs: ['the quick Brown fox', 'Beat', 'the', 'slow', 'turtle.']

#: 38: rstrip   #--> starting from RIGHT, remove just the first instance of the specified substring
n+=1; print(n, ':', sample_1.rstrip('turtle.')) #<--- requires the whole ending substring?

#: 39: split  #--> starting from LEFT, split into LIST of substrings using the provided splitter upto max times
n+=1; print(n, ':', sample_1.split(' ', maxsplit=3))

#: 40: splitlines  #--> searches for \n and uses it as terminator for creating a list
sample_8 = 'Please be sure to like\nand SUBSCRIBE\nAs well as wathcing\n'
n+=1; print(n, ':', sample_8.splitlines(keepends= False)) #<-- if True, the \n terminators are included in LIST

#: 41: startswith  #--> Boolean result= True/False if sample starts with specified substring
n+=1; print(n, ':', sample_8.startswith('Please'))
print(n, ':', sample_8.startswith('please'))        #<-- and is case sensitive

#: 42: strip    #--> remove the specified substring
n+=1; print(n, ':', sample_8.strip('watching'))       #<-- can be in mid of sample string? NOT WORKING HERE !!!!

#: 43: swapcase    #--> Changes UPPERS to lowers and vise versa

#: 44: title    #--> forces 1st alpha letter of each word to be capped
n+=2; print(n, ':', sample_4.title())

#: 45: translate    #--> See maketable above

#: 46: upper
#: 47: zfill    #--> Zero fill: prefixes the sample with n 0's (for what use, don't know)

# Process finished with exit code 0

##########  EXTRA SECTION: USEFUL f-string METHODS #####
# from https://www.youtube.com/watch?v=EoNOWVYKyo0

#: 50: Inserting commas or underscores into large numbers
biggie: int = 1000000000    #<-- lots of zeroes
n=50; print(n, ':', f'{biggie:,}')  #inserts commas for every 3 zeroes
print(n, ':', f'{biggie:_}')        #inserts underscores for every 3 zeroes, NO OTHER CHARs allowed

#: 51: Use f-string to right-align strings
short = 'Hi You'; short_2 = "Yes it's You"
n+=1; print(n, ':', f'{short:>20}')     #<--- Total string length is 20 chars
print(n, ':', f'{short_2:>20}')
print(n, ':', f'{short_2:<19}', '|')     #<--- left-aligned plus '|" as end indicator
print(n, ':', f'{short_2:^19}', '|')     #<--- CENTER-aligned plus '|" as end indicator
print(n, ':', f'{short_2:_^19}', '|')    #<--- filler char inserted after colon :

#: 52:  Date/time tricks (to be continued)

# (new) Indently ALL f-string tricks from https://www.youtube.com/watch?v=9saytqA0J9A

#60 The basic f-string usage = avoid plus signs and open/close quotes
n=60; print('\n\n\nBasic combining of strings calls for "str1" + "str2"')
my_name: str = 'Gideon'; my_age: int = 73 #<-- next want to combine string plus integer
print('NAME =' + 'Gideon ' + 'AGE = ' + str(my_age))
print(n, ':', 'Above was printed as concatenation of only strings')
print(f'NAME =  {my_name}   AGE = {my_age}')
print(n, ':', 'Above was printed as an f-string using { } for evaluating different types of objects')
n+=1; print('\n', n, ':', f" 5 + 6 = {5+6},  5*6 = {5*6}, 5^3 = {5**3}")
print('Above was printed with  an f-string using { } for evaluating different math expressions')

#: 62 : Auto complete of literal plus value for DEBUGGING runs
debug_var = 125
n+=1; print('\n', n, ':', f"{debug_var = }")
print('Above was printed with  an f-string using {var=} for auto insertion of var name')

#: 63 :  Auto complete even works for Boolean function tests !!!
n+=1; print('\n', n, ':', f"{isinstance(debug_var, int) = }")
print('Above was printed with an f-string using { } for evaluating a Boolean inquiry and auto competing the result')

#: 64 :  Rounding high precision floats and converting value to percentage
multi_digit: float = 8765.4167;  compare_percent: float = 0.5678
n+=1; print('\n', n, ':', f"{multi_digit:.2f}", f"{compare_percent:.2%}")
print('Above was printed with an f-string using { } for rounding to 2 decimal places (2f) and shifting dec point 2 places')
biggie2: float = 1_234_567.8901    #<-- lots of digits (see biggie int above as reminder)
print('\n', n, ':', f"{biggie2:,.1f}")      #<-- don't forget period b4 1f !!
print(' ^^^^ Above uses f-string { } for rounding to 1 decimal place AND insering commas every 3 zeroes')

#: 65 :  Dealing with DATE-TIME issues
from datetime import datetime       #<-- this is a class (a type) that has its own methods
time_now: datetime = datetime.now()  #<-- declares var time_now as being of type, datetime
n+=1; print('\n', n, ':', f"{time_now:%X}")
print(' ^^^^ Above uses f-string { } for limit to just the short form date  (% X )') #<-- can be lower case X too
print('\n', n, ':', f"{time_now:%C}")
print(' ^^^^ Above uses f-string { } for long form date + military time  (% C )')
print('\n', n, ':', f"{time_now:%H:%M:%S}")
print(' ^^^^ Above uses f-string { } for long form time  (% H : M : S )') #<-- note colon (:) separators
print('\n', n, ':', f"{time_now:%H:%M}")
print('\n', n, ':', f"{time_now:%H military :%M time H:M}")
print('\n', '\033[96mThis should be colored blue due to the 033 escape sequence')
print('\033[91m This should be colored red  due to the 033 escape sequence')
print('\033[92m Check out Python Tutorial: Escape Sequence Explained at https://www.youtube.com/watch?v=hExrjJ_KR48')
print('\033[93m Check out Caleb Curry\'s Python Tutorial: at ..')
print('\t https://www.youtube.com/watch?v=9miLWHISMqc&list=PL_c9BZzLwBRKK8ndQBBKolg7IxrC5T6Ws&index=20')

#: 66 :  FRench Raw data specifier for f-strings (at 9:40 / 1942 in Indently video)
print('\n \033[95m This should be colored what? due to the 033 escape sequence')
print('\033[97m This should be colored what? due to the 033 [97m escape sequence, Answer: back to WHITE !!')

raw_text: str = r'Back slashes are \n treated as \b literals \t when the r-string attribute is used'
n+=1; print('\n', n, ':', raw_text)
print('\t On other hand, \t tabs and backups \bare not ignored \" if not \"raw\" ')

sample_11: str = 'My_Name'
sample_path: str = fr'\User\{sample_11}\Documents\PythonTutorials'  #<-- note fr-string !!!!!!!!! the 'f' allows {samp}
print('\nThe path to target folder is:', sample_path) #<-- the French string (fr) sample_path includes raw back slashes

#: 67:  Nested f-strings
n+=1; print('\n', n, ':', f'{5+5=}    {10 + 10=}    {10*10=}      {10**10=:,}') #<-- note also use of biggie colon-comma
print(f'{5+5=}    {10 + 10=} {r'User\Folder\Docs'}  <-- this is a nested r-string')

#: 68:  CUSTOM F-STRINGS !!!!!!!!!!
class Special_text:
    def __init__(self, text : str) -> None:
        self.text = text

    def __format__(self, format_spec: str) -> str:
        match format_spec:      #<--- test for cases of where format_spec is one thing or another
            case 'up':
                return self.text.upper()
            case 'low':
                return self.text.lower()
            case 'len':
                return str(len(self.text))      #<-- this will return the length count as a string
            case _:             #<-- all other cases default to next
                raise ValueError(f'Supplied format specifier {format_spec} is not valid')

my_sample_text_1: Special_text = Special_text('this started off as all lower case but of type: special_text')
my_sample_text_2: Special_text = Special_text('THIS STARTED OFF AS ALL UPPER CASE BUT OF TYPE: SPECIAL_TEXT')
n+=1; print('\n', n, ':', f'{my_sample_text_1:up}')
print('\t', f'{my_sample_text_2:low}')
print('\t', f'{my_sample_text_2:len} <--this is the length count')