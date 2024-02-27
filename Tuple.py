def check(name, key):
    a = name.count(100)
    if 100 in name:
        print(f'{key} got {a} 100')
    else:
        print(f'Winter score is {name}')


data = {
    'Winter': (90, 100, 98),
    'Summer': (74, 89, 85),
    'Spring': (75, 96, 88),
    'Paul': (100, 100, 100)}
Rounded = [round(sum(data['Winter'])/3, 2),
           round(sum(data['Summer'])/3, 2),
           round(sum(data['Spring'])/3, 2),
           round(sum(data['Paul'])/3, 2)]
last = {'Winter': Rounded[0], 'Summer': Rounded[1],
        'Spring': Rounded[2], 'Paul': Rounded[3]}
print(f'Winter: {Rounded[0]}')
print(f'Summer: {Rounded[1]}')
print(f'Spring: {Rounded[2]}')
print(f'Paul: {Rounded[3]}')
check(data['Winter'], 'Winter')
check(data['Summer'], 'Summer')
check(data['Spring'], 'Spring')
check(data['Paul'], 'Paul')
print(f'{max(last, key=last.get)} got the highest score!')
print(f'{min(last, key=last.get)} got the lowest score!')

# def check(name, key):
#     count_100 = name.count(100)
#     if 100 in name:
#         print(f'{key} got {count_100} 100')
#     else:
#         print(f'{key} score is {name}')
# data = {
#     'Winter': (90, 100, 98),
#     'Summer': (74, 89, 85),
#     'Spring': (75, 96, 88),
#     'Paul': (100, 100, 100)
# }
# averages = {key: round(sum(values) / len(values), 2) for key, values in data.items()}
# print('\n'.join([f'{key}: {average}' for key, average in averages.items()]))
# for season, scores in data.items():
#     check(scores, season)
# highest_score = max(averages, key=averages.get)
# lowest_score = min(averages, key=averages.get)
# print(f'{highest_score} got the highest score!')
# print(f'{lowest_score} got the lowest score!')
