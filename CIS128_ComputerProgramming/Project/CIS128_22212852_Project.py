'''
CIS-128 Project - Student Management System
Name: Cheung Siu Chun
SID: 22212852

version: 1.1
- Added support of student ID and contact number in add entry and update entry function
- Combined the if condition of update entry for mulitple found entry on single entry
- Added a warning if user update the student name, which already exists in other entries
'''
# Library Import
import re # FOR input validation
import os

'''
Unit Functions
'''

def fileOpener(fileName: str, openMode: str, allowCreate: bool):
    '''
    Purpose: 
        1. Check whether it exists at the working directory
        2. If the file does not exist depnding on {allowCreate}:
            if {allowCreate} == True, ask the user to see if they wants to create one
            if {allowCreate} == False, quit the system 
    Parameter: 
        1. fileName (String): the name of file to be opened
        2. openMode (String): same as the {mode} parameter of python open()
        3. allowCreate (Boolean): check to trigger file creation
    Return:
        1. fileOpened (class '_io.TextIOWrapper'): file object is returned if file found or created / None if file not found and not created
    '''

    # use os.path.exists function to check whether the file is under the same working directory of the python scipt
    # might expand to support ither directory if have time
    fileExist = os.path.exists(fileName)

    if not fileExist and allowCreate == True:
        # if file does not exist and allow to create, ask user whether to create a new text file
        create = input("Would you want to create a New File for storing student info?\nInput [Y] for yes / any other key for Quit: ")
        if create.upper() == "Y": # use upper to allow both lower case y and upper case Y
            # if yes, then create file
            fileOpened = open(fileName, "x", encoding="utf-8")
            if fileOpened:
                print(f"{os.getcwd()}\{fileName} is created.")
            return fileOpened
        else:
            # if user does not want to create at the directory
            print("Quit Student Mangement System. Have a good day!")
            exit()

    elif not fileExist and allowCreate == False:
        # if file does not exist and not allow to create, return None
        print(f"File does not exists under the folder {os.getcwd}")
        return None

    elif fileExist:
        # if file exists, open and return the file object
        fileOpened = open(fileName, openMode, encoding="utf-8")
        if fileOpened:
            print(f"{os.getcwd()}\{fileName} is the targeted file.")
        return fileOpened

def fileCloser(file):
    '''
    Purpose: 
        1. To initiate and display the major functions of the Student Mangement System
        2. To check and read the text file: student_info.txt
        3. If the file does not exist, then ask the user 
    Parameter: 
        1. file (file Object): file object, which is opened by the open()
    Return: 
        1. True if it is closed
    '''
    if not file.closed:
        file.close()
        return True

def studentInfoReader(fileObj):
    '''
    Purpose: 
        1. To read the file line by line and convert the string into dictionary
    Parameter: 
        1. fileObj (file object): file object parameter, which is opened by open() function
    Return:
        1. dictList (list): the list of entries, which are in dictionary form
    '''

    dictList = []
    for line in fileObj:
        dictList.append(eval(line.strip("\n"))) # remove the line break and convert into dictionar
    
    return dictList

def studentInfoWriter(fileObj, dictList: list):
    '''
    Purpose: 
        1. To read the list of dictionary composed and write it into the file
    Parameter: 
        1. fileObj (file object): file object parameter, which is opened by open() function
        2. dictList (list): the list of entries, which are in dictionary form
    Return: nil
    '''

    for dict in dictList:
        fileObj.write(str(dict)+"\n")
    
def optionInputNValidation(optionDict: dict):
    '''
    Purpose: 
        1. To standardize the disply of option keys for user input
        2. To check the user input whether it is in the option key list
    Parameter: 
        1. optionDict (dictionary): a dictionary of option key and description
            Example: {"Y": "confirm", "N": "reject"} -> print out "Input [Y] to confirm, [N] to reject:"
    Return: 
        1. ans (string): the input string from the user
    '''

    # construct the string for display all the keys and the corresponding description
    question = "Input "
    for opt in optionDict:
        question += f"[{opt}] to {optionDict[opt]}, "
    
    question = question.strip(", ") + ": " # strip the last comma

    ans = ""
    # while the user input is not in the list of keys
    while ans not in optionDict.keys():
        ans = input(question) 
        ans = ans.upper().strip() # convert into upper case and remove heading and tailing spaces User Friendly

        # check whether the key is the list of keys and print out warning
        if ans not in optionDict.keys():
            print("The key is not a valid option.")
    
    return ans

def sidInputNValidation():
    '''
    Purpose: 
        1. To get input of student id
        2. Validate the student id in the format of e.g. (s22212852)
    Parameter: nil
    Return: 
        1. sid (String): a student id input by user after passing validation
    '''
    
    sidValid = None
    while not sidValid:
        sidInput = input("Please enter the ID of the student (in the format 's' + 8-digits): ")
        # strip accidentally added space at the start and the end of the sid
        sid = sidInput.strip()
        
        # using regex only accept characters starting with char and ending with char + ".", allow space in the middle
        sidValid = re.fullmatch("^[s]{1}[0-9]{8}$", sid)
        if not sidValid:
            print(f"The input name '{sidInput}' is not in the format of sXXXXXXXX, where X is an integer from 0-9")
        
    return sid

def contactInputNValidation(name):
    '''
    Purpose: 
        1. To get input of contact number
        2. Validate the contact number in the format of HK Number i.e. 8 digits, starting with 2, 3, 5, 6, 9
    Parameter: nil
    Return: 
        1. contact (String): a student id input by user after passing validation
    '''
    
    contactValid = None
    while not contactValid:
        contactInput = input(f"Please enter the contact number of {name}: ")
        # strip accidentally added space at the start and the end of the sid
        contact = contactInput.strip()

        # checking whether the input is numeric, if not skip the loop and ask the user to re-enter
        if contact.isnumeric() == False:
            print("The contact number contains non-numeric characters. Please re-enter the contact number.")
            continue

        # checking whether the length of contact number is 8, if not skip the loop and ask the user to re-enter
        if len(contact) != 8:
            print(
                f"The contact number consists of {len(contact)} numbers, which does not match the standard HK number, 8-numbers.\
                 Please re-enter the contact number. ")
            continue

        # checking whether the starting number of contact number is 2, 3, 5, 6, 7, 8, 9 
        if contact[0] not in ["2", "3", "5", "6", "7", "8", "9"]:
            print("The starting number of the phone number is not 2, 3, 5, 6, 7, 8, 9. Please re-enter the contact number.")
            continue

        contactValid = True
    
    return contact
        
def nameInputNValidation():
    '''
    Purpose: 
        1. To get input of name from user
        2. Validate the name in the format of e.g. (Anna Kit Ying Fong)
    Parameter: nil
    Return: 
        1. name (String): a name input by user after passing validation
    Note:
        Not accepting Non-English chracters, including Chinese and , comma(e.g. John, Ting Chan) and . dot(e.g. Jr.)
    '''
    
    nameValid = None
    while not nameValid:
        nameInput = input("Please enter the name of the student (Only Support English Characters): ")
        # strip accidentally added space at the start and the end of the name
        name = nameInput.strip()
        # Handle the name such that only the first character and first character after space is capital letter
        name = name.lower().title()
        
        # using regex only accept characters starting with char and ending with char + ".", allow space in the middle
        nameValid = re.fullmatch("^[A-Z][a-z]*(\s[A-Z][a-z]*)*$", name)
        if not nameValid:
            print(f"The input name '{nameInput}' contains invalid character(s) / invalid format / empty. Please input a valid name.")
    
    return name

def genderInputNValidation(name: str):
    '''
    Purpose: 
        1. To get input of gender from a user
        2. Validate the gender (accept input like, Male or Woman and convert it to M, F for robustness and user-friendliness)
    Parameter:
        1. name (String): for displaying the student name
    Return: 
        1. genderOut (String): M for Male and F for Female
    '''

    validGenderDict = {
        "M": "M", "F": "F", "MALE": "M", "FEMALE": "F", "MAN": "M", "WOMAN": "F", "MEN": "M", "WOMEN": "F",
        "BOY": "M", "GIRL": "F", "BOYS": "M", "GIRLS": "F"
        } # bulding a gender dict to accept more variation of gender of M and F
    
    genderValid = False

    # Gender input and validation
    while not genderValid:
        genderInput = input(f"Please input the gender of {name} (M/F): ")
        gender = genderInput.upper().strip() # convert into upper case and remove heading and tailing spaces User Friendly
        
        # if the input is not in the dictionary, then warn the user
        if gender not in validGenderDict:
            print(f"The input gender '{genderInput}' is not a valid gender. Please input a valid gender.")
        else:
            # get the gender in the form of M / F
            genderOut = validGenderDict[gender]
            genderValid = True # set it to true to break the loop

    return genderOut

def ageInputNValidation(name: str):
    '''
    Purpose: 
        1. To get input of age from a user
        2. Validate the gender (accept input like, Male or Woman and convert it to M, F for robustness and user-friendliness)
    Parameter:
        1. name (String): for displaying the student name
    Return: 
        1. age (Integer): the age in integer
    '''

    # initialize the parameter age
    age = -1
    # filter any age less than 0 and greater than 150 (a reasonable range for human age)
    while age < 0 or age > 150:
        ageInput = input(f"Please input the age of {name} (accept 0 to 150): ")
        
        # try to turn the string into float and excep ValueError
        try:
            age = float(ageInput.strip())
        except ValueError:
            print(f"The age '{ageInput}' is not a valid number. Please input a valid age.")
            continue

        # Notify the user if the input age is not a decimal and round down
        if age % 1 != 0:
            print(f"The '{ageInput}' input is not an integer. It will be round down to {age//1}")
        
        # Round down the age
        age = int(age//1)

        # warn the user if the age input is not in the range of 0 - 150
        if age < 0:
            print(f"The input age {ageInput} is less than zero. Please input a valid age.")
        elif age > 150:
            print(f"The input age {ageInput} input is greater than 150. Please input a reasonable age.")
    
    return age


'''
Core Functions
'''
def initiation():
    '''
    Purpose: 
        1. To check and read the text file: student_info.txt
        2. To check whether intermediate file "student_info_sample.txt" exists (might be left over when system quits during updating the tex file)
        3. If the file does not exist, then ask the user whether to create student_info.txt
    Parameter: nil
    Return: nil
    '''
    if os.path.exists("student_info_sample.txt"):
        os.remove("student_info_sample.txt")

    # Check whether the student_info.txt exists under the current directory, if not, ask if create one
    s_info = fileOpener(fileName="student_info.txt", openMode="r", allowCreate=True)
    
    # closing the file first
    fileCloser(s_info)

def func_curator():
    '''
    Purpose: 
        1. To take in user input from 1-6 or other character and launch the related function
        2. To initiate and display the major functions of the Student Mangement System
    Parameter: nil
    Return: nil
    '''
    
    # Printing List of function of the system
    print("--- Welcome to Student Mangement System ---\n\
        List of Functions of the System\n\
        1. Add a New Entry\n\
        2. Delete an Entry\n\
        3. Update an Entry by Name\n\
        4. Search for an Entry by Name \n\
        5. Display All Student\n\
        6. Exit \n\
        --------------------------")
    
    # list of valid input for validation
    valid_opt = ["1", "2", "3", "4", "5", "6"]
    option = ""

    # check whether user input is in the the valid option list
    while option not in valid_opt:
        option = input("Please type 1 - 6 to select a function of the system: ")
        option = option.strip() # using option.replace(".", "") to allow user type x

        if option not in valid_opt:
            print("Invlid input. Please input one of the following digits to proceed:\n\
                1, 2, 3, 4, 5, 6")
    
    # Depending on the user's input, direct user to different functions of the system
    if option == "1":
        # calling add entry function
        addEntry()
    elif option == "2":
        # calling delete entry function
        deleteEntry()
    elif option == "3":
        # calling update entry function
        updateEntry()
    elif option == "4":
        # calling search entry function
        searchEntry()
    elif option == "5":
        # calling display all entry function
        displayAll()
    elif option == "6":
        # calling system exit function
        exitSys()

def addEntry():
    '''
    Purpose: 
        1. Ask users about the Name, Gender and Age of the student
        2. Validate User's input of the following criteria
            student ID: sXXXXXXXX (unique)
            Name: accepting format (warning if duplicate)
            Gender: M and F
            Age: integer from 0 to 150
            contact number: XXXXXXXX (warning if duplicate)
        3. Ask user inputs once again if user input is not valid
        4. if student with the same name exists, ask 
    Parameter: nil
    Return: nil
    '''
    print("----- Add New Entry -----")

    # display all the entries for user first
    sDicts = displayAll("internal")

    # creating a list of studnet ID and name storing in the system
    sidList = []
    sNameList = []
    contactList = []

    for sDict in sDicts:
        sNameList.append(sDict["name"])
        sidList.append(sDict["student ID"])
        contactList.append(sDict["contact number"])

    # Setting a while loop such that it does not end until the user confirm the detail
    confirmed = False
    while not confirmed:

        sid = sidInputNValidation()

        if sid in sidList:
            print(f"The student ID {sid} already exists in the system. Please re-enter the student ID.")
            continue
            

        # asking for user input of name
        isDuplicate = True
        while isDuplicate == True:
            name = nameInputNValidation()
            # checking if the name already exists in the system
            if name in sNameList:
                print(f"The name {name} already exists in the system, do you want to add a new entry using the same name?")
                ans = optionInputNValidation({"Y": "confirm to add", "R": "re-enter the name", "M": "return to menu"})
                if ans == "M":
                    # return to menu
                    return None
                elif ans == "R":
                    # skip the following code to re-enter the name
                    continue
                elif ans == "Y":
                    # break the while loop if yes
                    break
            else:
                isDuplicate = False
        
        # asking for gender input
        gender = genderInputNValidation(name)
        # asking for age input
        age = ageInputNValidation(name)
        
        # asking for contact
        isDuplicate = True
        while isDuplicate == True:
            contact = contactInputNValidation(name)
            # checking if the name already exists in the system
            if contact in contactList:
                print(f"The contact number {contact} already exists in the system, do you want to add it?")
                ans = optionInputNValidation({"Y": "confirm to add", "R": "re-enter the contact number", "M": "return to menu"})
                if ans == "M":
                    # return to menu
                    return None
                elif ans == "R":
                    # skip the following code to re-enter the name
                    continue
                elif ans == "Y":
                    # break the while loop if yes
                    break
            else:
                isDuplicate = False

        # display the info to be added
        print(f"Please confirm whether the information is correct.\n\
            Student ID: {sid}\n\
            Name of the student: {name}\n\
            Gender of the student: {gender}\n\
            Age of the student: {age}\n\
            Contact of student: {contact}")

        # asking for confirmation from user
        ans = optionInputNValidation({"Y": "confirm", "R": "re-enter the info", "M": "return to menu"})
        
        if ans == "M":
            # Option: return None to back to menu
            print(f"Discarded student information for student ID: {sid}, name: {name}, gender: {gender}, age: {age} and contact: {contact}. Returning to Menu.")
            return None

        elif ans == "Y":
            # Option: open the file in append mode
            sInfo = fileOpener(fileName="student_info.txt", openMode="a", allowCreate=False)
            newSDict = {"student ID": sid, "name": name, "gender": gender, "age": str(age), "contact number": contact}
            sInfo.write(str(newSDict)+"\n")
            sInfo.close()

            print(f"Added student information for student ID: {sid}, name: {name}, gender: {gender}, age: {age} and contact: {contact}!")
            confirmed = True # ending the while loop
        elif ans == "R":
            # Option: skip the following code to re-enter the name
            print(f"Discared student information for student ID: {sid}, name: {name}, gender: {gender}, age: {age} and contact: {contact}.")
            continue
    
    # return to menu
    return None

def deleteEntry():
    '''
    Purpose: 
        1. Ask users to input a name
            a. if one entry matched -> delete / return to menu / re-enter the name
            b. if two or more entries matched -> delete All / decide one by one / return to menu / re-enter the name
            c. if no entry matched -> return to menu / re-enter the name
        2. Delete entry once confirmed by user
    Parameter: nil
    Return: nil
    '''
    print("----- Delete Entry -----")
    # display all the entries for user first
    sDicts = displayAll("internal")

    # if there is no entries in the system -> force the user to return to menu.
    if len(sDicts) == 0:
        input("There is no entry in the system at the moment. Please Add an entry. Press enter key to return to menu. ")
        return None

    # Setting a while loop such that it does not end until the user confirm the detail
    confirmed = False
    while confirmed == False:
        # If user does not confirm, then reset the matched list of record
        matchList = []

        print("Input the name to be deleted.")
        # Asking user to input name
        name = nameInputNValidation()
        
        # checking if there are matched names existing in the system
        for sDict in sDicts:
            if sDict["name"] == name:
                matchList.append(sDict)
        
        # Case c: for the case of no matching name found
        if len(matchList) == 0:
            print(f"The system found no matching entry.")
            
            # provide options for users (return to menu / re-enter the name)
            ans = optionInputNValidation({"R": "re-enter the name", "M": "return to menu"})
            if ans == "R":
                # Option: Skip the rest of the loop back to enter name
                continue
            elif ans == "M":
                # Option: return to menu by ending the function
                print("Returning to menu without deleting")
                return None
        
        # Case a: for the case of 1 entry with matching name found
        elif len(matchList) == 1:
            print(f"The system found {len(matchList)} matched entry.")
            print(f"The entry to be deleted: {matchList[0]}")

            # provide options for users (delete / return to menu / re-enter the name)
            ans = optionInputNValidation({"Y": "confirm to delete the entry", "R": "re-enter the name", "M": "return to menu"})
            if ans == "M":
                # Option: return to menu by ending the function
                print("Returning to menu without deleting")
                return None
            elif ans == "Y":
                # Option: confirm to delete
                sDicts.remove(matchList[0])

                # create a file call "student_info_temp.txt" is safer, if there is any error, the original record will not be affected.
                try:
                    sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                    studentInfoWriter(sInfoTemp, sDicts) # write the updated list of dict into student_info_sample.txt
                except:
                    # if there is any error, close file then remove the temporary file
                    fileCloser(sInfoTemp)
                    os.remove("student_info_sample.txt")
                    exit() # quit the system
                
                fileCloser(sInfoTemp) # close the file
                os.replace("student_info_sample.txt", "student_info.txt") # replace the original file with the temp file
                print(f"Entry {matchList} deleted.")
                
                # closing the while loop
                confirmed = True 
            elif ans == "R":
                # Option: Skip the rest of the loop back to enter name
                continue

        # Case b: for the case of 2 or more entries with matching name found
        elif len(matchList) > 1:
            print(f"The system found {len(matchList)} entries.")
            print(f"The entries to be deleted: {matchList}")

            # provide options for users (delete All / decide one by one / return to menu / re-enter the name)
            ans = optionInputNValidation({"A": "delete all", "O": "decide one by one", "R": "re-enter the name", "M": "return to menu"})
            
            if ans == "M":
                # Option: return to menu by ending the function
                print("Returning to menu without deleting")
                return None
            
            elif ans == "A":
                # Option: confirm to delete all matched entries
                for item in matchList:
                    sDicts.remove(item) # remove the entry dictionary from the list
                
                # create a file call "student_info_temp.txt" is safer, if there is any error, the original record will not be affected.
                try:
                    sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8") 
                    studentInfoWriter(sInfoTemp, sDicts) # write the updated list of dict into student_info_sample.txt
                except:
                    # if there is any error, close file then remove the temporary file
                    fileCloser(sInfoTemp)
                    os.remove("student_info_sample.txt")
                    exit() # quit the system
                
                fileCloser(sInfoTemp) # close the file
                os.replace("student_info_sample.txt", "student_info.txt") # replace the original file with the temp file
                print(f"All entries {matchList} deleted.")

                # closing the while loop
                confirmed = True
                
            elif ans == "O":
                # Option: Decide whether to delete one by one
                removeList = []

                # looping the matched entries and ask whether to keep or delete one by one
                for item in matchList:
                    print(f"Delete {item}?")
                    
                    # asking whether to keep or delete
                    decision = optionInputNValidation({"Y": "delete", "N": "keep"})
                    if decision == "Y":
                        # if [Y] then remove the item from the list of entries
                        sDicts.remove(item)
                        removeList.append(item)
                
                if len(removeList) != 0:
                    # if there is one or more item to remove
                    # create a file call "student_info_temp.txt" is safer, if there is any error, the original record will not be affected.
                    try:
                        sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                        studentInfoWriter(sInfoTemp, sDicts) # write the updated list of dict into student_info_sample.txt
                    except:
                        # if there is any error, close file then remove the temporary file
                        fileCloser(sInfoTemp)
                        os.remove("student_info_sample.txt")
                        exit() # quit the system
                
                    fileCloser(sInfoTemp) # close the file
                    os.replace("student_info_sample.txt", "student_info.txt") # replace the original file with the temp file
                    print(f"Entry {removeList} deleted.")
                else:
                    # if the user selects to keep all
                    print("All entries are kept")
                
                # end the while loop
                confirmed = True
            elif ans == "R":
                # Option: skip the following code to re-enter the name
                continue
    # return to menu
    return None
                
def updateEntry():
    '''
    Purpose: 
        1. Ask users to input a name
            a. if one entry matched -> ask whether to change student ID, name, gender, age and contact number one by one and then confirm
            b. if two or more entries matched -> ask each entry whether to change student ID, name, gender, age and contact number one by one and then confirm
            c. if no entry matched -> return to menu / re-enter the name
        2. Update the entry with the new input value
    Parameter: nil
    Return: nil
    '''
    print("----- Update Entry -----")
    # display all the entries for user first
    sDicts = displayAll("internal")

    # if there is no entries in the system -> force the user to return to menu.
    if len(sDicts) == 0:
        input("There is no entry in the system at the moment. Please Add an entry. Press enter key to return to menu. ")
        return None

    # Setting a while loop such that it does not end until the user confirm the detail
    confirmed = False
    while confirmed == False:
        matchList = []
        sidList = []
        nameList = []
        contactList = []
        print("Input a name to be updated.")
        # ask user to input name
        name = nameInputNValidation()
        
        # checking if there are matched names existing in the system
        for sDict in sDicts:
            sidList.append(sDict["student ID"])
            contactList.append(sDict["contact number"])
            nameList.append(sDict["name"])
            if sDict["name"] == name:
                matchList.append(sDict)
        
        # Case b: for the case of no matching name found
        if len(matchList) == 0:
            print(f"The system found no matching entry.")
            
            # provide options for users (delete / return to menu / re-enter the name)
            ans = optionInputNValidation({"R": "re-enter the name", "M": "return to menu"})
            if ans == "R":
                # Option: Skip the rest of the loop back to enter name
                continue
            elif ans == "M":
                # Option: return to menu by ending the function
                print("Returning to menu without updating.")
                return None

        # Case a: for the case of 1 or more entries with matching name found
        elif len(matchList) >= 1:
            print(f"The system found {len(matchList)} entries.")
            print(f"The entries to be updated: {matchList}")

            # initiate a list to store the updated entries
            updateList = []

            # looping for each matched entry
            for entry in matchList:
                # create a while loop such that entry will only be saved when the user confirmed (starting point of re-loop)
                editConfirm = False
                while editConfirm == False:
                    # create a while loop such that entry will only be saved when the user confirmed (starting point of re-loop)

                    print(f"Current Selected Entry: {entry}")

                    # Section 1: Update Student ID
                    print(f"The current student ID for {name}: {entry['student ID']}")
                    # provide options for users (update the student ID / keep the student ID unchanged)
                    updateSid = optionInputNValidation({"Y": "proceed to update student ID", "N": "keep the name unchanged"})
                    if updateSid == "Y":
                        # intitiate a loop to check whether the updated student ID already exists in the system 
                        isDuplicate = True
                        while isDuplicate:
                            sid = sidInputNValidation()
                            # if student ID not equal to the original SID and already exists in the list -> reject
                            if sid != entry["student ID"] and sid in sidList:
                                print("The SID already exists in the system for other entries. Please enter a unique SID.")
                            else:
                                # update the student id list for next entry duplication checking
                                sidList.remove(entry["student ID"])
                                sidList.append(sid)
                                isDuplicate = False
                    elif updateSid == "N":
                        # keep the student ID unchagned
                        sid = entry["student ID"]

                    # Section 2: Update Student Name
                    print(f"The current name: {entry['name']}")
                    # provide options for users (update the name / keep the name unchanged)
                    updateName = optionInputNValidation({"Y": "proceed to update student's name", "N": "keep the name unchanged"})
                    if updateName == "Y":
                        # ask for input to update the name
                        # intitiate a loop to check whether the updated student ID already exists in the system 
                        isDuplicate = True
                        while isDuplicate:
                            name = nameInputNValidation()
                            # if student name not equal to the original name and already exists in the list -> ask
                            if name != entry["name"] and name in nameList:
                                print(f"The name already exists in the system for other entries. Do you want to change to {name}?")
                                ans = optionInputNValidation({"Y": "confirm to change", "R": "re-enter the name"})
                                if ans == "R":
                                    # skip the following code to re-enter the name
                                    continue
                                elif ans == "Y":
                                    # update the student id list for next entry duplication checking
                                    nameList.remove(entry["name"])
                                    nameList.append(name)
                                    # break the while loop if yes
                                    break
                            else:
                                nameList.remove(entry["name"])
                                nameList.append(name)
                                isDuplicate = False
                    elif updateName == "N":
                        # keep the name unchagned
                        name = entry["name"]
                    
                    # Section 3: Update Student Gender
                    print(f"The current gender for {name}: {entry['gender']}")
                    # provide options for users (update the gender / keep the gender unchanged)
                    updateGender = optionInputNValidation({"Y": "proceed to update student's gender", "N": "keep the gender unchanged"})
                    if updateGender == "Y":
                        # ask for input to update the gender
                        gender = genderInputNValidation(name)
                    elif updateGender == "N":
                        # keep the gender unchagned
                        gender = entry["gender"]
                    
                    # Section 4: Update Student Age
                    print(f"The current age for {name}: {entry['age']}")
                    # provide options for users (update the age / keep the age unchanged)
                    updateAge = optionInputNValidation({"Y": "proceed to update student's age", "N": "keep the age unchanged"})
                    if updateAge == "Y":
                        # ask for input to update the age
                        age = ageInputNValidation(name)
                    elif updateAge == "N":
                        # keep the age gender unchagned
                        age = entry["age"]
                    
                    # Section 5: Update Student contact
                    print(f"The current contact number: {entry['contact number']}")
                    # provide options for users (update the name / keep the name unchanged)
                    updateContact = optionInputNValidation({"Y": "proceed to update student's contact number", "N": "keep the contact number unchanged"})
                    if updateContact == "Y":
                        # ask for input to update the contact number
                        # intitiate a loop to check whether the updated contact number already exists in the system 
                        isDuplicate = True
                        while isDuplicate:
                            contact = contactInputNValidation(name)
                            # if student name not equal to the original name and already exists in the list -> ask
                            if contact != entry["contact number"] and contact in contactList:
                                print(f"The contact number already exists in the system for other entries. Do you want to change to {contact}?")
                                ans = optionInputNValidation({"Y": "confirm to change", "R": "re-enter the contact number"})
                                if ans == "R":
                                    # skip the following code to re-enter the name
                                    continue
                                elif ans == "Y":
                                    # update the contact list for later contact number comparison
                                    contactList.remove(entry["contact number"])
                                    contactList.append(contact)
                                    # break the while loop if yes
                                    break
                            else:
                                # update the contact list for later contact number comparison
                                contactList.remove(entry["contact number"])
                                contactList.append(contact)
                                # quite the loop
                                isDuplicate = False
                    elif updateName == "N":
                        # keep the name unchagned
                        contact = entry["contact number"]

                    if updateSid == "N" and updateName == "N" and updateGender == "N" and updateAge == "N" and updateContact == "N":
                        # if no change in all info
                        print(f"There is no change in student info for {entry}")
                    else:
                        # summary of updated info
                        print(f"The updated student's information:\n\
                            Student ID: {sid}\n\
                            Name of student: {name}\n\
                            Gender of student: {gender}\n\
                            Age of Student: {age}\n\
                            Contact number of student: {contact}")
                    
                    # provide options for users (confirm to update the entry / re-enter the information)
                    ans = optionInputNValidation({"Y": "confirm to update the entry", "R": "re-enter the information"})
                    if ans == "Y":
                        # Option: confirm to update the entry
                        if updateSid == "Y" or updateName == "Y" or updateGender == "Y" or updateAge == "Y" or updateContact == "Y": # if there is at least one info unpdated
                            sDicts.remove(entry) # remove the selected entry
                            updateList.append({"student ID": sid, "name": name, "gender": gender, "age": str(age), "contact number": contact}) # adding the updated entry to the list of updated
                            sDicts.append({"student ID": sid, "name": name, "gender": gender, "age": str(age), "contact number": contact}) # adding the updated entry of the original copy
                        editConfirm = True # Quiting the while loop for confirmation of the update info
                        confirmed = True # CLosing the while loop
                    elif ans == "R":
                        # Option: Skip the rest of the loop back to enter name
                        continue
            
            # display the list of entry updated
            print(f"The summary of update entries: {updateList}")
            # create a file call "student_info_temp.txt" is safer, if there is any error, the original record will not be affected.
            try:
                sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                studentInfoWriter(sInfoTemp, sDicts) # write the updated list of dict into student_info_sample.txt
            except:
                # if there is any error, close file then remove the temporary file
                fileCloser(sInfoTemp)
                os.remove("student_info_sample.txt")
                exit() # exist system
                        
            fileCloser(sInfoTemp) # close the file
            os.replace("student_info_sample.txt", "student_info.txt") # replace the original file with the temp file
            print("Entries updated")

def searchEntry():
    '''
    Purpose: 
        1. Ask users to input a name
            a. if any entry matched -> display all the matched entry
            b. if no entry matched -> warn user
    Parameter: nil
    Return: nil
    '''
    print("----- Search Entry -----")
    sInfo = fileOpener(fileName="student_info.txt", openMode="r", allowCreate=False)
    if not sInfo:
        # quit the system if file not found, to avoid error
        exit()
    
    matchList = []
    sDicts = studentInfoReader(sInfo)

    # Case of no entries in the system
    if len(sDicts) == 0:
        input("There is no entry in the system at the moment. Please Add an entry. Press enter key to return to menu. ")
        return None
    
    # ask for name input
    name = nameInputNValidation()

    # search for matched entries
    for sDict in sDicts:
        if sDict["name"] == name:
            matchList.append(sDict)
    
    # if no entry found, display 
    if len(matchList) == 0:
        print(f"No matched entry found.")
    
    # print matched entries
    print(f"The system found {len(matchList)} matched entries.")
    print(f"The serach result: {matchList}")

    # press enter key to return to menu
    input("Press enter key to return to menu. ")

def displayAll(callBy="user"):
    '''
    Purpose: 
        1. Display all the entries
    Parameter: nil
    Return:
        1. sDicts (list): List of dictionary of the student entries
    '''

    # open the file
    sInfo = fileOpener(fileName="student_info.txt", openMode="r", allowCreate=False)
    if not sInfo:
        # quit the system if file not found, to avoid error
        exit()
    
    sDicts = studentInfoReader(sInfo)
    print(f"The system currently has {len(sDicts)} entries.")
    print(sDicts)
    
    # if the function is NOT called by other function in the system, add an option for user to press enter key to return to menu
    if callBy != "internal":
        input("Press enter key to return to menu. ")
    fileCloser(sInfo)
    return sDicts

def exitSys():
    '''
    Purpose: 
        1. Exit system
    Parameter: nil
    Return: nil
    '''
    
    # Ask the user whether to exit the system
    print("Do you want to quit the system?")
    ans = optionInputNValidation({"Y": "exit", "N": "stay"})

    if ans == "Y":
        # Option: Exit the system
        print("Quit Student Mangement System. Have a good day!")
        exit()
    elif ans =="N":
        # Option: return to menu
        return None

# Main Execution of functions
initiation()
while True:
    func_curator()