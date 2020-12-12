import random
import openpyxl
print("Enter the title of the names column to be made:")
name = input()
name_list = []

wb = openpyxl.load_workbook("input_data.xlsx")

sheet = wb.active

for i in range(7,84):
    name_list.append(sheet['C'+str(i)].value)

print(name_list)

wb_out = openpyxl.Workbook()

sheet_out = wb_out.active

sheet_out['A1'].value = name

for i in range(2,79):
    sheet_out['A'+str(i)].value = sheet['C'+str(i+7)].value

wb_out.save("output_data.xlsx")
