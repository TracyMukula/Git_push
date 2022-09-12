#defining the decimal varibles
dict_ones= {
    '0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five',
    '6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','11':'Eleven',
    '12': 'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen',
    '17':'Seventeen','18':'Eighteen','19':'Nineteen'}
dict_tens = {
    '0':'','1':'Ten','2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty',
    '6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
dict_thousand= {'0':'','1':'Thousand','2': 'Hundred', '3':'Million','4':'Billion'}
n = int(input("Enter number: "))
x = str(n)
y = int(len(x))
for y in x:
    y=1
    print(dict_ones[x[0]])
    y =+1
    if 9 < int[x[0:2]] < 20 :
        print(dict_ones[x[0:2]], end = ' ')
    else:
        print(dict_tens[x[0]], dict_ones[x[1]], end =' ')
    
    
    if len(x) == 2:
       # print(dict_tens[x[]])
    
        print(dict_ones[x[0]], dict_thousand['2'], end = ' ')
    if 9 < int(x[1:3]) < 20 :
        print(dict_ones[x[1:3]], end = ' ')
    else:
        print(dict_tens[x[1]], dict_ones[x[2]])
    #if len(x) == 2:
       # print(dict_tens[x[]])
    
#elif len(x) <=6:
    print(dict_ones[x[0]], dict_thousand['1'], end ='')
    print(dict_ones[x[3]], dict_thousand['2'])
    if 9 < int(x[3:5]) < 20:
        print(dict_ones[x[3:5]], dict_thousand['1'])
    else:
            print(dict_tens[x[4]], dict_ones[x[5]], dict_thousand['1'])
#elif len(x) <= 9:
    print(dict_ones[x[6]], dict_thousand['2'])
    if x[7:9] == range(10,20):
            print(dict_ones[range(10, 20)], dict_thousand['3'])
    else:
            print(dict_tens[x[7]], dict_ones[x[8]], dict_thousand['3'])
#elif len(x) ==10:
    print(dict_ones[x[0]], dict_thousand['4'], )
#if x[1:10] is None:
    print (dict_thousand['0'])
#else:
    #print("Number entered is too long")