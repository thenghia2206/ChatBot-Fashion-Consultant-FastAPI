import pandas as pd
import math

def CBR(data_input : str):
    data = pd.read_excel("CBR\output (4).xlsx", sheet_name = "Sheet_name_1")
    data1 = data
    new_arr = pd.DataFrame(data1).to_numpy()
    data2  = pd.read_excel('CBR\Final.xlsx')
    data2 = data2.drop(['Unnamed: 0'], axis=1)
    arr_input = [int(x) for x in data_input.split()]
    # print(arr_input)
    thisdict = dict()
    case = 0
    for arr in new_arr:
        dis = 0
        case += 1
        for x in range(len(arr)):
            dis += math.sqrt(pow(arr[x]- arr_input[x], 2))
        dis /= 24 
        thisdict[case] = dis
    sorteddict = sorted(thisdict.items(), key=lambda x:x[1])
    result = []

    for i in sorteddict:
        if i[1] == 0:
            result.append(i[0])
            break
    if len(result) == 0:
        result.append(sorteddict[0][0])
    list1 = []
    for x in result:
        new_clo =""
        for i in data2['Loại quần áo nên mặc'][x]:
            if i !="[" and i!=']' and i!='\'':
                new_clo+=i
        if new_clo != "":
            list1.append(new_clo)
    return set(list1)

