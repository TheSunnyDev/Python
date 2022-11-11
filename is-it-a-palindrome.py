Write a function that checks if a given string (case insensitive) is a palindrome.

Solution:
def is_palindrome(s):
    if s.upper().lower()[::-1] == s.upper().lower():
        return True
    else:   
        return False
