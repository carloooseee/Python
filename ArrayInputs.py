#List
location = ['Davao', 'Cebu', 'Iloilo', 'Bohol', 'Boracay']
food = []

# Start of program
print('\nEnter their delicacy: ')
for i in range(len(location)):
    food.append(input('Enter: '))

# Result
print('''
==========================================
Travel Destination                Delicacy
==========================================''')
food.reverse()
x = len(location)
while x > 0:
    print(f'{location[x-1]:<34}{food[x-1]}')
    x -= 1