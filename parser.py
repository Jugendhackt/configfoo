#!/usr/bin/env python3
def countIdent(s):
    ident = 0
    for c in s:
        if c == " ":
            ident += 1
        else:
            return ident
    return ident

def write(d, file):
    f = open("tags", "w")
    f.write("!_TAG_FILE_FORMAT\t2\t/extended format; --format=1 will not append ;\" to lines/\n")
    f.write("!_TAG_FILE_SORTED\t1\t/0=unsorted, 1=sorted, 2=foldcase/\n")
    f.write("!_TAG_OUTPUT_MODE\tu-ctags /u-ctags or e-ctags/\n")
    f.write("!_TAG_PROGRAM_AUTHOR\tConfig foo Team\t//\n")
    f.write("!_TAG_PROGRAM_NAME\tconfig foo\n")
    for x in d:
        f.write(x[2] + "\t" + file + "\t" + x[2] + "\n") # "\ts\ttitle:" + file + "\n")


def main():
    previos = ""
    previosText = ""
    optionSection = False
    list = []
#    list.append((0, "p", ""))
    listCounter = 0
    counter = 0
    default_indent = 0
    last_key_word = 0
    with open("manFile") as f:
        for line in f:
            counter += 1
            if default_indent == 0:
                if countIdent(line) == 0 and line.startswith("NAME"):
                    last_key_word = 1
                if last_key_word == 1:
                    default_indent = countIdent(line)
                print("test")
                continue

            if line in ('\n', '\r\n'):
                continue
            if countIdent(line) == 0:
                print("section")
                optionSection = False
                continue
            indent = (countIdent(line) / default_indent)
            if indent < 1:
                print("half indent")
                continue
            if indent == 1:
                previosText = line.strip()
#                if optionSection == True:
#                    if list[-1][2].startswith(line.strip()):
#                        print("double")
#                    list.append((counter, "o", line.strip()))
                continue
            if indent > 1:
                if previosText == "":
                    continue
#                if list[-1][2].startswith(line.strip()):
#                    print("double")
                if '=,' in previosText:
                    options = previosText.split(",")
                    if len(options) > 3:
                        print("larger than 3??")
                        continue
                    for x in options:
                        list.append((counter - 1, "o", x.strip().strip("=")))
                    previosText = ""
                    continue
                insert_text = previosText.strip().split(" ")[0]
                list.append((counter - 1, "o", insert_text.strip("=")))
                optionSection = True
                previosText = ""

    write(list, "test")



if __name__ == "__main__":
    main()





# lastKeyWord
# 1 = NAME
