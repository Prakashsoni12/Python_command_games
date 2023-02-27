

lower_case = "a quick brown fox jumps over the lazy dog"
upper_case = (lower_case.upper())

lower_unicode = {i:ord(i) for i in lower_case if i!= ' '}
print(lower_unicode.items())

upper_unicode = {i:ord(i) for i in upper_case if i!= ' '}
print(upper_unicode.items())

char_unicode = [chr(i) for i in range(100)]
print(char_unicode)

char_unicode1 = {i: chr(i) for i in range(2038,2500)}
print(char_unicode1)

