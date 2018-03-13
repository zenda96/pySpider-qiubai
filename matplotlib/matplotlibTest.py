#!/usr/bin/env python3
# import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
customers = ['a','b','c']
customers_index = range(len(customers))
sale_amounts =[11,22,33]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(customers_index,sale_amounts,align='center',color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index,customers,rotation=0,fontsize='small')
plt.xlabel('customer')
plt.ylabel('sale')
plt.title('bar')
plt.savefig('bar.png',dpi=400,bbox_inches='tight')
plt.show()

# x=np.linspace(-np.pi,np.pi,256,endpoint=True)  
# C,S=np.cos(x),np.sin(x)  
# plt.plot(x,C)  
# plt.plot(x,S)  
# plt.show()