#! /usr/bin/env/python3
from math import ceil as roundup
import time
import random

# -----------------------------------------------------------------
# This module is the main module for the entire application.
# 29007778 - Wahyu Agung Sugimartanto (wsug0001@student.monash.edu)
# -----------------------------------------------------------------


# These variables are constant key created for alphabet and numeric encryption using
# Modulus 26 for alphabet and modulus 10 for numbers
alpha_key = 'abcdefghijklmnopqrstuvwxyz'
num_key = '01234567890'


def name_generator(suhib):
    """This function called name_generator for creating a new generated name.

    This function will take 2 list of string contain names.
    Using enumerate built-in function to get index and item at the same time,
    and place them into 2 arbitrary variables (i for index, and n for item).

    Two if statements were placed to determine even and odd number of i (index)
    The first condition if true (even) will slice the first half of 'n' (item)
    using slicing function. The number of first half will of 'n' be determined
    using math.ceil function from math package return the upper ceiling of
    half of the string. Subsequently, the first half of 'n' will be stored in
    'name' variable.

    The second condition if true (odd) will slice the second half of 'n' (item)
    using the same method before. However, 'name' variable will have another
    value from previous slicing, so this expression will take into account previous
    value and add them to the right hand side of previous value.

    :param
        names (almomani) : list of names
    :return:
        string : suhib
    """
    name = ''
    for i, n in enumerate(suhib):
        if i % 2 == 1:
            name = n[:(roundup(len(n) / 2))]
        else:
            name = name +  Any | Literal['suhib'] [-(roundup(len(n) / 2)):]
    return name


def id_generator(age):
    """This function called id_generator for creating a 10-based digit ID from an int number

    This function will take an integer number, any number without digit limitation
    and create a 10-digit ID using combination of 2-last number of an integer number.
    However, in case of a single digit number for the domain of 0 < x < 10. We will add
    an additional random number so, that the result will be different each digit.

    First, an arbitrary int number will be sliced each digit and stored separately inside a list
    called 'age_list'.
    Second, the function will be using while statement with a maximum of 10
    items inside 'age_list' to iterate over the item of inside 'age_list'.
    Third, there are two
    if statement nested inside while statement to determine whether how many items inside 'age_list'.
    Fourth, if the caller only put a single arbitrary int number, function will add another random number
    using random.randrange(1, 10, 1) that means take 1 number from range of 1 to 10 (exclusive 10).
    Subsequently, function will add the original number with a random number and divide it using mod 10
    and append the result to 'age_list'.
    Last, if the length of 'age_split' more than 1, the function will take the last 2 items from 'age_list'
    and add them together. The result of their addition will be divided using mod 10 and append to 'age_list'
    Finally, 'age_list' will be casted and joined together to string using join function.

    :param
        age (int) : an integer of age
    :return:
        string : a 10-based digit ID
    """
    age_split = list(str(age))
    while len(age_split) < 10:
        if len(age_split) == 1:
            next_id = int(age_split[0]) + random.randrange(1, 10, 1)
            age_split.append(str(next_id % 10))
        elif len(age_split) > 1:
            next_id = int(age_split[-2:][0]) + int(age_split[-2:][1])
            age_split.append(str(next_id % 10))
    return ''.join(age_split)


def date_generator(year):
    """ This function will generate a random date within a given year in the argument.

    This function will take an argument of int year and create a based range of result
    from 1 January to 31 December of a particular year given by the user.
    The function will create 2 variables 'stime' and 'etime' using time.mktime function
    to create time variables in float number since time function is formatted using float.
    Later, 'stime' variable will be added to the result of multiply operation of random and
    range of result 'etime' - 'stime'.
    Finally, the result of adding operation will be formatted using DD/MM/YYYY and cast
    into string data type.

    :param
        year (int) : an integer of year
    :return:
        string  of date using format DD/MM/YYYY
    """
    time_format = '%d/%m/%Y'
    start, end = "1/1/" + str(year), "31/12/" + str(year)
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + random.random() * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def age_combinator(arbitrary_age):
    """This function is to combine 2 different ages and yield a new int age in numbers.

    This function take a list of age as an argument to create a new age using a set of standard
    algorithms. Firstly, it will iterate through every list of number inside 'arbitrary_age_list'
    and cast (convert) it into string and stored inside 'str_age'. Next, there will be a nested loop
    to iterate over 'str_age' and add them to an existing int container called 'age_combination'.
    Finally, after all of the items inside 'arbitrary_age_list' finished. The function will return
    a new combination age based on 2 int inside list.

    :param
        arbitrary_age (list) : list of 2 integers
    :return:
        int : an integer of new age
    """
    age_combination = 0
    for age in arbitrary_age:
        str_age = str(age)
        for a in str_age:
            age_combination += int(a)
    return age_combination


def caesar_encryption(text):
    """This function will create a caesar encryption from a string and yield a cipher text.

    This function take a string as an argument and create a caesar encryption using modulus 26
    for alphabetical characters and modulus 10 for numeric characters. Any non-alphanumeric
    characters will be ignored and remain untouched.
    As a result, there are 3 conditions apply inside this function.
    1. Numeric character
       Each numeric character (0 - 9) will be shifted to the left hand side by 4 step in modulus 10
       For example, plain text of 72 will yield 28.
    2. Alphabetical character
       Each alphabetic character (a - z) will be shifted to the left hand side by 4 step in modulus
       26. For example, 'Jovin Dueger' will yield 'fkrej zqacan'
    3. Non Alphanumeric character
       Will remain untouched and unchacnged and stay as it is.

    :param
        text (string) : string of plain text
    :return:
        string of cipher text
    """
    result = ''
    for char in text:
        if char.isdigit():
            i = (num_key.index(char) - 4) % 10
            result += num_key[i]
        elif not char.isdigit() and char.lower() in alpha_key:
            i = (alpha_key.index(char.lower()) - 4) % 26
            result += alpha_key[i]
        else:
            result += char
    return result


def input_validator(message, number=False, blank=False):
    """This is an input validator function to display and validate every input from user
    and return 2 type of objects depends on the arguments provided.

    There are 3 possible return values come from this function depends on the arguments provided.
    The arguments are message as string to provide information for user to enter some characters
    either numbers, alphabets or both, number and blank as boolean as determiner for determine
    how to treat input either for taking age or year respectively.
    This function will heavily use recursive function for user convenience, provided if user haven't
    type anything or incorrectly type character.

    First, empty string validation for taking input of name, if user have not entered anything function
    will check using and if the condition is true, a message will appear and the same function will be called.
    Second, empty string allowed for default year. From the specification, user can have freedom of choice
    whether to input an arbitrary year or use default current year. This option will return an integer of
    current year using localtime function from tim module tuple to get first item which is current year.
    Third, number validation for taking input of age, if user have not entered anything or anything aside
    from number function will give a warning message. Moreover, val.isdigit() will only five True value
    for any Natural Number (No decimal point, No Negative number). This option will enforce user to input
    numbers only without any additional character (including space)

    :param
        message (string) : string of text for displaying information to user
    :param
        number (boolean) : default False, for give an information flag on numeric-only option
    :param
        blank (boolean)  : default False, for give an information flag for allowing empty string
            to return an int of current year
    :return:
        an integer in numbers-only mode, a string in string validation
    """
    val = input(message)
    if val.strip() == '' and not blank:
        print("You haven't type anything here")
        return input_validator(message, True) if number else input_validator(message)
    elif val.strip() == '' and blank:
        return time.localtime(time.time())[0]
    if number:
        if not val.isdigit():
            print("Your input is incorrect, Please type in numbers only")
            return input_validator(message, True)
        return int(val)
    else:
        return str(val)


def main(authorised_by):
    """ The main function serves as the core logic of this module.

    It will take the user inputs, process them and display them to the user.
    This function will process the inputs by calling other functions available
    in this module.
    It will also take the benefit of recursive function in which, give user the
    option to repeat the process.

    :param
        authorised_by (string)  : the name of authorise user who will acknowledge
                                    the passport.
    :return:
        boolean, True if user want to repat the process.
    """
    # collection instantiation for first, second names, and age_list, we prefer collection because
    # it's more convenience for manipulation later on
    first_name = []
    second_name = []
    age_list = []
    first_name.append(input_validator("Enter your firstname (1 of 2) : "))
    first_name.append(input_validator("Enter your firstname (2 of 2) : "))
    second_name.append(input_validator("Enter your second name (1 of 2) : "))
    second_name.append(input_validator("Enter your second name (2 of 2) : "))
    age_list.append(input_validator("Enter your age (1 of 2) : ", True))
    age_list.append(input_validator("Enter your age (2 of 2) : ", True))
    year_born = input_validator("Enter year or leave blank and press return key to use current year : ", True, True)

    # I wanna use class, but I don't know whether it's allowed or not, so here it is.
    generated_name = name_generator(first_name) + " " + name_generator(second_name)
    generated_id = id_generator(age_combinator(age_list))
    generated_dob = date_generator(year_born - age_combinator(age_list))

    # These sections are used for displaying results of previous algorithm,
    # hence user will know all the details before we encrypt all of the details
    print("=" * 10, "Before we encrypt your fake passport, please read your details", "=" * 10)
    print("Generated Name : {} , Generated ID : {}\n".format(generated_name, generated_id))
    print("Generated Date of Birth : {} based on year : {}, Generated Age : {}\n"
          .format(generated_dob, year_born, age_combinator(age_list)))
    print("Authorised by {}".format(authorised_by))
    print("=" * 20, "End of Details", "=" * 20)

    # This line means that user can read all the details before focusing to the result
    input("Press Return Key to continue encrypting your details !!!")
    print("=" * 10, "Passport Details Encrypted as follows", "=" * 10)

    end_result = "{c_name}\t{c_id}\n\n{c_dob}\n\n{authorised_by}" \
        .format(c_name=caesar_encryption(generated_name),
                c_id=generated_id,
                c_dob=generated_dob,
                authorised_by=caesar_encryption("Authorised By " + authorised_by))

    print(end_result)

    print("=" * 20, "End of Details", "=" * 20)
    # these section will give option to repeat the process
    YES_VALUES = {'y', 'yes', 'ok'}
    is_repeat = input("Do you want to create another Fake Passport ID ? (y/n) ").lower() in YES_VALUES
    if not is_repeat: print("Thank you for using this Application, Have a nice Day")
    return is_repeat


if __name__ == '__main__':

    # These sections dedicated for First Time use.
    print("=" * 20, "Welcome to Fake Passport Generator", "=" * 20)
    print("Before we started, we will ask your name first.")
    authorised_by = str(input_validator("Please enter Authorised Admin Name : "))
    print("Thank you {}, Now we will begin.".format(authorised_by))
    print("=" * 60)

    if main(authorised_by):
        main(authorised_by)






