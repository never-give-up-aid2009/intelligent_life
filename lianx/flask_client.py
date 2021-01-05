from flask import Flask, send_file
import sys


app = Flask(__name__)

@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/list2_1_1')
def topic_release(username):
    #发表分享内容
    return send_file('templates/list2_1_1.html.html')


@app.route('/list3_1_1')
def topics_detail(username, t_id):
    #互动内容详情
    return send_file('templates/list3_1_1.html.html')

if __name__ == '__main__':
    app.run(debug=True)

