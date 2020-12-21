enter_text = open('input.txt', 'r', encoding='utf8')
separation_enter = []
output_list = []
couple = dict()
for j in enter_text:
    j = j.split()
    for p in range(len(j)):
        separation_enter.append(j[p])
for i in separation_enter:
    if i not in couple:
        couple[i] = 0
        output_list.append(couple[i])
    else:
        couple[i] += 1
        output_list.append(couple[i])
print(*output_list)
