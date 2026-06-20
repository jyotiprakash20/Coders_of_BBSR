'''Camel case of a given sentence'''
def camel_case(sentence):
    result = []

    capitalize_next= False

    for i in range(len(sentence)):
        if sentence[i] ==' ':
            capitalize_next= True
        elif capitalize_next:
            result.append(sentence[i].upper())
            capitalize_next= False
        else:
            result.append(sentence[i])
    return ''.join(result)

str= 'hello world'
result= camel_case(str)
print(result)