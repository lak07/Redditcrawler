import praw
import threading
stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there',
              'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do',
              'its', 'yours', 'such', 'into',
              'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
              'themselves', 'until', 'below','I',
              'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself',
              'this', 'down', 'should', 'our', 'their','while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she',
              'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have','in', 'will', 'on',
              'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now',
              'under', 'he',  'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i',
              'after', 'few','whom', 't', 'being', 'if', 'theirs','my', 'against', 'a', 'by', 'doing', 'it', 'how',
              'further', 'was','here', 'than'] #Stop Words
reddit = praw.Reddit(client_id='w9j4aR6VL9KDUA',
                     client_secret='hHqjghmpUmuK20tYG1y6F2Jsjzc',
                     password='',
                     user_agent='testscript by /u/laxay_7',
                     username='laxay_7') # reddit instance
subredit_url = input("Please enter subredit url")
subredit_url_final = subredit_url.split('/')
subredit_url_final = subredit_url_final[len(subredit_url_final)-1]
print(subredit_url_final)
submission_list=[]

    # print(submission.title)
    # for top_level_comment in submission.comments:
    #    print(top_level_comment.score)


def getKeywords(submission):
    comments_dic = {}
    print(submission.title)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if comment.score in comments_dic.keys():
            comments_dic[comment.score].append(comment.body)
        else:
            comments_dic[comment.score]= [comment.body]
        #print(comment.score,comment.body)
    sorted_x = sorted(comments_dic.items(), key=lambda x: x[0])
    sorted_x.reverse()
    sorted_x=sorted_x[:10]
    top_comments = []
    for comments in sorted_x:
        for each_comments in comments[1]:
            top_comments.append(each_comments)
    top_comments = top_comments[:10]
    keywords = []
    for comment in top_comments:
        for word in comment.split():
            keywords.append(word)
    keywordensity = dict((x, keywords.count(x)) for x in set(keywords))
    # print(keywordensity)
    sorted_keywords = sorted(keywordensity.items(), key=lambda x: x[1])
    sorted_keywords.reverse()
    top_keywords = [x for x in sorted_keywords if x[0] not in stop_words]
    print(top_keywords[:10])


for submission in reddit.subreddit(subredit_url_final).top(limit=10): #limit specifies limit
    threading._start_new_thread(getKeywords,(submission))
