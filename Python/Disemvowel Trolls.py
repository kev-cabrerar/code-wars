import re


def disemvowel(string):

    return(re.sub('a|A|e|E|i|I|o|O|u|U', '', string))
