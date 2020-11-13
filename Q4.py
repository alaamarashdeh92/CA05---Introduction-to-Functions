# Q 4
# ******

def last_two(astring):
    if len(astring) > 2:
        return tuple(astring[-2:])
    else :
        return 'Error'
print(last_two('abcdef'))