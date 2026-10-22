S1 = {2,3,1}
S2 = {'b','a','c'}
S3 = list(zip(S1,S2))
print (S3,"\n")


list1 = [10,20,30,40]
list2 = [100,200,300,400]

for x, y in zip(list1, list2):
    print(x,y)


stocks = ['reliance','infosys','tcs']
prices = [2175, 1127, 2750]

new_Dict = {stocks: prices for stocks,
            prices in zip (stocks, prices)}


print('\n'.format(new_Dict))








