direct_work = raw_input("Direct Work Cost = ")
dwc= int(direct_work)
subguard =  dwc * 0.02
general_conditions = dwc * 0.08
Subtotal_1 = dwc + subguard + general_conditions
CCIP = Subtotal_1 * 0.07
Subtotal_2 = Subtotal_1 + CCIP
Fee = Subtotal_2 * 0.05
Total_Cost = Subtotal_2 + Fee
print("Total Cost = ${:,.2f}".format(Total_Cost))
