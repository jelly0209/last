import tweepy
import MeCab
from wordcloud import WordCloud, STOPWORDS # 単語の頻出頻度の可視化
import streamlit as st
import os

# 取得した各種キーを格納-----------------------------------------------------
os.chdir('/Users/gakuto/desktop')
CONSUMER_KEY = "eiCDcdjft2UHyF0emsupSgxSR"
CONSUMER_SECRET = "sYOpWa9WcsamAjcPvR3YF1KRWVaVSkjNuy9BCatxCR4enPVhB8"
ACCESS_TOKEN = "1386962991069892609-6CYjiPkBrIQEokgc616F9gbtq56jdO"
ACCESS_TOKEN_SECRET = "s0HNtO1wT7eBMNFfExojWn2DP7v9B6lr3QVafxwLZcstW"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

st.title('Twitterから見る性格診断')

url = st.text_input('@の後ろを入力してください:')

if st.button('テキストマイニングを実行') :
 def main():

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

 api = tweepy.API(auth)
 tweets = api.user_timeline( screen_name = url ,count=200,page=1)
 num = 1
 text = ''
 for tweet in tweets:
    text += tweet.text

 j = " ".join([i.split("\t")[ 0] for i in text.split("\n")])# \n改行除去 \t空白除去

 add_STOPWORDS = [ "https" ,"nasutokai" , "chistoryoflife","t","co"]#表示させないキーワードを追加する
 for word in add_STOPWORDS:
    STOPWORDS.add(word)

 tagger = MeCab.Tagger()
 tagger.parse('')
 node = tagger.parseToNode(j)

 word_list = []
 while node:
    word_type = node.feature.split(',')[0]
    word_surf = node.surface.split(',')[0]
    if word_type == '名詞' and word_surf not in add_STOPWORDS:
        word_list.append(node.surface)
    node = node.next

 word_chain = ' '.join(word_list)
 word_cloud = WordCloud(
    background_color="white",
    width=900,
    height=500,
    max_words = 4000,
    font_path = "/Library/Fonts//ヒラギノ丸ゴ ProN W4.ttc" 
 )

 word_cloud.generate(word_chain)
 word_cloud.to_file('sample.jpg')
 img = 'sample.jpg'
 st.image(img)

