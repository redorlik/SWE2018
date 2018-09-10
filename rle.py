

def rle_encoder(txt):
    """ RLE encoder modetager en streng og returner en streng
        med så gentagne bogstaver bilver erstattet med bogstavet og
         antallet af gentagelser

         "bbbkkk" bliver "b3k3"
         """
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
    return ''.join(res)

def rle_decoder(inp):
    res = []
    i = 0
    while i<len(inp):
        c = inp[i]
        i += 1
        count = 0
        while i<len(inp) and inp[i].isdigit():
            count = count*10 + int(inp[i])
            i += 1
        res.append(c*count)

    return ''.join(res)

if __name__ == "__main__":
    import sys
    args = sys.argv
    print(args)
    if (args[1]=='-d'):
        print(rle_decoder(args[2]))
    else:
        print(rle_encoder(args[2]))
