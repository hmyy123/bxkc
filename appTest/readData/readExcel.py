import xlrd, os


class ExcelUtil():
    def __init__(self, sheetName="Sheet1"):
        Dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(Dir_path, "readData", "user.xls")
        excelPath = file_path
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            # print(self.keys)
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                k = dict(zip(self.keys,values))
                r.append(k)
                j += 1
            return r

    def value_re(self, vaule):
        try:
            if vaule % 1 == 0:
                vaule = int(vaule)
        except:
            vaule = vaule
        return vaule

if __name__ == "__main__":
    sheetName = "login"
    data = ExcelUtil(sheetName)
    print(*(data.dict_data()))
