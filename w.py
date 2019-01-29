import xlwt
x=xlwt.Workbook()
x1=x.add_sheet('a1')
x1.write(0,1)
x.save("E:\s.xls")
