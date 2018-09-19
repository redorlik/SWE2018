

def rle_encoder(txt):
    """ RLE encoder modetager en streng og returner en liste
        af gentagne bogstaver bliver erstattet med bogstavet og
         antallet af gentagelser

         "bbbkkk" bliver "b3k3"
         """
    if not txt:
        return ''
    c = txt[0]
    i = 1
    res = []
    for x in txt[1:]:
        if x == c:
            i += 1
        else:
            res.append(f'{c}{i}')
            i = 1
            c = x
    res.append(f'{c}{i}')
    return res

def rle_decoder(inp):
    res = []

    for kode in inp:
        c = kode[0]
        i = 1
        count = 0
        while i<len(kode) and kode[i].isdigit():
            count = count*10 + int(kode[i])
            i += 1
        res.append(c*count)

    return ''.join(res)

if __name__ == "__main__":
    import sys
    args = sys.argv
    print(args)
    if len(args)==3:
        dat = args[2]
    elif len(args)==2:
        dat = sys.stdin.read()
    else:
        print("Error")
        exit(0)
    if args[1]=='-d':
        print(rle_decoder(dat))
    else:
        print(rle_encoder(dat))
