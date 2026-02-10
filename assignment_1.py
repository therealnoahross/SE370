# Returns a number to the power of 3, accepting only integers and floats
def cube_number(n):
    if type(n) != int and type(n) != float:
        return "Wrong data type!"
    return n**3

#Checks to see what a number is
def check_number(n):
    if type(n) != int:
        return "This is not an integer"
    #If a number is greater than 0 continue
    if n > 0:
        #If a number is even continue
        if n % 2 == 0:
            return "positive and even"
        #Else, if a number is odd, continue
        elif n % 2 != 0:
            return "positive and odd"
    elif n < 0:
        if n % 2 == 0:
            return "negative and even"
        elif n % 2 != 0:
            return "negative and odd"
    elif n == 0:
            return "Zero not valid"
        
#This function takes in a string and returns the number of vowels it contains
def count_vowels(string):
    vowel = "aeiouAEIOU"
    count = 0
    #Counts the number of vowels in the string and adds it to the count variable
    for char in string:
        if char in vowel:
            count += 1
    return count

#This functon does the same as the previous function, just using a while loop
def count_vowels_while(string):
    vowel = "aeiouAEIOU"
    count = 0
    index = 0
    #while the index is less than the length of the word, check to see if the specific character is in the string of vowels
    while index < len(string):
        if string[index] in vowel:
            count += 1
        index += 1
    return count

#This function adds a key and a value to a prexisting dict
def add_to_dict(dictionary, key, value):
    #Iterate through the keys
    for original_key in dictionary:
        #Check if the new key matches an already used key
        if key == original_key:
            return "Key already exists!"
    #using the .update function, add a key and value to the dict
    dictionary.update({key: value})
    return dictionary

#This function takes in two lists ad uses the first as a key and the second as a value for a new dict
def make_dict(list_a, list_b):
    new_dict = dict()
    #If the user tries to input an incorrect type, return this string
    if type(list_a) != type(list()) or type(list_b) != type(list()):
        return "Wrong data type!" 
    #if the length of the lists do not match, return this message
    if len(list_a)!= len(list_b):
        return f"Length mismatch! length of list 1 is {len(list_a)} while length of list 2 is {len(list_b)}"
        #if the lengths do match, add the specific indexes of each list together
    else:
        for i in range(len(list_a)):
            new_dict.update({list_a[i]: list_b[i]})
        return new_dict

#Creates a function that checks to see if a number is prime
def check_prime(n):
    if n < 2:
        return "Number must be greater than or equal to 2"
    if n % 2 == 0:
        return False
    if n == 2:
        return True
    #This function checks to see if an odd number is divisible by another odd number 1-10
    for i in range(3, 10, 2):
        #If it is divisible by an odd num and the num is not divided by itself, its not a prime, so returns false
        if n % i == 0 and n/i != 1:
            return False
    return True

#This function takes a list of numbers and returns whether each number is or is not a primse
def check_prime_list(n):
    new_list = []
    #Iterate through a range the length of the list
    for i in range(len(n)):
        #If num is less than two return message
        if n[i] < 2:
            new_list.append('Number must be greater than or equal to 2')
            #Else if the number is 2 it is a prime
        elif n[i] == 2:
            new_list.append(True)
        else:
            #Create a variable prime to check if it is a prime number
            prime = True
            #Iterate through range of values up to the number
            for index in range(2, n[i]):
                #If the number is divisible set prime equal to False
                if n[i] % index == 0:
                    prime = False
            #Append the result to the list
            new_list.append(prime)
    return new_list

#Function to check if a string is the same forwards and backwards ie. is a palindrome
def check_palindrome(string):
    new_string = ""
    temp_list = []
    #Iterate through the string to create list
    for i in range(len(string)):

        temp_list += string[i]

    #Iterate through list to create new string
    for i in range(len(temp_list)):
        #add the list to the new string backwards 
        new_string += temp_list[-i-1]
    # if the strings are equal return True for a palindrome
    if new_string == string:
        return True
    #If not a palindrome return False
    else:
        return False
