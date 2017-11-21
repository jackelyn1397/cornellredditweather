import praw
import time

def getDocuments(): # returns a dictionary of documents
    reddit = praw.Reddit(client_id='2uVEdfikHOMbpA',
                         client_secret='rxJn-oQkARMg1Z_B355-r6tkfqY',
                         password='5306testacc',
                         user_agent='testscript',
                         username='coldbrewfan')
    reddit.read_only = True
    subreddit = reddit.subreddit('cornell')

    postDict = {}
    documents = {'documents':[dict() for x in range(100)]}
    count = 0

    for submission in subreddit.top(limit=100):
        documents['documents'][count]['id'] = count
        documents['documents'][count]['language'] = 'en'
        documents['documents'][count]['text'] = submission.title
        documents['documents'][count]['date'] = time.strftime('%Y%m%d', time.localtime(submission.created))
        #print(submission.title)  # Output: the submission's title
    #    print(submission.score)  # Output: the submission's score
    #    print(time.strftime('%Y%m%d', time.localtime(submission.created)))
        count += 1


    return documents
