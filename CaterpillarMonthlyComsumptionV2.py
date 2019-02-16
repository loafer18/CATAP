#-- coding: utf-8 -- 
# Author: EthanLiu@2019Feb2
# local path: C:\Users\Ethan.L\Desktop\Data_Analyze\CATAP
# file name: AIIM Master Report - Vallen - 2019Jan.xls
# 程序思路：
# 首先导入文件，获得数据源，读取数据。 
# 6 个关键字段： Site ID, Crib, Site Location, Price, Manufacturer and Keyword
# 首先 第一次数据汇总， 同Site下的所有销售汇总，得出各个Site的独立汇总数据并列柱状图显示
# 其次，用 Manufacturer 来做物料汇总，查看大厂商的产品使用量，比如 3M， SANDVIK等
# 最后，关键字， 几种关键字分几个类 归类。 看哪些属性的物料属于哪些类，并用饼图来显示，得到物料种类销售图
# 以上的柱状图及饼图绘制后，将相关的汇总数据写入新的汇总表，后续和其他月份汇总，得到全年数据。
import xlrd
import xlwt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties 
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=12)

data = 'AIIM Master Report - Vallen - 2019Jan.xls'  # 后期改动：增加待处理提示，用户自己输入文件名
CATMonthly = xlrd.open_workbook(data)
s = CATMonthly.sheet_by_name('Sheet1')

# print (s.cell(462,4).value) # 无价格的该单元，是一个 为“空” 的字符串？？？
# 数据清洗： 先判断是否有脏数据，如果有，建立新的工作表，将干净数据复制到新表中； 如果没有脏数据，反馈数据OK

for row in range(1,s.nrows):
	if type(s.cell(row,4).value) == str:
		print('Dirty Data Containing. Needs data sorting.')
		#print (row)  反馈第一行数据有问题的位置，在row 为 462 时
		#break 跳出循环
		break 
wbWrite = xlwt.Workbook()
wsWrite = wbWrite.add_sheet(u'Sheet2', cell_overwrite_ok=True)

# data forwarding
for row in range(0,s.nrows):
	rowValues = s.row_values(row)

	'''
	# 获取 表1 第一行的整行数据
	row0 = s.row_values(0)
	print(row0)
	'''

	# 由于发现有脏数据，现在进行数据转储， 2个循环迭代，将干净数据转至新的表格中。
	# 判断，如果是脏数据，则这次的循环需要单独处理，该行数据单独一个个append到一个重置的 rowValues 例表中
	if row > 0 and type(s.cell(row,4).value) == str:
		print('The line data is dirty, cleaning.')
		rowValues = []
		# continue  
		# 2/6这里的输出有问题，程序直接把 相关单元格是字符串的整行都留空 而不是跳过，让下面的数据接上来，需要改
		# wsWrite.write(row,4,0) 目标cell不单独赋值，后面直接赋值在行列表的单一单元格
		for i in range(0,11):
			#rowValues = []
			rowValues.append(s.cell(row,i).value)	
			# 这里需要单独更新一下该行 rowValues 的值列表， 将该行每一个cell 都 append 进这个列表里
		rowValues[4] = 0
		rowValues[8] = rowValues[10] = 'NA'
		# 这里在 append 完的例表里 再修改需要的 3 列数据，改成可统计的数值及类型。 Bingo！！！
		print(rowValues)
		#print (s.cell(row,4).value)
		#s.cell(row,8).value = s.cell(row,10).value = 'NA'
	# 写入上面获取的整行数据到新的表2中
	for i in range(0,len(rowValues)):
		wsWrite.write(row,i,rowValues[i])

wbWrite.save('DataSorting.xls')

''' # 下面是显示已转储的数据，单独显示 Cell（462，4） 单元格的数值，确认是需要的数据及类型
wb = xlrd.open_workbook('DataSorting.xls')
ws = wb.sheet_by_name('Sheet2')
cell461 = ws.cell(462,4).value
print(cell461)
'''

# 下面就已清洗整理后的数据为分析样本。  2019/2/6

# 以下为数据读取后的数据获取测试单元
# python 按 row column 顺序获取数据， 计数由 0 开始
# print(s.cell(3,4).value) 

# 第一次数据分类 按 Site ID, 汇总同ID 的归并到该 ID 列表里， Price 最后加总。
# 判断各 Site 的数据范围： 方法，ID 相同，为同一个 Site， 不同，则建立新的 SiteID 列表
# 记录下每一个 site 的起始 和结束 行的行数， 为金额汇总做准备。
# 所有数据从excel的第2行开始， row = 1

CleanData = 'DataSorting.xls'  # 后期改动：增加待处理提示，用户自己输入文件名
CATMonthlywb = xlrd.open_workbook(CleanData)
CATMonthlyws = CATMonthlywb.sheet_by_name('Sheet2')
# 获取所有行数
nrows = CATMonthlyws.nrows  # nrows = 9928
print ('nrows equal: '+ str(nrows))
print ('数据行从第: 2 行到第: %s 行' %nrows )
print ('行号定位从第 1 行到 第 %s 行' %str(nrows-1))
# 获取所有 Site ID记录的全部清单
SiteIDList = []
for i in range(1,nrows-1):
	ID = s.cell(i,0).value
	SiteIDList.append(ID)
	i += 1
	#print (SiteIDList, len(SiteIDList))

	# 去重，获取SiteID清单
SiteList = []
for i in SiteIDList:
	if not i in SiteList:
		SiteList.append(i)
print('一共有 %s 个Site， 分别是： %s ' %(len(SiteList),SiteList))


'''
(below code block seems useless, to be delete)
for i in range (1, nrows-1):
	if s.cell(i,4).value == None:
		print (i)
		s.cell(i,4).value = 0.0
		i+=1
		print (s.cell(i,4).value) # s.cell(i,8).value, s.cell(i,10).value)
		#s.cell(i,8).value = s.cell(i,10).value = 'NA'
		#i += 1
	#print (s.cell(i,4).value, s.cell(i,8).value, s.cell(i,10).value)

(below codes seems useless, to be delete)
	CATMonthly = xlwt.open_Workbook(data)
	s = CATMonthly.sheet_by_name('Sheet1')
	s.write()
'''

# 取得每个Site的起始结束范围

SiteCost = 0
CostList = []

for j in range(len(SiteList)):  # j为SiteList范围（0~11），判断如果同一个Site就累加费用 
	for row in range (1, nrows): # 以行号起始 循环
		SiteID = CATMonthlyws.cell(row,0).value # 全表中逐个取SiteID值,第一个 SiteID 值： AK
		#print (SiteID)
		if SiteID == SiteList[j]:  # 如果 SiteID 取值 和 SiteList表里值一致，那就是同一个 Site
			SiteCost += CATMonthlyws.cell(row,4).value # 累加该 Site 的所有金额
			#print(SiteID, SiteList[j])
	CostList.append(round(SiteCost,2))
	SiteCost = 0
print('各个Site每月费用依次为： '+ str(CostList))
# 这里的 SiteCost/CostList 金额需要做保留2位有效小数/不保留小数位
# SiteList = ['AK', 'MF', 'EB', 'DEFAULT', 'WJ', 'NN', 'HB', 'WK', 'KG', 'HO', '66']
# CostList = [4412.77, 16953588.33, 67981.28, 63245.73, 371618.8, 11362.89, 45059.05, 15551913.5, 3406486.67, 3379.62, 34186.0]
# 以上程序运行结果与手工验证结果一致。 *****************************************************************

# 出图： 用饼图 1 显示各Site费用， 用饼图 2 综合显示各国家费用




# 下面进行 【品牌】、【金额】统计， 为了出图适度，挑选费用最高的10大品牌，汇总金额，并用柱状图显示。
# 出图： 费用前10大品牌， 金额，用柱状图显示。

# 数据结构: TotalList = [9927], BrandList = [966] 所有品牌列表。 BrandCost=[966]统计各品牌汇总金额
# TopTenCosts = [10]  是 BrandCost[966] 列表里数值最大的10个。
# TopTenPositions = [10] 根据 TopTenCosts 里的10个数值，找到 BrandList 里的品牌位置。
# TopTenBrands = [10str] 
# 
TotalList = []
BrandList = []
# 下面4行为建立所有第8列的品牌值列表 TotalList，有重复。
for row in range(1,nrows):
	TotalList.append(CATMonthlyws.cell(row,8).value)
print('品牌列一共有： '+str(len(TotalList))+ '个值')

for row in range(1,nrows):
	if CATMonthlyws.cell(row,8).value not in BrandList:
		BrandList.append(CATMonthlyws.cell(row,8).value)
print ('所有的品牌数量有: %d' %(len(BrandList)))
print (BrandList)
print ('将挑选费用前 10 名的品牌进行分析演示。')

# 下面需要将 966 个品牌的依次费用加总，放入BrandCost[966]列表，并挑出数值最大的10个数值。
# returnNum 做为一个临时值，存储每一行的金额，并汇总到 returnNum， 后续再 append 到费用列表 BrandCost=[966]
# 2019/2/16 问题，品牌大小写，程序分为2个品牌，分别计算金额，各品牌汇总金额＜手工品牌汇总金额
# 所以品牌汇总需忽略大小写， BrandList = [<966]  或者 金额汇总的时候，将大小写一致的品牌金额再汇总
BrandCost = []
returnNum = 0
#for row in range(1,nrows):
for i in BrandList:
	for row in range(1,nrows):
		if CATMonthlyws.cell(row,8).value == i: # 只要品牌名匹配的情况下
			returnNum += CATMonthlyws.cell(row,4).value  # 将该行金额汇总至returnNum
			#print (returnNum) 
	BrandCost.append(round(returnNum))
	returnNum = 0
print(BrandCost)
print(len(BrandCost))		



# 下面需要挑出数值最大的前 10 个数值，并记录下位置。
# list method of max, index
# maxCost 做为一个临时值，存储每一次的最大金额，并汇总到 TopTenCosts, 然后BrandCost列表里清除掉这个值
TopTenCosts = []
BrandPositions = []
maxCost = 0
maxCostPosition = 0
TopTenPositions = []
# 因为后续还需要在 BrandCost ？

for i in range(10):
	maxCost = max(BrandCost)
	maxCostPosition = BrandCost.index(maxCost)
	#print(maxCost)
	TopTenCosts.append(maxCost)
	TopTenPositions.append(maxCostPosition)
	BrandCost.remove(maxCost)
	maxCost = 0
	maxCostPosition = 0
print(TopTenCosts,TopTenPositions)
# TopTenCosts = [5351236, 5188462, 4637462, 2113558, 1447425, 1075427, 931500, 895391, 699556, 666409]
# TopTenPositions = [407, 890, 38, 236, 242, 119, 936, 133, 174, 890] 前10大费用品牌在费用总单中的位置
# 再在同期找出相对应的位置，再 append 到一个位置列表中去。


# 下面找品牌的部分先暂停，上面品牌大小写造成品牌金额汇总＜手工汇总金额
'''
returnBrand = 0
for num in TopTenPositions:
    returnBrand = BrandList[num]
    print (returnBrand)
'''





'''
# 下面的代码虽然简单 一个 set 函数就达到了去重的效果，但是获得的 BrandList 数据却是一个集合Set
BrandList = set(TotalList)
print ('Total item brands are: '+str(len(BrandList)))
print (type(BrandList))
'''


'''
# 按照位置列表，反差15个品牌信息  位置列表为 MaxBrandPositionList = [38,406,3...]
# 需要从之前的 966 个品牌列表里面按照上面的位置号找出对应的品牌并汇总到一个列表中 TopFifteenBrand = []
TopFifteenBrand = []
# 按 MaxBrandPositionList 位置清单，找到BrandList 中对应的品牌，作图
for i in MaxBrandPositionList:
	TopBrand = MaxBrandPositionList[i]
	TopFifteenBrand.append(TopBrand)
print(TopFifteenBrand)
'''




















# 关键字分析，今次使用 Safety，关键字记录里有 Safety/PPE，SAFETY EYE WEAR,Safety Clothes,Safety Shoes
# 所以有关安全产品的物料比较有一定的代表性。 
# 图表 则把所有有关 Safety 的物料汇总， SafetyItem, SafetyItemTimes =int, SafetyItemCosts=float
# 另外2类物品： Drill(s)和Tape(s), 这两类是比较常见的物料，有一定的代表性，希望他们和 Safety 类物料有可比性














































'''
WHcode=[]
SOHData=[]
SOOData=[]
for i in range(4, 65):
    if s.cell(i,4).value != 0 and s.cell(i,5).value != 0:
        WHcode.append(s.cell(i, 3).value)
        SOHData.append(s.cell(i, 4).value)
        SOOData.append(s.cell(i,5).value)        

#3. 显示数据图形，增加图例，增加x轴y轴及图表抬头，优化图像格式
plt.bar(WHcode, SOHData, label='SOH')
plt.bar(WHcode, SOOData, bottom=SOHData, label='SOO')
plt.xlabel('Warehouse Code')
plt.ylabel('RMB * 10M')
plt.legend(loc='upper right')
plt.title('Data Visualization: Vallen China Daily SOH/SOO (Jan 16 2018)')
plt.show()

#4. 变换显示数据，增加时间维度
#5. 增加互动， 点击某方块，图表上显示 数据类别 及 对应数值（单位：百万)

'''