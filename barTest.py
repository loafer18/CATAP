import matplotlib.pyplot as plt

'''
费用最大的10个品牌分别是：
TopTenBrandCostList = ['KENNAMETAL', 'ESK', 'SANDVIK', 'TUBTIMSIAM', 'TOP PAC', 'ATLAS', 'INTERNATIONAL PRODUCTS CORPORATION', 'WATANA BHAND', 'LEE&STEEL', 'ESK']
他们各自消耗的费用为：
TenBrandCostOrder = [5351235.63, 5188461.87, 4637461.55, 2113558.31, 1447424.98, 1075427.08, 931500.26, 895391.24, 699556.2, 666409.39]
'''
width = 0.39
TopTenBrandCostList = ['KENNAMETAL', 'ESK', 'SANDVIK', 'TUBTIMSIAM', 'TOP PAC', 'ATLAS', 'INTERNATIONAL PRODUCTS CORPORATION', 'WATANA BHAND', 'LEE&STEEL', 'ESK']
TenBrandCostOrder = [5351235.63, 5188461.87, 4637461.55, 2113558.31, 1447424.98, 1075427.08, 931500.26, 895391.24, 699556.2, 666409.39]

# 由于个别品牌名称过长，需要 cut 掉一部分
TopTenBrandCostList[6] = 'INTERNATIONAL'
TopTenBrandCostList[7] = 'WATANA'
plt.bar(TopTenBrandCostList,TenBrandCostOrder, width)
plt.show()
