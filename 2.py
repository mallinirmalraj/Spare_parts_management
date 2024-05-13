import sqlite3

list_data = "part_number, part_name, received_quantity, machine_name"
conn = sqlite3.connect('spare_part_maintenance.db')
c = conn.cursor()
pop = c.execute(f'SELECT {list_data} FROM In_request_form').fetchall()
list_data = []
for row in [a[0] for a in pop]:
    pop1 = c.execute(f'SELECT Quantity FROM new_spare_in where VPN=?',(row,)).fetchone()
    list_data.append(pop1)
conn.close()
print(list_data)
for i in range(len(pop)):
    pop[i] = pop[i] + list_data[i]
print(pop)
# result_dict = {}
# for row in pop:
#     part_number, part_name, received_quantity, machine_name, current_stock = row
#     key = (part_number, part_name, machine_name, current_stock)
#     if key in result_dict:
#         result_dict[key] += int(received_quantity)
#     else:
#         result_dict[key] = int(received_quantity)
# #
# result_list = [(part_number, part_name, machine_name, str(current_stock), str(received_quantity)) for (part_number, part_name, machine_name, current_stock), received_quantity in result_dict.items()]
# print(sorted(result_list))
