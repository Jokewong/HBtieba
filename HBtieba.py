
# coding: utf-8

# #抓取湖北大学贴吧的帖子标题，发帖人，回复数 

# In[206]:


import requests
from bs4 import BeautifulSoup


# In[210]:


def getnews(newsurl):
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    news_detail = []
    for news in soup.select('.t_con'):
        result = {}
        result['title'] = news.select('.j_th_tit ')[0].text.strip()
        result['author'] = news.select('.frs-author-name')[0].text
        result['reply'] = news.select('.threadlist_rep_num')[0].text
        news_detail.append(result)
    return news_detail


# In[217]:


news_total = []
url = 'http://tieba.baidu.com/f?kw=%E6%B9%96%E5%8C%97%E5%A4%A7%E5%AD%A6&ie=utf-8&pn={}'
for i in range(0,10):
    newsurl = url.format(i * 50)
    newsary = getnews(newsurl)
    news_total.extend(newsary)


# In[220]:


import pandas
df = pandas.DataFrame(news_total)


# In[229]:


df.to_excel('HBtieba.xlsx')

