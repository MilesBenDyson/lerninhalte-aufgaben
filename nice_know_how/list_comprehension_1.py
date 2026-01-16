geraete = [
    {"name": "Router", "status": "ok"},
    {"name": "Laptop", "status": "offline"},
    {"name": "Server", "status": "ok"},
    {"name": "Drucker", "status": "fehler"}
]

problem_namen = []

# for schleife
for dict_ in geraete:
    if dict_['status'] != 'ok':
        problem_namen.append(dict_['name'])

print(problem_namen)

# list comprehension
problem_namen_2 = [dict_['name'] for dict_ in geraete if dict_['status'] != 'ok']


print(problem_namen_2)
ok_liste = []
# weiter Übungen

#for-Schleife
for dict_ in geraete:
    if dict_['status'] == 'ok':
        ok_liste.append(dict_)
#list_comprehension
ok_liste_2 = [dict_ for dict_ in geraete if dict_['status'] == 'ok']

print(ok_liste,"\n",ok_liste_2)

#nächste Übung
upper_list_ok = []

for dict_ in geraete:
    if dict_['status'] == 'ok':
        upper_list_ok.append(f"{dict_['name'].upper()} (OK)")
upper_list_ok_2 = [f"{dict_['name']} (OK)".upper() for dict_ in geraete if dict_['status'] == 'ok']

print(upper_list_ok)
print(upper_list_ok_2)

