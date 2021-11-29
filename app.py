from hashlib import new
from flask import Flask, request
from flask import render_template
from main import search
from collections import defaultdict
app = Flask(__name__)

lang_dict = {}

@app.route('/search', methods=['POST', 'GET'])
def index():
    lang = []
    query = request.form.get("query")
    is_en = request.form.get("English")
    is_zh = request.form.get("Chinese")
    is_ru = request.form.get("Russian")
    is_ja = request.form.get("Japanese")
    is_ka = request.form.get("Korean")
    print("query: ", query)
    if is_en!=None:
        lang.append('en')
    if is_zh!=None:
        lang.append('zh-CN')
    if is_ru!=None:
        lang.append('ru')
    if is_ja!=None:
        lang.append('ja')
    if is_ka!=None:
        lang.append('ko')
    res, news_res_List = search(query, lang)
    return render_template("res_list.html", res_1=res[0] if len(res)>0 else "", res_2=res[1] if len(res)>1 else "",\
                           res_3=res[2] if len(res)>2 else "", res_4=res[3] if len(res)>4 else "", \
                           res_5=res[4] if len(res)>4 else "", \
                           news_1=news_res_List[0] if len(news_res_List) > 0 else defaultdict(str), news_2=news_res_List[1] if len(news_res_List) > 1 else defaultdict(str), \
                           news_3=news_res_List[2] if len(news_res_List) > 2 else defaultdict(str), news_4=news_res_List[3] if len(news_res_List) > 3 else defaultdict(str), \
                           news_5=news_res_List[4] if len(news_res_List) > 4 else defaultdict(str))

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()