def vogal(ch):
    if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U':
        return True
    else:
        return False


char = input('Vogal:')
if len(char) == 1:
    print(vogal(char))

