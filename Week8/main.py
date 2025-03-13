crews = [['Mal', 'Washburne', 'Zoe'], ['Han', 'Chewie'], ['Kirk', 'Spock', 'McCoy']]
for position, crew in enumerate(crews):
        print('=' * 20)
        print(f'Crew #{position + 1}')
        print('=' * 20)
        for member in crew:
              print(member)