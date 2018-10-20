def countIdent(s):
    ident = 0
    for c in s:
        if c == " ":
            ident += 1
        else:
            return ident
    return ident

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

    print(list)



if __name__ == "__main__":
    main()





# lastKeyWord
# 1 = NAME
