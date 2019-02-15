#-- coding: utf-8 -- 
# Author: EthanLiu@2019Feb13
# local path: C:\Users\Ethan.L\Desktop\Data_Analyze\CATAP
# file name: AIIM Master Report - Vallen - 2019Feb.xls

import numpy as np
import matplotlib.pyplot as plt

TopFifteenBrand = ['SANDVIK', "King' Stella", '3M', 'DEERGE', 'Umbrella', 'KOKEN', 'ISCAR', 'TRIPLE Q', 'VALSPA', 'OIL SEAL', 'DYNA-M', 'UNIAIR', 'HONEYWELL SAFETY PRODUCTS AUST P/L', 'ZB', 'Lakeland']
BrandTopFifteen =  [905, 615, 580, 409, 245, 240, 188, 176, 158, 120, 117, 115, 115, 109, 107]
TotalFifteenBrandCost = [4637442, 157, 333731, 3891, 1722, 2182, 201804, 3402, 69303, 53, 1378, 6, 81, 16, 156]
men_std = (2,3,4,1,2,2,3,4,1,2,2,3,4,1,2)
women_std = (3,5,2,3,3,3,5,2,3,3,3,5,2,3,3)

ind = np.arange(len(TopFifteenBrand)) # the x locations for the groups
#width = 0.35 # the width of the bars

#fig, ax = plt.subplots()
#rects1 = ax.bar(ind-width/2, BrandTopFifteen, width, yerr= men_std, color = 'SkyBlue', label='Top 15 Brand Times')
#rects2 = ax.bar(ind+width/2, TotalFifteenBrandCost, width, yerr=women_std, color ='IndianRed', label='Each Brand Cost')

# Add some text for labels, title and custom x-axis tick labels, etc.
'''
ax.set_ylabel('Scores')
ax.set_title('Top 15 Brands Consumption Overview')
ax.set_xticks(ind)
ax.set_xticklabels(TopFifteenBrand)
ax.legend()
'''
plt.plot(men_std, women_std, 'b')
#plt.bar(TopFifteenBrand, TotalFifteenBrandCost, 'b.')

'''
def autolabel(rects, xpos = 'center'):
     ~~~Attach a text lable above each bar in *rects*, displaying its height.
    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    ~~~
    xpos = xpos.lower() # normalize the case of the parameter
    ha = {'center':'center', 'right':'left', 'left':'right'}
    offset = {'center' : 0.5, 'right':0.57, 'left':0.43} # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        #ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height, '{}'.format(height), ha = ha[xpos], va = 'bottom')
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height, '{}'.format(height), ha=ha[xpos], va='bottom')
autolabel(rects1, 'left')
autolabel(rects2, 'right')
'''
    
plt.show()
