# вводишь коэфиценты уравнения по порядку (от большей степени к меньшей)
# в ответе первое число ответ, остальные числа полученный остаток из коэфицентов
a = [int(i) for i in input().split()]
m = []
k1 = a[0]
k2 = a[-1]
for i in range(1, 1+abs(k2)):
    if k2 // i == k2 / i:
        m.append(i)
        m.append(-i)
n = []
for i in range(1, 1+abs(k1)):
    if k1 // i == k1 / i:
        n.append(i)
        n.append(-i)
print(m,n)
mkt = []
for i in m:
    for j in n:
        c = k1
        ck = [k1]
        for q in range(len(a)-1):
            c = i/j * c + a[q+1]
            ck.append(c)
        if c == 0:
            for l in range(len(ck)):
                if ck[l] == int(ck[l]):
                    ck[l] = int(ck[l])
            yu = str(i)+'/'+str(j)
            if i/j == i//j:
                yu = i//j
                if yu not in mkt:
                    print(i // j,'\t',*ck)
                    mkt.append(yu)
            else:
                if yu not in mkt:
                    print(str(i)+'/'+str(j),'\t',*ck)
                    mkt.append(yu)