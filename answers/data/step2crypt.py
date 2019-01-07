def encrypt(pt):
    ct = []
    for i, e in enumerate(pt):
        ct.append(e+str(i+1))
    ct = sorted(ct)
    return "".join(ct)
def decrypt(ct):
    print(ct)
    ct += ' '
    ans = [None for i in range(len(''.join([i for i in ct if not i.isdigit()])))]
    # print(ct)
    c_c = ''
    c_i = 0
    for i in ct:
        if i.isdigit():
            c_i = c_i*10 + int(i)
            # print(c_i)
        else:
            ans[c_i - 1] = c_c
            c_i = 0
            c_c = i
    return "".join(ans)

print(encrypt("Улица_Сухая,_дом_D,_квартира_D._Пароль_-_customcryptomasterhere"))