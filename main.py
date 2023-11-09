print("Tocca fa a stecca?! Boni tutti rega ce penso io.")
bill = float(input("Quant'è 'rdanno? €'"))
tip = int(input("Quanta percentuale de mancia? 0, 10,12 15? o dimme te "))
people = int(input("In quanti se stecca? "))
tip_as_percent = tip /100
tot_tip_amount = bill * tip_as_percent
tot_bill = bill + tot_tip_amount
bill_per_person = tot_bill / people
# final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"So €{final_amount} a capoccia ")
