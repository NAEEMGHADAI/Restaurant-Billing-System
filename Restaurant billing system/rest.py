import xlrd
from tkinter import *
import xlwt
import datetime
import xlsxwriter
from xlwt import Workbook
root = Tk()


def closeWin():
    root.destroy()


def printtext():

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

    now = datetime.datetime.now()
    sheet1.write(1, 0, 'DATE')
    sheet1.write(3, 0, 'ITEM')
    sheet1.write(1, 4, 'BILL NO.')
    sheet1.write(3, 4, 'RATE')
    sheet1.write(3, 5, 'AMOUNT')
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'
    sheet1.write(1, 2, datetime.datetime.now(), date_format)
    sheet1.write(10, 2, 'GST @18%')
    sheet1.write(11, 2, 'GRAND TOTAL')

    global entry_num
    string = entry_num.get()
    print(string)

    L = string.split(',')
    print("\nThe values of input are", L)
    total_price = 0
    nr = 4
    pr = 4

    for i in L:
        if i == 'chkspp':
            price = 762
            total_price = total_price+price
            name = 'chicken supreme party pack'
            sheet1.write(nr, 0, name)
            sheet1.write(pr, 5, price)
            sheet1.write(pr, 4, price)
        elif i == 'chkfp':
            price = 552
            total_price = total_price+price
            name = 'chicken family pack'
            sheet1.write(nr, 0, name)
            sheet1.write(pr, 4, price)
            sheet1.write(pr, 5, price)
        elif i == 'muttspp':
            price = 867
            total_price = total_price+price
            name = 'mutton supreme party pack'
            sheet1.write(nr, 0, name)
            sheet1.write(pr, 5, price)
            sheet1.write(pr, 4, price)
        elif i == 'muttfp':
            price = 629
            total_price = total_price+price
            name = 'mutton family pack'
            sheet1.write(nr, 0, name)
            sheet1.write(pr, 5, price)
            sheet1.write(pr, 4, price)
        elif i == 'nveggp':
            price = 619
            total_price = total_price+price
            name = 'non-veg gift pack'
            sheet1.write(nr, 0, name)
            sheet1.write(pr, 5, price)
            sheet1.write(pr, 4, price)
        elif i == 'vegfp':
            price = 505
            total_price = total_price+price
            name = 'veg family pack'
            sheet1.write(nr, 0, name)
            sheet1.write(pr, 4, price)
            sheet1.write(pr, 5, price)
        elif i == 'vegsp':
            price = 705
            total_price = total_price+price
            name = 'veg supreme pack'
            sheet1.write(nr, 0, name)
            sheet1.write(pr, 5, price)
            sheet1.write(pr, 4, price)

        nr = nr + 1
        pr = pr + 1

    total_gst = total_price * (0.18)
    total_price = total_price + total_gst

    sheet1.write(10, 5, total_gst)
    sheet1.write(11, 5, total_price)

    # Program to extract a particular row value

    '''loc = ("bill")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(1)

    sheet.cell_value(0, 0)

    print(sheet.row_values(1))
    print(sheet.row_values(2))
    print(sheet.row_values(3))
    print(sheet.row_values(4))
    print(sheet.row_values(5))
    print(sheet.row_values(6))
    print(sheet.row_values(7))
    print(sheet.row_values(8))
    print(sheet.row_values(9))
    print(sheet.row_values(10))
    print(sheet.row_values(11))
    print(sheet.row_values(12))
'''
    output.delete(0.0, END)
    output.insert(END, str(total_price))

    output_gst.delete(0.0, END)
    output_gst.insert(END, str(total_gst))
    wb.save('bill.xls')


root.minsize(500, 500)
no_dishes = Label(root, text="Enter the dishes")
no_dishes.grid(row=0, column=0)

entry_num = Entry(root, width=40)
entry_num.grid(row=0, column=2)

button_entry = Button(root, text='SUBMIT', command=printtext)
button_entry.grid(row=1, column=3)

# output tax, 6
lab_output_tax = Label(root, text="Total Bill")
lab_output_tax.grid(row=5, column=0)

output = Text(root, width=42, height=1, wrap=WORD)
output.grid(row=5, column=1, columnspan=4)

# output taxable, 7
lab_output_taxable = Label(root, text="Total gst")
lab_output_taxable.grid(row=6, column=0)

output_gst = Text(root, width=42, height=1, wrap=WORD)
output_gst.grid(row=6, column=1, columnspan=4)


# make sure to define the reset button
def reset():
    lab_output_tax = Button(root, text="")
    lab_output_taxable = Button(root, text="")
    no_dishes = Button(root, text="")
    return


ButtonReset = Button(root, text="Reset", command=reset)
ButtonReset.grid(row=7, column=1)


quit = Button(text="Quit", command=closeWin)
quit.grid(row=7, column=4)

root.mainloop()
