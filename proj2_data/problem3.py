import sys
def main():
    with open(sys.argv[1]) as f:
        num = int( f.readline().strip())
        r = []
        for i in range(num):
            line = f.readline().strip().split()
            r.append((i,int(line[0]),int(line[1])))
        start = 0
        energy = 0
        done = False
        while not done:
            curr_r = r.pop(0)
            energy += curr_r[1]
            r.append(curr_r)
            energy -= curr_r[2]
            if energy < 0:
                start = curr_r[0]+1
                energy = 0
            elif r[0][0] == start:
                done = True
        print(start)
if __name__ == "__main__":
    main()
