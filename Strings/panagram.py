'''Check if given String is Pangram or not'''

from string import ascii_lowercase

def pangram(s):

    for i in ascii_lowercase:
        found = False

        for j in range(len(s)):
            if i==s[j].lower():
                found = True
                break
        if not found:
            return False
    return True

str='The quick brown fox jumps over the lazy cat'

if pangram(str)==True:
    print('True')
else:
    print('False')
