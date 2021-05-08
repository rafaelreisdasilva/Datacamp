import matplotlib.pyplot as plt
import math

import datetime as datetime
#year = [1950,1970,1990,2010]
#pop = [2.519,3.692,5.263,6.972]
#line graph
#plt.plot(year,pop)
#plt.show()

#scatter plot
#plt.scatter(year,pop)
#plt.show()


def funcao(valor):
    return 2*math.pow(valor,3)-5


print(funcao(4))
print(funcao(2))

for n in range(10):
    if n%2:
        print(n)

print(datetime.datetime(1970, 1, 1).strftime('%Y-%d-%B'))
