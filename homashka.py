with open('files.csv', mode='r') as f1:
    lst = f1.read().split('\n') # все файлы
    types = {} #Количество файлов каждого типа
    print(lst)
    for i in lst:
        k = i[i.index('.'):i.index(',')]
        if k in types:
            types[k] += 1
        else:
            types[k] = 1
    print('Количество файлов каждого типа:')
    for i in types:
        print("'", i, '\': ', types[i], sep='')
    print('\n', 'Самые большие файлы:', sep='')
    top = sorted(lst, key=lambda x: int(x.split(',')[1]), reverse=True)[:10] #топ 10 самых больших файлов
    top = sorted(top, key=lambda x: x.split(',')[0]) # тот же топ, отсортированный по алфавиту
    for i in top:
        k = i.split(',')[:2]
        print(*k,' Кбайт')
    print('\nсписок презентаций ограниченного доступа, которые изменялись в 2012 году:')
    m = [] #список презентаций ограниченного доступа, которые изменялись в 2012 году
    for i in lst:
        k = i.split(',')
        if k[-1] == 'ограничен' and k[-2].split('.')[-1] == '2012' and k[2] == 'презентация':
            m.append(k[0])
    print('\n'.join(sorted(m)), '\n\nсписок видео размером больше 100 Мбайт, созданных во второй половине 2011 года:',
          sep='')
    u = [] #список видео размером больше 100 Мбайт, созданных во второй половине 2011 года
    for i in lst:
        size = i.split(',')[1] # размер файла
        yoc = i.split(',')[3].split('.')[1]  # Year Of Create
        moc = i.split(',')[3].split('.')[2]  # Month Of Create
        if int(size) > 102400 and int(yoc) == 11 and int(moc) >= 7 and i.split(',')[2] =='видео':
            u.append(i)
    u.sort(key=lambda x:x[1],reverse=True)

    print('\n'.join([(' : '.join(i.split(',')[:2]))+ ' Кбайт' for i in u]))
