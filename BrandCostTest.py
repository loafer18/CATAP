import xlrd
import xlwt
import matplotlib.pyplot as plt

CleanData = 'small.xlsx'  # 后期改动：增加待处理提示，用户自己输入文件名
CATMonthlywb = xlrd.open_workbook(CleanData)
CATMonthlyws = CATMonthlywb.sheet_by_name('Sheet2')

nrows = CATMonthlyws.nrows

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
print ('将挑选费用前 3 名的品牌进行分析演示。')

# BrandList =[8] ['PSE SAFETY AND INDUSTRIAL SERVICES', 'YY CABLE TIES', 'AIK LEE', '3M', 'NORTON', 'HENKEL', 'ELVEX', 'Hagemeyer']
# 下面需要将 8 个品牌的依次费用加总，放入BrandCost[8]列表，并挑出数值最大的3个数值。
# returnNum 做为一个临时值，存储每一行的金额，并汇总到 returnNum， 后续再 append 到费用列表 BrandCost=[966]
BrandCost = []
returnNum = 0
for i in BrandList:
	for row in range(1,nrows):
		if CATMonthlyws.cell(row,8).value == i:
			returnNum += CATMonthlyws.cell(row,4).value
	BrandCost.append(returnNum)
	returnNum = 0
print(BrandCost)
# BrandCost = [21.0, 5.0, 5.0, 2.8, 3.6, 73.0, 4.0, 36.0]
# 以上程序运行结果与手工验证数据一致，程序通过。 2019/2/16

CATMonthlywb = xlrd.open_workbook(CleanData)
CATMonthlyws = CATMonthlywb.sheet_by_name('Sheet2')

# for row in range(1,CATMonthlyws.nrows):
	# rowValues = CATMonthlyws.row_values(row) # 该行 整行的值
	
print('下面需要将品牌名称统一大写，转存数据。')
	#下面代码错误，cell 单元格的值不可以直接赋值，只能用心的值用write方法写入单元格并保存表格，再次读取后即为新值
	# CATMonthlyws.cell(row,8).value = (CATMonthlyws.cell(row,8).value.upper())
	
	#print (CATMonthlyws.cell(row,8).value)

wbWrite = xlwt.Workbook()
wsWrite = wbWrite.add_sheet('Sheet2', cell_overwrite_ok = True)

# 这里再次读取显示还是有小写品牌，应该是文件没有写入全大写的内容，
# 所以文件内容实质还是大小写都存在，最后显示的还是老的数据
# 需要写入一次之后，再次读取，应该就会全部是大写的，现将。等健身回来再搞
# 2019/2/16 16:49PM

