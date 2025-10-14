import pyperclip        #<-- this imported module enables copy/paste to clipboard

import os               #<-- this module will allow us to manipulate the targeted file (fyl)

#-- Many of the notes in here are for purpose of learning PYTHON
#-- Comments start with a hash sign     ## TODAY= 4/15/2025  9:30 pm

# GOAL here = learn STRing handling and FILE handling

##### OLD risky way
#  target_file = open("zForm_Abbv.GG-1011.txt", "r")   #which is in .venv folder
#  print(target_file.name)     # name of the file is an attribute of the object
#  target_file.close()        # !!! This is CRITICAL when using the open() function
#
## print(target_file.mode)     # r= read only  w= write only r+ = read and write

target_fi = "zForm_Abbv.GG-1011.txt"  #<-- this string variable names the file in our virt environment

#### MODERN context management way below (with "with" a 'close' is not required)

def IsFiValid(filepath, maxSize, minSize):   #<-- this function will test if target_fi exists and not too large
    if (os.path.exists(filepath) == False):     #<-- Using a method of the imported OS object
        return False
    file_size = os.stat(filepath).st_size/1024  #<-- using another method and return as KBytes
    return (file_size < maxSize and file_size > minSize)
    # IsFiValid.help = "returns a True only if Fi(le) exists and is not too large or too small"

if IsFiValid(target_fi, 200, 5) != True:
    print("The targeted file is not here or wrong size")
else:
    size = str(os.stat(target_fi).st_size/1024)
    print("The targeted file exists and it is greater than 5 KB but less than 200KB")
    print ("The file size is", size, "KiloBytes" )

    halt= input("stopping here to view results of file test")

with open(target_fi, "r") as target_file:
#    pass
     file_content = target_file.readline()
     print(file_content, end='')
     file_content = target_file.readline()
     print(file_content, end='')
     print('^^^^ Above got first two lines of the file, one at a time \n \n')

# ^^^^ in the above, the readline() method gets one line and points to next
# ^^^^^^ the end='' blocks print() from appending a new line char

####  Better way is to iterate through the target file (a long text string)
with open("zForm_Abbv.GG-1011.txt", "r") as target_file:    # cause the object, target_file to be
    print('*' *8, target_file.name, '*' *8, '\n \n')
    print('vvvvvv  Below is dump of the entire target_file  vvvvv \n')
    for line in target_file:
        print(line, end='')             # <-- this better than doing f= target_file.read()
#                                       # , where latter fills the variable f with all of target_file
# ^^^^^ above should print the whole file contents as line iterates through the file
# ^^^^^ AND YES, IT WORKS !!!!!
# ^^^   target_file becomes 'closed' once we leave the indents under the 'with' statement


with open("zForm_Abbv.GG-1011.txt", "r") as target_file:    # cause the object, target_file to open
    f_sample = target_file.read(199)
    print('\n \n', f_sample, '  <-end of first sample', '%' * 20)
    f_sample = target_file.read(300)        # <-- sampler picks up where it left off
    print('\n \n', f_sample,'   <-end of second sample', '%' * 20)


def pBlns(n):        #print n Blank lines
    print('\n'*n)
    self= pBlns                     # <-- This a 'local' varaible, not global !
    self.name = 'pBlns (lower) = print (n) Blank lines:  '
    self.help = self.name + ' This function prints n Blank Lines'


def pStars(n):       #rPint n Astriks
    print('*' * n, end='')
    self = pStars
    self.name = 'pStars (lower) = Print (n) Asterisks (*):  '
    self.help = self.name + ' This function prints n Stars'
pStars(10)
pBlns(3)
pStars(10)

print('\n', pBlns.help)
print('\n', pStars.help)
pBlns(3)

def pii(mssg1, mssg2):       # <--- function prints TWO prompt msssgs to user and gets user input !!!!
    print(mssg1)
    mssg2 = mssg2 + ' (pgm-line 69)\n'
    ui = input(mssg2)
    return ui       # <-- the function return string is the user reponse to the two mssg's

cond = True
if cond == True:
    m1= 'The condition is true'
    m2= 'Please give your opinion about it being True'
else:
    m1 = 'The condition is false'
    m2 = 'Please give your opinion about it being False'

ur = pii(m1, m2)
print('\n \n This is the user response to double messages', ur)

# import pyperclip          # <--- load the ClipBoard read/write module (from pip file)
x = input('copy something to the Clipboard  (pgm-line 84)')
fetch= pyperclip.paste()  # <--- pull from clipboard
print(fetch)
send_back = fetch #'this was sent back from python program'
# push = 'text to push to the clipboard'
pyperclip.copy(send_back)      # <--- pushes text to the clipboard
input('sent back should be in the clipboard (pgm-line 90)')
print('Look for tutorials about pip and pyperclip re interfacing with the clipboard')


# sample from zAbvv file = ~prr~ presented ation~~
# clipboard will contain "prr"
# program will convert it to "~" + {clip_in} + "~ " = search_4_string
fetch= pyperclip.paste()  # <--- pull from clipboard
fetch_mod= "~" + fetch + "~ "
print(fetch_mod)
input('above should show the modified clipboard fetch (pgm-line 100)')

# program will input part of zAbvv file and search for the search_4_string

with open("zForm_Abbv.GG-1011.txt", "r") as target_file:    # cause the object, target_file to open
    f_sample = target_file.read(1000)
    print('\n \n', f_sample, '  <-end of first sample of 1000 chars (index= 0:999)', '%' * 20)
    print(len(f_sample), "= Length of the f_sample string")

fetched_sub_sample = f_sample[-20:-1] + f_sample[-1]  # <-- note the first slice stops before index= -1
print(fetched_sub_sample, " <-- this was last 20 characters \n")

i=0
while i> -len(f_sample):
    i -= 1
    if f_sample[i] == "~" and f_sample[i-1] == "~":
        print('double tilda found at i=', i, 'and i-1 =', i-1)
        print(f_sample[i-30:i+1])
        break
    else:
        print('double tilda was NOT yet found with i=', i)
print ('end of while loop was hit (pgm-line 121)')


# program will take in subsequent characters one at a time unitl ~~ is hit
# program will remove the ending ~~ and then push the remainder to the clipboard
# calling VBA will read clipboard and paste pushed content if success

