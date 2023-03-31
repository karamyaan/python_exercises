"""This function give us al of the 26 english alphabets mapping each with the corresponding integer. """

import string

eng_ltts = string.ascii_lowercase

def alphabets(letters):
    res_dict = {letter:number for number,letter in enumerate(letters , start = 1)}
    return res_dict
    
print(alphabets(eng_ltts))

