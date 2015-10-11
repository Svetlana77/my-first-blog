participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print(participant['name'])
del participant['favorite_numbers']
participant = {'country': 'Poland', 'favorite_language': 'Python', 'name': 'Ola'}
participant['country'] = 'Germany'
participant = {'country': 'Germany', 'favorite_language': 'Python', 'name': 'Ola'}
print(participant)