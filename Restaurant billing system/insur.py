# GUI example
import tkinter as tk


def calc_income_tax():
    income = float(entry_income.get())
    section_80c = float(entry_sec_80c.get())
    health_insurance = float(entry_health_ins.get())
    housing_loan = float(entry_house_loan.get())

    max_housing_loan = 0.3 * income

    section_80c = 150000 if section_80c > 150000 else section_80c
    health_insurance = 30000 if health_insurance > 30000 else health_insurance
    housing_loan = max_housing_loan if housing_loan > max_housing_loan else housing_loan

    income -= section_80c
    income -= health_insurance
    income -= housing_loan

    if income <= 500000:
        percent = 0
    elif income > 500000 and income <= 750000:
        percent = 0.10
    elif income > 750000 and income <= 1000000:
        percent = 0.15
    elif income > 1000000 and income <= 2000000:
        percent = 0.20
    else:
        percent = 30

    income_tax = income * percent

    output_tax.delete(0.0, tk.END)
    output_tax.insert(tk.END, str(income_tax))

    output_taxable.delete(0.0, tk.END)
    output_taxable.insert(tk.END, str(income))


root = tk.Tk()
root.minsize(500, 500)

# income, 1
lab_income = tk.Label(root, text="Enter your income")
lab_income.grid(row=0, column=0)

entry_income = tk.Entry(root, width=20)
entry_income.grid(row=0, column=2)

# section 80 c, 2
lab_sec_80c = tk.Label(root, text="Enter 80c investment")
lab_sec_80c.grid(row=1, column=0)

entry_sec_80c = tk.Entry(root, width=20)
entry_sec_80c.grid(row=1, column=2)

# health insurance, 3
lab_health_ins = tk.Label(root, text="Enter health insurance")
lab_health_ins.grid(row=2, column=0)

entry_health_ins = tk.Entry(root, width=20)
entry_health_ins.grid(row=2, column=2)

# housing loan, 4
lab_house_loan = tk.Label(root, text="Enter housing loan")
lab_house_loan.grid(row=3, column=0)

entry_house_loan = tk.Entry(root, width=20)
entry_house_loan.grid(row=3, column=2)

# submit, 5
btn_submit = tk.Button(root, text="Submit", command=calc_income_tax)
btn_submit.grid(row=4, column=2)

# output tax, 6
lab_output_tax = tk.Label(root, text="Income tax is")
lab_output_tax.grid(row=5, column=0)

output_tax = tk.Text(root, width=42, height=1, wrap=tk.WORD)
output_tax.grid(row=5, column=1, columnspan=4)

# output taxable, 7
lab_output_taxable = tk.Label(root, text="Taxable income is")
lab_output_taxable.grid(row=6, column=0)

output_taxable = tk.Text(root, width=42, height=1, wrap=tk.WORD)
output_taxable.grid(row=6, column=1, columnspan=4)

root.mainloop()
