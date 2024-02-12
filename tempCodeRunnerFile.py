import os
import random

def make_commit(days: int):
    if days < 1:
        # git push
        return os.system('git push')
    else:
        dates = f'{days} days ago'
        
        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')
            
        os.system('git add data.txt')
        os.system('git commit --date="'+dates+'" -m "Commit {days} days ago"') 
        return days * make_commit(days-1)

def make_random_commits():
    total_commits = 700
    while total_commits <= 2500:
        days = random.randint(1, 30)  # Randomly select days between 1 and 30
        total_commits += days
        if total_commits > 2500:
            break
        commit_with_days(days)

def commit_with_days(days: int):
    dates = f'{days} days ago'
    
    with open('data.txt', 'a') as file:
        file.write(f'{dates}\n')
        
    os.system('git add data.txt')
    os.system('git commit --date="'+dates+'" -m "Commit {days} days ago"')

# Random commits
make_random_commits()

# Start the commit with the specified days
make_commit(500)
