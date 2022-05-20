def main():
    x = read_file(input().strip())
    d = make_key(x[0], x[1])
    if not d:
        print("Invalid code")
    else:
        for i in range(2, len(x)):
            s = ""
            for e in x[i].split():
                if x[0] == "T2M":
                    for c in e:
                        if c in d:
                            s += d[c] + " "
                        else:
                            s = "Invalid : " + x[i]
                            break
                else:
                    if e in d:
                        s += d[e]
                    else:
                        s = "Invalid : " + x[i]
                        break
            print(s.strip())


def read_file(file):
    f = open(file, "r")
    x = []
    for e in f:
        x.append(e.strip())
    f.close()
    return x


def make_key(c, k):
    d = {}
    for i in range(len(k.strip("[").replace("]", "[").split("[")) // 2):
        if c == "T2M":
            d[k.strip("[").replace("]", "[").split("[")[2 * i]] = (
                k.strip("[").replace("]", "[").split("[")[2 * i + 1]
            )
        elif c == "M2T":
            d[k.strip("[").replace("]", "[").split("[")[2 * i + 1]] = (
                k.strip("[").replace("]", "[").split("[")[2 * i]
            )
        else:
            return False
    return d


main()