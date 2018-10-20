def countIdent(s):
    ident = 0
    for c in s:
        if c == " ":
            ident += 1
        else:
            return ident
    return ident

def main():
    counter = 0
    default_indent = 0
    last_key_word = 0
    with open("manFile") as f:
        for line in f:
            counter += 1
            if default_indent == 0:
                if countIdent(line) == 0 and line.startswith("NAME"):
                    last_key_word = 1
                    print("NAME")
                if last_key_word == 1:
                    print(line)
                    default_indent = countIdent(line)
    print(default_indent)

if __name__ == "__main__":
    main()





# lastKeyWord
# 1 = NAME