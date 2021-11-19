days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus', 'szeptember', 'október',
         'november', 'december']

months_and_days = []
for i in range(12):
    """print(month[i], days_in_month[i])"""
    months_and_days.append(month[i])
    months_and_days.append(days_in_month[i])
print(months_and_days)

szamok = [34, 97, 12, -15, 35, 10]
maxi = szamok[0]
index = 0
for i in range(len(szamok)):
    if szamok[i] > maxi:
        maxi = szamok[i]
        index = i
print(maxi, index)

mini = szamok[0]
for i in range(len(szamok)):
    if szamok[i] < mini:
        mini = szamok[i]
        index = i
print(mini, index)
