# this is my try at porting crach.sh to python
 #imports
import os
import time
import sqlite3
#variables
what_mode = 99 #99 is the main menue
main_path = os.getcwd()
file_name_list = {0: None}
#hashcat related
hashcat_file = None
wordlist = None
session_name = None
double_check = None
#word menue:
wordlist_menue_mode = None
crunch_options = None
merge_dir = None
merged_file_name = None
#session menue
session_name_recoverie = "None"
#capture menue
capture_mode = None
#functions

def sql(command):
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute(command)
    conn.commit()
    return c.fetchall()
    c.close()
def merge_text_files(directory_path, output_file):
    """
    Merges the contents of all text files in the specified directory into a single output file.

    Args:
        directory_path (str): Path to the directory containing text files.
        output_file (str): Path to the output file where the merged content will be saved.
    """
    try:
        with open(output_file, 'w') as output:
            for filename in os.listdir(directory_path):
                if filename.endswith('.txt'):
                    file_path = os.path.join(directory_path, filename)
                    with open(file_path, 'r') as input_file:
                        output.write(input_file.read())
                        output.write('\n')  # Add a newline after each file's content
        print(f"Successfully merged text files into {output_file}")
    except Exception as e:
        print(f"Error merging text files: {e}")
def filter_lines_by_length(input_file, output_file, target_length):
    """
    Reads lines from the input file, filters out lines with the specified length or longer,
    and writes the filtered lines to the output file.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output file where filtered lines will be saved.
        target_length (int): Desired minimum line length for filtering.
    """
    try:
        with open(input_file, 'r') as input_text:
            lines = input_text.readlines()
            filtered_lines = [line.strip() for line in lines if len(line.strip()) >= target_length]

        with open(output_file, 'w') as output_text:
            for line in filtered_lines:
                output_text.write(line + '\n')

        print(f"Filtered lines with length {target_length} or longer saved to {output_file}")
    except Exception as e:
        print(f"Error filtering lines: {e}")
def check_where_i_am():
    global what_mode
    if what_mode == 99:
        main_menue()
        check_where_i_am()
    if what_mode == 0:
        crack_in_hashcat()
        check_where_i_am()
    if what_mode == 1:
        wordlist_menue()
        check_where_i_am()
    if what_mode == 2:
        session_menue()
        check_where_i_am()
    if what_mode == 3:
        capture_mode()
        check_where_i_am()
    if what_mode == 4:
        dependencie_mode()
        check_where_i_am()
    if what_mode == 5:
        close()
    if what_mode == 6:
        os.system("rm settings.db")
        exit()

        check_where_i_am()
    #0 to crack a file in hashcat
def crack_in_hashcat():
    global main_path, hashcat_folder
    global hashcat_file
    os.system('clear')
#get the cracking file
    print("select the file to crack")
    counter = 1
    for x in os.listdir(hashcat_folder):
        print(counter, ":", x, end=' ')
        file_name_list[counter] = x
        counter = counter + 1
    print()
    print("enter the Number corosponding to the file you want to crack")
    hashcat_file = file_name_list[int(input())]
    file_name_list.clear() #clear the to get the wordlist
#get the wordlist
    print("Select the Wordlist")
    counter = 1
    for x in os.listdir(wordlist_folder):
        print(counter, ":", x, end=" ")
        file_name_list[counter] = x
        counter = counter + 1
    print()
    print("enter the Number corosponding to the Wordlist you want to use")
    wordlist = file_name_list[int(input())]
    #ask for session name
    print("What should the session be called?")
    session_name = input("Enter the session name: ")
    #double check
    print("Please make shure that all information is correct")
    print("Hashcat file:" + hashcat_file)
    print("Wordlist:" + wordlist)
    print("Session Name:" + session_name)
    double_check = input("Enter yes to continue enter no to re enter all information: ")
    if double_check == "yes":
        os.system("hashcat -m 22000 -a 0 --session " + session_name + " " + "hashcat_files/" + hashcat_file + " " + "wordlists/" + wordlist)
    else:
        crack_in_hashcat()
    #main
def wordlist_menue():
    os.system("clear")
    global what_mode
    global wordlist_menue_mode
    global crunch_options
    global merge_dir, merged_file_name
    wordlist_menue_mode = None
    print("What do you want to do?")
    print("Enter 1 to start mentalist")
    print("Enter 2 to start Crunch")
    print("Enter 3 to merge all txts in a dir to one")
    wordlist_menue_mode = input("Enter 1 or 2: ")
    #print(wordlist_menue_mode)
    if wordlist_menue_mode == "1":
        os.system("./Mentalist")
    if wordlist_menue_mode == "2":
        print("please enter all options for crunch(use -o filename to save to file)")
        print("IMPORTANT!!! this is a unfinished feature it works but i will add my own proper crunch engine")
        crunch_options  = input("Enter all crunch options:")
        os.system("crunch " + crunch_options)
    if wordlist_menue_mode == "3":
        merge_dir = input("In what dir are the files located?")
        merged_file_name = input("What is the name off the new file")
        merge_text_files(merge_dir, merged_file_name)
    what_mode = 99
def session_menue():
    global what_mode
    session_name_recoverie = input("Please enter the name of the session: ")
    os.system("hashcat --restore --session " + session_name_recoverie)
    time.sleep(5)
    what_mode = 99
def capture_mode():
    print("Enter 1 to open airgeddon")
    print ("Enter 2 to open wireshark")
    capture_mode = input("Enter 1 or 2: ")
    if int(capture_mode) == 1:
        os.system("sudo bash ./" + airgeddon_folder + "/airgeddon.sh")
    elif int(capture_mode) == 2:
        os.system("sudo wireshark")
def dependencie_mode():
    print("work under construction")
def close():
    exit()

def main_menue():
    os.system('clear')
    print()
    print("What do you want to do?")
    print()
    print("Enter 0 to crack a file in hashcat")
    print("Enter 1 to get to the wordlist menue")
    print("Enter 2 to restore a session")
    print("enter 3 to enter the capture mode")
    print("enter 4 to open the dependencie installer")
    print("enter 5 to exit")
    print("enter 6 delete the settings")
    print()
    global what_mode # defines that it shoud use the normal what_mode instead of a function specific one
    what_mode = int(input())
    check_where_i_am()
sql("CREATE TABLE IF NOT EXISTS settings (first_start INTEGER, hashcat_folder TEXT, wordlist_folder TEXT, airgeddon_folder TEXT)")
sql("INSERT INTO settings (first_start) VALUES (0)")
test = sql("SELECT First_start FROM settings")

if str(test)[2:3] == "0" or None:
    print("first start, setting up")
    wordlist_folder_temp = input("Enter the location of the wordlists folder: ")
    hashcat_folder_temp = input("Enter the location of the folder where you want to save the hashcat ready files: ")
    airgeddon_folder_temp = input("Enter the location of the airgeddon folder: ")
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute("UPDATE settings SET hashcat_folder = ?", (hashcat_folder_temp,))
    c.execute("UPDATE settings SET wordlist_folder = ?", (wordlist_folder_temp,))
    c.execute("UPDATE settings SET airgeddon_folder = ?", (airgeddon_folder_temp,))
    conn.commit()
    c.close()
    sql("UPDATE settings SET first_start = 1 WHERE first_start = 0")
    wordlist_folder = sql("SELECT wordlist_folder FROM settings")[0][0]
    hashcat_folder = sql("SELECT hashcat_folder FROM settings")[0][0]
    airgeddon_folder = sql("SELECT airgeddon_folder FROM settings")[0][0]
else:
    wordlist_folder = sql("SELECT wordlist_folder FROM settings")[0][0]
    hashcat_folder = sql("SELECT hashcat_folder FROM settings")[0][0]
    airgeddon_folder = sql("SELECT airgeddon_folder FROM settings")[0][0]
check_where_i_am()

 