'''
CIS-128 Project - Student Management System
Name: Cheung Siu Chun
SID: 22212852

version: 0.1
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
        1. file object (class '_io.TextIOWrapper') if file found or created
        2. None if file not found and not created
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
        1. file parameter
    Return: nil
    '''
    if not file.closed:
        file.close()
        return True

def studentInfoReader(fileObj):
    '''
    Purpose: 
        1. To read the file line by line and convert the string into dictionary
    Parameter: 
        1. file parameter
    Return:
        1. 
    '''

    dictList = []
    for line in fileObj:
        dictList.append(eval(line.strip("\n")))
    
    return dictList

def studentInfoWriter(fileObj, dictList: list):
    for dict in dictList:
        fileObj.write(str(dict)+"\n")
    
def optionInputNValidation(optionDict: dict):
    '''
    Purpose: 
        1. To initiate and display the major functions of the Student Mangement System
        2. To check and read the text file: student_info.txt
        3. If the file does not exist, then ask the user 
    Parameter: 
        1. file parameter
    Return: nil
    '''
    question = "Input "
    for opt in optionDict:
        question += f"[{opt}] to {optionDict[opt]}, "
    
    question = question.strip(", ") + ": "

    ans = ""
    while ans not in optionDict.keys():
        ans = input(question)
        ans = ans.upper().strip()
        if ans not in optionDict.keys():
            print("The key is not a valid option.")
    
    return ans

def nameInputNValidation():
    '''
    Purpose: 
        1. To get input of name from user
        2. Validate the name in the format of e.g. (Anna Kit Ying Fong)
    Parameter: nil
    Return: 
        1. name (String): a name input by user after passing validation
    Note:
        Not accepting Non-English chracters at the moment, including Chinese and , comma(e.g. John, Ting Chan) and . dot(e.g. Jr.)
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
        1. gender (String): M for Male and F for Female
    '''

    validGenderDict = {
        "M": "M", "F": "F", "MALE": "M", "FEMALE": "F", "MAN": "M", "WOMAN": "F", "MEN": "M", "WOMEN": "F",
        "BOY": "M", "GIRL": "F", "BOYS": "M", "GIRLS": "F"
        } # bulding a gender dict to accept more variation of gender of M and F
    
    genderValid = False

    # Gender input and validation
    while not genderValid:
        genderInput = input(f"Please input the gender of {name} (M/F): ")
        gender = genderInput.upper().strip()
        
        if gender not in validGenderDict:
            print(f"The input gender '{genderInput}' is not a valid gender. Please input a valid gender.")
        else:
            genderOut = validGenderDict[gender]
            genderValid = True

    return genderOut

def ageInputNValidation(name: str):
    '''
    Purpose: 
        1. To get input of age from a user
        2. Validate the gender (accept input like, Male or Woman and convert it to M, F for robustness and user-friendliness)
    Parameter:
        1. name (String): for displaying the student name
    Return: 
        1. gender (String): M for Male and F for Female
    '''

    age = -1
    while age < 0 or age > 150:
        # filter any age less than 0 and greater than 150 (a reasonable range for human age)
        ageInput = input(f"Please input the age of {name} (accept 0 to 150): ")
        try:
            age = float(ageInput.strip())
        except ValueError:
            print(f"The age '{ageInput}' is not a valid number. Please input a valid age.")
            continue

        if age % 1 != 0:
            print(f"The '{ageInput}' input is not an integer. It will be round down to {age//1}")
        
        age = int(age//1)

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
        2. If the file does not exist, then ask the user 
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
        1. Ask user's about the Name, Gender and Age of the student
        2. Validate User's input of the following criteria
            Name: Alpha Characters + "." Example: Neymar Jr. Valid
            Gender: M and F (Are we going to consider some of the new Gender in U.S.?)
            Age: integer from 0 to 130 
        3. Ask user inputs once again if user input is not valid
        4. if student with the same name exists, ask 
    Parameter: nil
    Return: nil
    '''
    print("----- Add New Entry -----")
    sDicts = displayAll("internal")
    sNameList = []
    for sDict in sDicts:
        sNameList.append(sDict["name"])

    confirmed = False

    while not confirmed:
        name = nameInputNValidation()

        # check for repeated name
        if name in sNameList:
            print(f"The name {name} already exists in the system, do you want to add a new entry using the same name?")
            ans = optionInputNValidation({"Y": "confirm to add", "R": "re-enter the name", "M": "return to menu"})
            if ans == "M":
                return None
            elif ans == "R":
                continue

        gender = genderInputNValidation(name)
        age = ageInputNValidation(name)
        
        print(f"Please confirm whether the information is correct.\n\
            Name of the student: {name}\n\
            Gender of the student: {gender}\n\
            Age of the student: {age}")

        ans = optionInputNValidation({"Y": "confirm", "R": "re-enter the name", "M": "return to menu"})
        
        if ans == "M":
            print(f"Discarded student information for {name}, gender: {gender} and age: {age}. Returning to Menu.")
            return None
        elif ans == "Y":
            sInfo = fileOpener(fileName="student_info.txt", openMode="a", allowCreate=False)
            newSDict = {"name": name, "gender": gender, "age": str(age)}
            sInfo.write(str(newSDict)+"\n")
            print(f"Added student information for {name}, gender: {gender} and age: {age}!")
            confirmed = True
        elif ans == "R":
            print(f"Discared student information for {name}, gender: {gender} and age: {age}.")
            continue
    
    return None

def deleteEntry():
    print("----- Delete Entry -----")
    sDicts = displayAll("internal")

    if len(sDicts) == 0:
        input("There is no entry in the system at the moment. Please Add an entry. Press enter key to return to menu. ")
        return None

    confirmed = False
    while confirmed == False:
        # If user does not confirm, then reset the matched list of record
        matchList = []

        print("Input the name to be deleted.")
        # Asking user to input name
        name = nameInputNValidation()
        
        for sDict in sDicts:
            if sDict["name"] == name:
                matchList.append(sDict)

        if len(matchList) == 0:
            print(f"The system found no matching entry.")
            
            ans = optionInputNValidation({"R": "re-enter the name", "M": "return to menu"})
            if ans == "R":
                continue
            elif ans == "M":
                print("Returning to menu without deleting")
                return None
        
        elif len(matchList) == 1:
            print(f"The system found {len(matchList)} matched entry.")
            print(f"The entry to be deleted: {matchList[0]}")
            ans = optionInputNValidation({"Y": "confirm to delete the entry", "R": "re-enter the name", "M": "return to menu"})
            
            if ans == "M":
                print("Returning to menu without deleting")
                return None
            elif ans == "Y":
                
                sDicts.remove(matchList[0])
                try:
                    sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                    studentInfoWriter(sInfoTemp, sDicts)
                except:
                    fileCloser(sInfoTemp)
                    os.remove("student_info_sample.txt")
                    exit()
                
                fileCloser(sInfoTemp)
                os.replace("student_info_sample.txt", "student_info.txt")
                print(f"Entry {matchList} deleted.")
                confirmed = True
            elif ans == "R":
                continue

        elif len(matchList) > 1:
            print(f"The system found {len(matchList)} entries.")
            print(f"The entries to be deleted: {matchList}")
            ans = optionInputNValidation({"A": "delete all", "O": "decide one by one", "R": "re-enter the name", "M": "return to menu"})
            
            if ans == "M":
                print("Returning to menu without deleting")
                return None
            elif ans == "A":
                for item in matchList:
                    sDicts.remove(item)
                
                # create a file call "student_info_temp.txt" is safer, if there is any error, the original record will not be affected.
                try:
                    sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                    studentInfoWriter(sInfoTemp, sDicts)
                except:
                    fileCloser(sInfoTemp)
                    os.remove("student_info_sample.txt")
                    exit()
                
                fileCloser(sInfoTemp)
                os.replace("student_info_sample.txt", "student_info.txt")
                print(f"All entries {matchList} deleted.")

                confirmed = True
                
            elif ans == "O":
                removeList = []
                for item in matchList:
                    print(f"Delete {item}?")
                    decision = optionInputNValidation({"Y": "delete", "N": "keep"})
                    if decision == "Y":
                        sDicts.remove(item)
                        removeList.append(item)
                
                # create a file call "student_info_temp.txt" is safer, if there is any error, the original record will not be affected.
                if len(removeList) != 0:
                    try:
                        sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                        studentInfoWriter(sInfoTemp, sDicts)
                    except:
                        fileCloser(sInfoTemp)
                        os.remove("student_info_sample.txt")
                        exit()
                
                    fileCloser(sInfoTemp)
                    os.replace("student_info_sample.txt", "student_info.txt")
                    print(f"Entry {removeList} deleted.")
                else:
                    print("All entries are kept")

                confirmed = True
            elif ans == "R":
                continue

    return None
                
def updateEntry():
    print("----- Update Entry -----")
    sDicts = displayAll("internal")

    if len(sDicts) == 0:
        input("There is no entry in the system at the moment. Please Add an entry. Press enter key to return to menu. ")
        return None

    confirmed = False
    while confirmed == False:
        matchList = []
        print("Input a name to be updated.")
        name = nameInputNValidation()
        
        for sDict in sDicts:
            if sDict["name"] == name:
                matchList.append(sDict)

        if len(matchList) == 0:
            print(f"The system found no matching entry.")
            
            ans = optionInputNValidation({"R": "re-enter the name", "M": "return to menu"})
            if ans == "R":
                continue
            elif ans == "M":
                print("Returning to menu without updating.")
                return None
        
        elif len(matchList) == 1:
            print(f"The system found {len(matchList)} entry.")
            print(f"The entry to be updated: {matchList[0]}")

            editConfirm = False
            while editConfirm == False:
                updateName = optionInputNValidation({"Y": "proceed to update student's name", "N": "keep the name unchanged"})
                if updateName == "Y":
                    name = nameInputNValidation()
                elif updateName == "N":
                    name = matchList[0]["name"]

                print(f"The current gender for {name}: {matchList[0]['gender']}")
                updateGender = optionInputNValidation({"Y": "proceed to update student's gender", "N": "keep the gender unchanged"})
                if updateGender == "Y":
                    gender = genderInputNValidation(name)
                elif updateGender == "N":
                    gender = matchList[0]["gender"]

                print(f"The current age for {name}: {matchList[0]['age']}")
                updateAge = optionInputNValidation({"Y": "proceed to update student's age", "N": "keep the age unchanged"})
                if updateAge == "Y":
                    age = ageInputNValidation(name)
                elif updateAge == "N":
                    age = matchList[0]["age"]

                if updateName == "N" and updateGender == "N" and updateAge == "N":
                    print("There is no change in student info.")
                else:
                    print(f"The updated student's information:\n\
                        Name of student: {name}\n\
                        Gender of student: {gender}\n\
                        Age of Student: {age}")
                ans = optionInputNValidation({"Y": "confirm to update the entry", "R": "re-enter the information"})

                if ans == "Y":
                    if updateName == "Y" or updateGender == "Y" or updateAge == "Y":
                        sDicts.remove(matchList[0])
                        sDicts.append({"name": name, "gender": gender, "age": age})
                        try:
                            sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                            studentInfoWriter(sInfoTemp, sDicts)
                        except:
                            fileCloser(sInfoTemp)
                            os.remove("student_info_sample.txt")
                            exit()
                        
                        fileCloser(sInfoTemp)
                        os.replace("student_info_sample.txt", "student_info.txt")
                        print("The entry is updated.")
                    
                    editConfirm = True
                    confirmed = True
                
                elif ans == "R":
                    continue

        elif len(matchList) > 1:
            print(f"The system found {len(matchList)} entries.")
            print(f"The entries to be updated: {matchList}")

            updateList = []

            for entry in matchList:
                editConfirm = False
                while editConfirm == False:
                    print(f"Update for {entry}")
                    print(f"The current name: {entry['name']}")
                    updateName = optionInputNValidation({"Y": "proceed to update student's name", "N": "keep the name unchanged"})
                    if updateName == "Y":
                        name = nameInputNValidation()
                    elif updateName == "N":
                        name = entry["name"]
                    
                    print(f"The current gender for {name}: {entry['gender']}")
                    updateGender = optionInputNValidation({"Y": "proceed to update student's gender", "N": "keep the gender unchanged"})
                    if updateGender == "Y":
                        gender = genderInputNValidation(name)
                    elif updateGender == "N":
                        gender = entry["gender"]

                    print(f"The current age for {name}: {entry['age']}")
                    updateAge = optionInputNValidation({"Y": "proceed to update student's age", "N": "keep the age unchanged"})
                    if updateAge == "Y":
                        age = ageInputNValidation(name)
                    elif updateAge == "N":
                        age = entry["age"]

                    if updateName == "N" and updateGender == "N" and updateAge == "N":
                        print("There is no change in student info.")
                    else:
                        print(f"The updated student's information:\n\
                            Name of student: {name}\n\
                            Gender of student: {gender}\n\
                            Age of Student: {age}")
                    
                    ans = optionInputNValidation({"Y": "confirm to update the entry", "R": "re-enter the information"})

                    if ans == "Y":
                        if updateName == "Y" or updateGender == "Y" or updateAge == "Y":
                            sDicts.remove(entry)
                            updateList.append({"name": name, "gender": gender, "age": age})
                            sDicts.append({"name": name, "gender": gender, "age": age})
                        editConfirm = True
                        confirmed = True
                    elif ans == "R":
                        continue
            
            print(f"The summary of update entries: {updateList}")
            try:
                sInfoTemp = open("student_info_sample.txt", "w", encoding="utf-8")
                studentInfoWriter(sInfoTemp, sDicts)
            except:
                fileCloser(sInfoTemp)
                os.remove("student_info_sample.txt")
                exit()
                        
            fileCloser(sInfoTemp)
            os.replace("student_info_sample.txt", "student_info.txt")
            print("Entries updated")

def searchEntry():
    print("----- Search Entry -----")
    sInfo = fileOpener(fileName="student_info.txt", openMode="r", allowCreate=False)
    if not sInfo:
        # quit the system if file not found, to avoid error
        exit()
    
    matchList = []
    sDicts = studentInfoReader(sInfo)

    if len(sDicts) == 0:
        input("There is no entry in the system at the moment. Please Add an entry. Press enter key to return to menu. ")
        return None
    
    name = nameInputNValidation()

    for sDict in sDicts:
        if sDict["name"] == name:
            matchList.append(sDict)
    
    if len(matchList) == 0:
        print(f"No matched entry found.")

    print(f"The system found {len(matchList)} matched entries.")
    print(f"The serach result: {matchList}")

    input("Press enter key to return to menu. ")

def displayAll(callBy="user"):
    sInfo = fileOpener(fileName="student_info.txt", openMode="r", allowCreate=False)
    if not sInfo:
        # quit the system if file not found, to avoid error
        exit()
    
    sDicts = studentInfoReader(sInfo)
    print(f"The system currently has {len(sDicts)} entries.")
    print(sDicts)
    if callBy != "internal":
        input("Press enter key to return to menu. ")
    fileCloser(sInfo)
    return sDicts

def exitSys():
    print("Do you want to quit the system?")
    ans = optionInputNValidation({"Y": "exit", "N": "stay"})

    if ans == "Y":
        print("Quit Student Mangement System. Have a good day!")
        exit()
    elif ans =="N":
        return None

# Main Execution of functions
initiation()
while True:
    func_curator()