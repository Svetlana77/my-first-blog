lottery = [3, 42, 12, 19, 30, 59]
print(len(lottery))
print(lottery)
print(lottery[0])
del lottery[0]
print(lottery)
participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print(participant['name'])
del participant['favorite_numbers']
participant 
{'country': 'Poland', 'favorite_language': 'Python', 'name': 'Ola'}
participant['country'] = 'Germany'
participant
{'country': 'Germany', 'favorite_language': 'Python', 'name': 'Ola'}