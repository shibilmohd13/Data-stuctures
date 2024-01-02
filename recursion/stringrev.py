def revstring(string):
    if not string:
        return ''
    else:
        return string[-1] + revstring(string[:-1])


print(revstring('hello my name is shibl'))