import pyperclip        #<-- this imported module enables copy/paste to clipboard
import os               #<-- this module will allow us to manipulate the targeted file (fyl)
print(f'Modified TODAY= 4/19/2025  4:04 pm  (This a cleaned up copy of main-2.py. Goal is to read Abbv file & find match)')
print(fr'Path = C:\Users\gideon\PycharmProjects\PythonProject\GG_Project-2_Strings_and-Files\.venv\main-3.py')

# target_path = r'C\u\pathway'
target_fi = "zForm_Abbv.GG-1011.txt"  #<-- this string variable names the file in our virt environment

#### MODERN context management way of inputting a file (with "with" method a 'close' is not required)
def IsFiValid(filepath, maxSize, minSize):   #<-- this tests if target_fi exists and not too large
    if (os.path.exists(filepath) == False):     #<-- Using a method of the imported OS object
        return False
    file_size = os.stat(filepath).st_size/1000  #<-- using another method and return as Bytes/1000
    return (file_size < maxSize and file_size > minSize)
    # IsFiValid.help = "returns a True only if Fi(le) exists and is not too large or too small"

if IsFiValid(target_fi, 2000, 5) != True:
    print("The targeted file is not here or wrong size")
else:
    size = str(os.stat(target_fi).st_size/1000)
    print("The targeted file exists and it is greater than 5,000 bytes but less than 2MB")
    print ("The file size is", size, "Bytes/1000" )

    halt= input("Stopping here just to view statistics results of file test")

####  Iterating through the target file (a long text string)
## with open("zForm_Abbv.GG-1011.txt", "r") as target_file:  # cause the object, target_file to be opened
    ##     print('*' *8, target_file.name, '*' *8, '\n \n')
    ## print('vvvvvv  Below we read a first 100 line chunk of target_file  vvvvv \n')
    ## line_number: int = 0; chunk_max: int = 100
    ## for line in target_file:
    ##     line_number +=1     #inc the current line number
    ##     if line_number >= chunk_max:
    ##         break
##     print(line, end='')             # <-- this reads the 100 line chunk of the target_file
#
# ^^^ note:  target_file becomes 'closed' once we leave the indents under the 'with' statement


# with open("zForm_Abbv.GG-1011.txt", "r") as target_file:    # cause the object, target_file to open
    #     f_sample = target_file.read(199)
    # print('\n \n', f_sample, '  <-end of first sample', '%' * 20)
    # f_sample = target_file.read(300)        # <-- sampler picks up where it left off
    # print('\n \n', f_sample,'   <-end of second sample', '%' * 20)

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
    f_sample = target_file.read(2000)
    print('\n \n', f_sample, '  <-end of first sample of 2000 chars (index= 0:999)', '%' * 20)
    print(len(f_sample), "= Length of the f_sample string")

## i=0
## while i> -len(f_sample):
##     i -= 1
##     if f_sample[i] == "~" and f_sample[i-1] == "~":
##         print('double tilda found at i=', i, 'and i-1 =', i-1)
##         print(f_sample[i-30:i+1])
##         break
##     else:
##         print('double tilda was NOT yet found with i=', i)
## print ('end of while loop was hit (pgm-line 121)')

fetched_sub_sample = f_sample

trim_index = int(fetched_sub_sample.rindex('~~'))  #<-- convert type to integer

if fetched_sub_sample.rfind('~~'):
    print('The fetched sub sample includes a double tilda')
    #trim_index = int(fetched_sub_sample.rindex('~~'))  #<-- convert type to integer
    print(f'The index position of the last double tilda is {trim_index}')
else:
    print('The fetched sub sample DOES NOT include a double tilda')

print(f'Here are the last 100 chars of the trimmed subsample\n  {fetched_sub_sample[ trim_index-100: trim_index+2] }')

# STRING methods can be found here: https://www.w3schools.com/python/ref_string_rindex.asp
# program will take in subsequent characters one at a time unitl ~~ is hit
# program will remove the ending ~~ and then push the remainder to the clipboard
# calling VBA will read clipboard and paste pushed content if success

