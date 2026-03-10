# to read excell sheet.

import xlrd
path= r'C:\Users\KIIT\PycharmProjects\selenium_project\selenium_training\training\register.xlsx'



def excel_data():
    workbook = xlrd.open_workbook(path)
    print(workbook)

    # openthe worksheet
    worksheet = workbook.sheet_by_name("Sheet1")

    # convert sheet object to the generator object
    rows = worksheet.get_rows()
    # print(rows)

    header = next(rows)
    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value

    # print(ele[0].value,ele[1].value)

    return d




