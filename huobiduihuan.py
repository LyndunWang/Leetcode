''' 最大货币兑换：获取最多种类的货币'''
'''最小货币兑换：获取最少的货币种类，也就是换成最不值钱的港币就可以了'''

mt = ['GBP','USD','CNY','HKD']
dh = ['MIN','MAX']
rt  = ''
#判断输入合法性
a = input().split()
for i in range(4):
    if int(a[i]) <= 0:
        print('ERROR')

if a[4] not in mt:
    print('ERROR')

if a[5] not in dh:
    print('ERROR')

Y2G = int(a[0]) * int(a[1]) * int(a[2]) #一个美元可以兑换的港币
M2G = int(a[1]) * int(a[2])
R2G = int(a[2])
#将当前的输入的货币均转换为港币
if a[4] == 'GBP':
    temp = int(a[3]) * Y2G
elif a[4] == 'USD':
    temp  = int(a[3]) * M2G
elif a[4] == 'CNY':
    temp = int(a[3]) * R2G
else:
    temp = int(a[3]) #港币的情况
#计算两种兑换方式
if a[5] == 'MIN':
    rt += (str(temp) + '' + 'HKD')
else:
    if(temp/Y2G > 0):
        rt +=(str(temp//Y2G)+ ' ' + 'GBP' + ' ')
        temp = temp%Y2G
    if(temp/M2G > 0):
        rt += (str(temp//M2G) + ' ' + 'USD' + ' ')
        temp = temp%M2G
    if(temp/R2G > 0):
        rt += (str(temp//R2G) + ' ' + 'CNY' + ' ')
        temp = temp%R2G
    if(temp > 0):
        rt += (str(temp) + ' ' + 'HKD' + ' ')

print(rt)

