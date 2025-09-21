unit_used = 350 #หน่อวย
rate_per_unit = 4.5 #บาทต่อนหน่วย
service_charge = 50 #บาท

 #1คำนวณค่าไฟฟ้า
electricity_cost = unit_used * rate_per_unit

#2คำนวณรวมทั้งหมด
total = electricity_cost + service_charge

print("Electricity Bill Calculator")
print(f"Unit used       : {unit_used}")
print(f"Rate per unit   : {rate_per_unit} THB")
print(f"Service charge  : {service_charge} THB")
print(f"Total cost      : {int(total)} THB")
print()
print(f"Summary: used {unit_used} unit equals {int(total)} THB")