import os
import random

def make_random_commits():
    total_commits = 0
    while total_commits <= 1000:
        days = random.randint(1, 30)  # Randomly select days between 1 and 30
        total_commits += days
        if total_commits > 1000:
            break
        commit_with_days(days)

def commit_with_days(days: int):
    dates = f'{days} days ago'
    
    with open('data.txt', 'a') as file:
        file.write(f'{dates}\n')
        
    os.system('git add data.txt')
    os.system('git commit --date="'+dates+'" -m "Commit {days} days ago"')

make_random_commits()
