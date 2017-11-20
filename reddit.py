import praw
import time

reddit = praw.Reddit(client_id='2uVEdfikHOMbpA',
                     client_secret='rxJn-oQkARMg1Z_B355-r6tkfqY',
                     password='5306testacc',
                     user_agent='testscript',
                     username='coldbrewfan')
reddit.read_only = True
subreddit = reddit.subreddit('cornell')

postDict = {} 

for submission in subreddit.hot(limit=10):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created)))
