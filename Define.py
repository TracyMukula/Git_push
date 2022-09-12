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
y = len(str(n))
def start(self):
    print(dict_ones[x[-3]], dict_thousand['2'], end = ' ')
    if 9 < int(x[-2:0]) < 20:
        print(dict_ones[x[-2:0]], end =' ')
    else:
        print(dict_tens[x[-2]], dict_ones[x[-1]])
def intermediate(self):
    print(dict_ones[x[-6]], dict_thousand['2'], end =' ')
    if 9 < int(x[-5:-3]) < 20:
        print(dict_ones[x[-5:-3]], dict_thousand['1'], end =' ')
    else:
        print(dict_tens[x[-5]], dict_ones[x[-4]], end = ' ')
    self.start()
def end(self):
    print(dict_ones[x[-9]], dict_thousand['2'], end = ' ')
    if 9 < int(x[-8:-6]) < 20:
        print(dict_ones[x[-8:-6]], dict_thousand['3'])
    else:
        print(dict_tens[x[-8]], dict_ones[x[-7]], dict_thousand['3'])
    self.intermediate()
    self.end()
    