
import xlrd
from tkinter import *
import xlwt
import datetime
import xlsxwriter
from xlwt import Workbook
root = Tk()

#Title
root.title("Restaurant Bill Calculator")

#Quit Function
def closeWin():
    root.destroy()

#---------------------WHOLE MENU AND CALCULATION SECTION----------------
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

    #Getting the dishes with , form
    global entry_num
    string = entry_num.get()
    print(string)

    #Converting it into list for seprating them
    L = string.split(',')
    print("\nThe values of input are", L)
    total_price = 0
    nr = 4
    pr = 4

    #MENU
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

    #Calculating GST
    total_gst = total_price * (0.18)
    total_price = total_price + total_gst

    sheet1.write(nr, 5, total_gst)
    sheet1.write(nr+1, 5, total_price)
    sheet1.write(nr, 2, 'GST @18%')
    sheet1.write(nr+1, 2, 'GRAND TOTAL')

    output.delete(0.0, END)
    output.insert(END, str(total_price))

    output_gst.delete(0.0, END)
    output_gst.insert(END, str(total_gst))

    #THIS WHOLE SECTION IS USED FOR NAMING THE EXCEL SHEET ACCORDING TO OUR RUN TIME 
    def get_var_value(filename="varstore.dat"):
        with open(filename, "a+") as f:
            f.seek(0)
            val = int(f.read() or 0) + 1
            f.seek(0)
            f.truncate()
            f.write(str(val))
            return val

    your_counter = get_var_value()
    sheet1.write(1, 5, '{}'.format(your_counter))
    print("This script has been run {} times.".format(your_counter))

    wb.save('{}.xlsx'.format(your_counter))
    
    

#MINIMUM SIZE OF OUTPUT SCREEN
root.minsize(500, 500)


#Title on output window screen
label_info = Label(root, font=('arial', 25, 'bold'),
                   text="Restaurant Bill Calculator", fg="steel blue", bd=10, anchor='w')
label_info.grid(row=0, column=3)

#-------------Section For Taking Input---------

#Making object of stringvar()
no_dishes_1 = StringVar()

#Input
no_dishes = Label(root, text="Enter the dishes", font=('arial', 16, 'bold'))
no_dishes.grid(row=1, column=1)
entry_num = Entry(root, width=40,  textvariable=no_dishes_1,
                  font=('arial', 16, 'bold'))
entry_num.grid(row=1, column=3)

#Input Button 
button_entry = Button(root, text='SUBMIT',
                      command=printtext, font=('arial', 16, 'bold'))
button_entry.grid(row=2, column=4)

#------------Section for Showing Total Bill----------

lab_output_tax = Label(root, text="Total Bill", font=('arial', 16, 'bold'))
lab_output_tax.grid(row=6, column=1)

#printing total bill 
output = Text(root, width=42, height=1, wrap=WORD, font=('arial', 16, 'bold'))
output.grid(row=6, column=2, columnspan=4)

#--------------Section For Showing Gst--------------------

lab_output_taxable = Label(root, text="Total gst", font=('arial', 16, 'bold'))
lab_output_taxable.grid(row=7, column=1)

#Print Total Gst
output_gst = Text(root, width=42, height=1, wrap=WORD,
                  font=('arial', 16, 'bold'))
output_gst.grid(row=7, column=2, columnspan=4)


# define the reset function
def reset():
    no_dishes_1.set(' ')

#Reset Button
ButtonReset = Button(root, text="Reset", command=reset,
                     font=('arial', 16, 'bold'))
ButtonReset.grid(row=8, column=2)

#Quit Button
quit = Button(text="Quit", command=closeWin, font=('arial', 16, 'bold'))
quit.grid(row=8, column=4)

#Looping 
root.mainloop()
