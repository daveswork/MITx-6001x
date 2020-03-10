import string

def shifty(shift):
    offset = shift
    if shift < 0:
        shift = shift * -1
    letters = [x for x in string.ascii_lowercase]
    letters_upper = [x for x in string.ascii_uppercase]
    shifted = [letters[i] for i in range(-26 + (shift), shift)]
    shifted_upper = [letters_upper[i] for i in range(-26 + shift, shift)]
    if offset >= 0:
        cipher = dict(zip(letters, shifted))
        cipher.update(dict(zip(letters_upper, shifted_upper)))
    else:
        cipher = dict(zip(shifted, letters))
        cipher.update(dict(zip(shifted_upper, letters_upper)))
    return cipher

def crypty(text, cipher_dict):
    cypher = cipher_dict
    out_text = ''
    for letter in text:
        if letter in cypher.keys():
            out_text = out_text + cypher[letter]
        else:
            out_text = out_text + letter

    return out_text


#test, this is only a test = uftu, uijt jt pomz b uftu
# test = uftu

print(crypty('hello', shifty(2)))