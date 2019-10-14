import json



#剔除掉不用的信息
def parse():
    name = "学校.json"
    with open(name, 'r', encoding='UTF-8') as data:
        schools = json.load(data)

        new = []
        for o in schools:
            school = {}
            school['name'] = o['name']
            school['province'] = o['province']
            school['city'] = o['city']
            school['area'] = o['area']

            if school['name'].find('教学')!=-1:
                continue

            new.append(school)

        with open('handle-' + name, 'w', encoding='utf-8') as file:
            file.write(json.dumps(new, ensure_ascii=False))
        print('完成！')

# def fit():
#     import xlrd
#     import os
#     # 打开excel文件,获取工作簿对象
#     root = os.getcwd()
#     wb = xlrd.open_workbook(filename="2019.xlsx")  # 打开文件
#     sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
#     cols = sheet1.col_values(0)  # 获取列内容
#
#     name = "handle-学校.json"
#     with open(name, 'r', encoding='UTF-8') as data:
#         schools = json.load(data)
#
#
#
#         new ={}
#         for o in schools:
#             school = {}
#             school['name'] = o['name']
#             school['province'] = o['province']
#             school['city'] = o['city']
#             school['area'] = o['area']
#             new['name']=school
#
#         new2=[]
#         for c in cols:
#             if c in new:
#                 new2.append(new[c])
#             else:
#                 print("没有{}".format(c))
#
#
#         with open('handle-' + name, 'w', encoding='utf-8') as file:
#             file.write(json.dumps(new2, ensure_ascii=False))
#         print('完成！')





parse()
