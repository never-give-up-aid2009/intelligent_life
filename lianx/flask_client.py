from flask import Flask, send_file
import sys


app = Flask(__name__)

@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/list2_1_1')
# def topic_release(username):
#     #发表分享内容
#     return send_file('templates/list2_1_1.html')
def topic_release():
    #发表分享内容
    return send_file('templates/list2_1_1.html')


@app.route('/list3_1_1')
# def topics_detail(username, t_id):
#     #互动内容详情
#     return send_file('templates/list3_1_1.html.html')
def topics_detail():
    #互动内容详情
    return send_file('templates/list3_1_1.html')

@app.route('/cart')
def cart_detail():
    #互动内容详情
    return send_file('templates/cart.html')

@app.route('/forget')
def forget_detail():
    #互动内容详情
    return send_file('templates/forget.html')

@app.route('/info')
def info_detail():
    #互动内容详情
    return send_file('templates/info.html')

@app.route('/list1_1_1')
def list1_1_1_detail():
    #互动内容详情
    return send_file('templates/list1_1_1.html')

@app.route('/list1_1_2')
def list1_1_2_detail():
    #互动内容详情
    return send_file('templates/list1_1_2.html')

@app.route('/list1_1_3')
def list1_1_3_detail():
    #互动内容详情
    return send_file('templates/list1_1_3.html')

@app.route('/login')
def login_detail():
    #互动内容详情
    return send_file('templates/login.html')

@app.route('/order')
def order_detail():
    #互动内容详情
    return send_file('templates/order.html')

@app.route('/place_order')
def place_order_detail():
    #互动内容详情
    return send_file('templates/place_order.html')

@app.route('/register')
def register_detail():
    #互动内容详情
    return send_file('templates/register.html')

@app.route('/reset')
def reset_detail():
    #互动内容详情
    return send_file('templates/reset.html')

@app.route('/search')
def search_detail():
    #互动内容详情
    return send_file('templates/search.html')

@app.route('/site')
def site_detail():
    #互动内容详情
    return send_file('templates/site.html')


if __name__ == '__main__':
    app.run(debug=True)

