import openpyxl

work_book = openpyxl.load_workbook("input_data.xlsx")

first_sheet = work_book.active


# checking condition for marks greater than 8.5
def check_condition(num):
    if int(num) > 8.5:
        return True
    return False


workbook_out = openpyxl.Workbook()
sheet_out = workbook_out.active
sheet_out['A1'].value = "Student Name"
sheet_out['B1'].value = "Percentage"

j=2
for i in range(7,85):

#writing values in the appropriate block
    if check_condition(first_sheet['D'+str(i)].value):
        sheet_out['A'+str(j)].value = first_sheet['C'+str(i)].value
        point = (float(first_sheet['D'+str(i)].value)/10)*100
        sheet_out['B'+str(j)].value = point
        j += 1

workbook_out.save("output_data_2.xlsx")