import sys
def main():
    with open(sys.argv[1]) as f:
        num = int( f.readline().strip())
        for _ in range(num):
            line = f.readline().strip()
            opens = []
            isValid = True
            open_char = "([{<"
            close_char = ")]}>"
            for i in range(len(line)):
                if not isValid:
                    break
                o_index = open_char.find(line[i])
                c_index = close_char.find(line[i])
                if o_index > -1:
                    opens.append(o_index)
                elif c_index > -1:
                    if c_index != opens.pop():
                        isValid = False
            if isValid:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
