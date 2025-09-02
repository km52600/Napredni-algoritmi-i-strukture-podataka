names = ["Ana", "Petar", "Ana", "Lucija", "Vanja", "Pavao", "Lucija"]
def reverse_sort(names: list) -> list:
    return sorted(names, reverse=True)


names_desc: list = reverse_sort(names)
print(names_desc)

selected_names = reverse_sort(names)[0:-1]
print(selected_names)

unique_selected_names = set(selected_names)
print(unique_selected_names)

pass_names: list = []

for name in unique_selected_names:
    pass_names.append(name + " - pass")

print(pass_names)