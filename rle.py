

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
    return ''.join(res)
