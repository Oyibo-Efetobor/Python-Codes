# def reverse_string(sentence):
#     word = sentence[::-1]
#     return print(word)


# reverse_string("We will conquere COVID-19")

def is_balanced(data):
    if data.count('(') == data.count(')'):
        if data.count('[') == data.count(']'):
            if data.count('{') == data.count('}'):
                data = True
    else:
        data = False
                
    if data:
        return print(data)
    else:
        return print(data) 
    


is_balanced("[a+b]*(x+2y)*{gg+kk}")

