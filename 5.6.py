file = open('FF_abbreviated.txt')                          # 'file' object

data = {}                                                  # initialize an empty dict

for lines in file:                                         # for each str in list of strings
    lines = lines.rstrip()                                 # a new str line w/o newline at end
    item = lines.split()                                   # split str line in comma
    year = item[0]                                         # 1st item of split line: 19260701
    year_split = year[0:4]                                 # slice the year varible: 1926
    value = float(item[1])                                 # float the value varible: 0.09
    if year_split in data:                                 # bool, True
        data[year_split] = data[year_split] + value        # add 1 to value
    else:
        data[year_split] = value
file.close()

sort = sorted(data, key=data.get)                          # list, ['1926', '1928', '1927']

for key in sort:                                           # for each key line in sort
    print(key, data[key])
