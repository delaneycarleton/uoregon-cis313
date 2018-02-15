import sys
def main():
    ht = {}
    with open(sys.argv[1]) as f:
        line = f.readline().strip().split()
        x = int(line[0])
        y=int(line[1])
        line2 = f.readline().strip().split()
        line3 = f.readline().strip().split()
        for i in (range(x)):
            ht[line2[i]] = True
        contains = True
        for i in (range(y)):
            if line3[i] not in ht:
                contains = False 
                break
        if contains ==True:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()
