import os, platform, sys
#returns what type of commenting style to use(by programming language)
def comment(x): 
    return {
        'c': {"/*", "*/"},
        'h': {"<!--", "-->"},
        'p': {"###", "###"}
        }.get(x, 9)
#returns a string broken up every nth character,
#or just the string if it's length < user specified max length
def string_breakup(line, max_length): 
    if(line < max_length): return line
    return [line[i:i+max_length] for i in range(0, len(line), max_length)]
#append string with correct comments!  math is involved :) ish
def string_append(string, max_length, b, e):
    length = len(string)
    print "\nlength of string: %r" %(length)
    number_of_spaces = (max_length-length)
    return b + string + " "*number_of_spaces + e

#determines the maximum string length from the stirings inputted
def string_maxlength(*args):
    max = 0
    for a in args:
        if max < len(a): max = len(a)
    return max

filename = raw_input("Enter filename>")
description = raw_input("Enter description>")
authors = raw_input("Enter authors>")
max_length = input("Max length to split the string?>")
comment_style = raw_input("Style of commenting?([c], [h]tml"
                +",[p]ython>")

comment_style = comment(comment_style)
if(comment_style == 9): sys.exit()

end_comment, begin_comment = comment_style

filename_string = "FILENAME: " + filename
description_string = "DESCRIPTION: " + description
author_string = "AUTHORS: " + authors
new_max = string_maxlength(filename_string,\
description_string, author_string)
if (max_length > new_max):
    max_length = new_max

filename_string = string_breakup(filename_string, max_length)
description_string = string_breakup(description_string, max_length)
author_string = string_breakup(author_string, max_length)


filename_string = [string_append(i, max_length, begin_comment, end_comment) for i in filename_string]
description_string = [string_append(i, max_length, begin_comment, end_comment) for i in description_string]
author_string = [string_append(i, max_length, begin_comment, end_comment) for i in author_string]
to_copy = '\n'.join(filename_string) +\
'\n' + '\n'.join(description_string) +\
'\n' + '\n'.join(author_string)

outf = os.popen('xclip -selection c', 'w')
content = outf.write(to_copy)
outf.close()


