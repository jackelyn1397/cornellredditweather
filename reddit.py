import praw

reddit = praw.Reddit(client_id='2uVEdfikHOMbpA',
                     client_secret='rxJn-oQkARMg1Z_B355-r6tkfqY',
                     password='5306testacc',
                     user_agent='testscript',
                     username='coldbrewfan')

print(reddit.user.me())
