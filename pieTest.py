import matplotlib.pyplot as plt
import matplotlib

Countries = ['Singapore', 'Thailand', 'China', 'India', 'Japan', 'Australia', 'Others']

size = [4412.77, 16953588.33, 496022.02, 18958400.17, 34186.0, 3379.62, 63245.73]

color = ['blue', 'springgreen', 'orangered','dodgerblue', 'indianred', 'greenyellow','black']
explode = [0.05, 0, 0, 0, 0, 0, 0]

patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=Countries, labeldistance=1.1, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
plt.axis('equal')
plt.legend()
plt.show()