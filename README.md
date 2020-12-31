<h1 align='center'>项目开发文档</h1>
## 1.需求分析

### 1.1 产品概述

​       本软件是web服务器程序，主要是实现网上分享，领养，线上支付，线下配送。

### 1.2 功能概述

​	1. 用户通过浏览器访问 ，浏览器页面展现宠物店铺提供的各类宠物及宠物信息，并且可以对宠物进行分类，方便用户查找， 还可以分享宠物的精彩日常，交流心得。

​        2.用户可以对心仪的宠物进行收藏 ，也可以加入购物车，并且能即时生成订单，选择不同支付方式来完成支付。

​        3.本商城提供完善的用户信息管理，包括个人信息，订单查询等。

​		4.商城会对领养的人进行测试。达到合格方可领养。

​        4.提供完善的领养售后服务系统，使用户无后顾之忧。

​	   5.本软件登录采用短信验证，提高安全性

​	   7.页面维持用户的登录状态，便于用户切换页面，提高用户的体验

### 1.3 运行环境

|     项目     |                    内容                     |
| :----------: | :-----------------------------------------: |
|   操作系统   |                 ubantu18.04                 |
| python解释器 |                  python 3                   |
|  第三方插件  | Django 2.2.12 、 redis 4.0 、 jquery 1.11.3 |

## 2.功能要求

|      功能      |                           达成效果                           |
| :------------: | :----------------------------------------------------------: |
|      登录      | 老用户可以通过正确的账号密码来进入页面，或者通过手机号和手机验证码登录，验证码10分钟有效,并保持登录状态 |
|      注册      | 新用户可以通过账号密码注册，验证输入格式的正确性，并能通过手机验证码完成注册,验证码10分钟有效 |
|      注销      |      用户取消登录状态，删除浏览器的缓存，提高账户安全性      |
|  展现商品信息  |       用户可以浏览商品信息，包括图片，租赁价格，类型等       |
|    搜索商品    | 用户可以按照商品名称，类型查找商品，并能实现用户自定义排序方式展示， |
|      分享      |          用户可以在页面上分享领养心得，精彩的照片等          |
|     小贴士     |                 会不定时的分享一些注意事项。                 |
|    收藏商品    |            用户在浏览商品时，可实时将商品加入收藏            |
| 商品加入购物车 | 用户可以将商品加入购物车，可以计算购物车商品总价，便于后期结算，删除购物车商品，移入收藏 |
|    生成订单    |            用户提交收货地址，支付方式，可生成订单            |
|    在线支付    |            采用第三方支付平台支付宝，完成订单支付            |
| 订单查询/删除  | 对生成的订单进行查询及评价，展示下单时间，订单状态进行订单筛选。 |
|      评价      |                 用户可对领养的宠物进行点评，                 |
|    个人中心    |                     对个人信息展示和修改                     |
|      售后      |                 用户可对已支付的商品进行售后                 |

## 3.技术分析

本web应用利用django搭建，采用前后端分离，Ajax进行前后端数据交互，redis缓解高并发，token保持登录状态和验证身份。



## 4.系统分析

### 4.1 模块划分

| 序号 |          模块          |                       功能                       |
| :--: | :--------------------: | :----------------------------------------------: |
|  1   |      **用户模块**      |     1. 注册   2. 查看信息 3.更改信息 4.注销      |
|  2   | **stoken模块**（登录） |                      1.登录                      |
|  3   |        分享模块        |          1分享心得  2转发评论 3上传照片          |
|  4   |      **商品相关**      |      1. 首页  2. 商品详情页  3. 商品搜索页       |
|  5   |     **购物车模块**     | 1.查看购物车 2.修改购物车商品 3.添加商品到购物车 |
|  6   |      **订单模块**      |              1.查看订单 2.订单生成               |
|  7   |      **支付模块**      |                 1.对订单进行支付                 |
|  8   |      **评论模块**      |              1.发表评论 2.查看评论               |
|  9   |      **收藏模块**      |           1.收藏商品 2.移除收藏的商品            |
|  10  |      **售后模块**      |               1.发表售后 2查看售后               |



### 4.2 API接口

#### 4.2.1 注册

URL:127.0.0.1:8000/users

请求方式:post

请求数据:  json格式  {"username":'aaa',"password_1":'123456',"password_2":'123456',"phone":"13566668888","email":"123@163.com","code":8888}

返回数据:  json格式  {"code:200"}  

说明: username,token 需要保存在本地

| 异常码 |      说明      |
| :----: | :------------: |
| 10000  | 两次密码不一致 |
| 10001  |  用户名已占用  |
| 10002  | 手机验证码错误 |
| 10003  |    邮箱错误    |
| 10004  |   手机号错误   |



#### 4.2.2 登录

URL:127.0.0.1:8000/users/token

请求方式:post

请求数据:  json格式  {"username":'aaa',"password":'123456'}   /   {"phone":13588886666,"code":8888}

返回数据:  json格式  {"code:200","data":{"username":'aaa',"token":"xxx"}}  

说明: username,token 需要保存在本地

| 异常码 |       说明       |
| :----: | :--------------: |
| 20000  | 用户名或密码错误 |
| 20001  |  手机验证码错误  |



#### 4.2.3 查看个人信息

URL:127.0.0.1:8000/users

请求方式:get

请求数据:  无 

返回数据:  json格式  {"code:200","data":{"username":'aaa',"phone":"phone","13566668888","email":"123@163.com","avatar":"avatar/1.jpg","birthday":"1997-7-7"}}  

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

- js文件中需要设置服务器上图片路径  例: BASE_URL = "127.0.0.1:8000/media/"

| 异常码 |  说明  |
| :----: | :----: |
| 30000  | 未登录 |
|        |        |



#### 4.2.4 修改个人信息

URL:127.0.0.1:8000/users

请求方式:put

请求数据:  {"phone":13566668888,"email":"123@163.com","birthday":"1997-7-7","code":6666}}  

返回数据:  json格式  {"code:200"}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token
- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"
- 修改手机号需要旧手机短信验证

| 异常码 |      说明      |
| :----: | :------------: |
| 30000  |     未登录     |
| 20001  | 手机验证码错误 |
| 10003  |    邮箱错误    |
| 10004  |   手机号错误   |
| 10005  |    生日错误    |

#### 4.2.5 上传头像

URL: 127.0.0.1:8000/users/avatar

请求方式: post

请求数据: FormData()

返回数据:  json格式  {"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |  说明  |
| :----: | :----: |
| 30000  | 未登录 |
|        |        |

#### 4.2.6 更改密码

URL: 127.0.0.1:8000/users/password

请求方式: put

请求数据:  json格式 {"password_1":'123456',"password_2":'123456,"phone":1556666888,"code":5555}

返回数据:  json格式  {"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |      说明      |
| :----: | :------------: |
| 30000  |     未登录     |
| 20001  | 手机验证码错误 |

#### 4.2.7 主页轮播图

URL: 127.0.0.1:8000/slide

请求方式: get

请求数据:  无

返回数据:  json格式  {"code":200,"src": ['slide/1.jpg',  'slide/2.jpg']

说明: 

- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"
#### 4.2.8 搜索商品

URL: 127.0.0.1:8000/commodity?keyword=手机

请求方式: get

请求数据:  查询字符串

返回数据:  json格式  {"code":200,"data": [{"c_id":1,kind":"xx","image":"c_img/1.jpg",price":100,"age":3,"sex":m},{...}]

说明: 

- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"

| 异常码 |    说明    |
| :----: | :--------: |
| 30001  | 商品不存在 |

#### 4.2.9 商品详情

URL: 127.0.0.1:8000/commodity?c_id=1

请求方式: get

请求数据:  查询字符串

返回数据:  json格式  

{"code":200,"data": [{"c_id":1,kind":"xx","image":"c_img/1.jpg",price":100,"age":3,"sex":m,"created_time":"2020-10-10","updated_time":"2020-10-10","address":"xxx"},{...}]

说明: 

- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"

| 异常码 |    说明    |
| :----: | :--------: |
| 30001  | 商品不存在 |
|        |            |

#### 4.2.10 查看收藏

URL: 127.0.0.1:8000/collection

请求方式: get

请求数据:  无

返回数据:  json格式  {"code":200,"data": [{"c_id":1,kind":"xx","image":"c_img/1.jpg",price":100,"age":3,"sex":m,"created_time":"2020-10-10","updated_time":"2020-10-10","address":"xxx"},{...}]

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token
- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"

| 异常码 |  说明  |
| :----: | :----: |
| 30000  | 未登录 |
|        |        |

#### 4.2.11删除收藏中商品

URL: 127.0.0.1:8000/collection

请求方式: delete

请求数据:  {"c_id":1}

返回数据:  json格式  {"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token
- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 30001  | 商品不存在 |

#### 4.2.12 查看购物车

URL: 127.0.0.1:8000/shopping_cart

请求方式: get

请求数据: 无

返回数据:  json格式   {"code":200,"data": [{"c_id":1,kind":"xx","image":"c_img/1.jpg",price":100,"age":3,"sex":m,"created_time":"2020-10-10","updated_time":"2020-10-10","address":"xxx"},{...}]

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token
- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"

| 异常码 |  说明  |
| :----: | :----: |
| 30000  | 未登录 |

#### 4.2.13 加入购物车

URL: 127.0.0.1:8000/shopping_cart

请求方式: post

请求数据: json格式 {"c_id":1,"count":1}

返回数据:  json格式{"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 30001  | 商品不存在 |
| 30002  | 数量不正确 |


#### 4.2.14 修改购物车商品数量

URL: 127.0.0.1:8000/shopping_cart

请求方式: put

请求数据: json格式 {"c_id":1，"count":1}

返回数据:  json格式{"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 30001  | 商品不存在 |
| 30002  | 数量不正确 |



#### 4.2.15 删除购物车商品

URL: 127.0.0.1:8000/shopping_cart

请求方式: delete

请求数据: json格式 {"c_id":1}

返回数据:  json格式{"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 30001  | 商品不存在 |

#### 4.2.16 生成订单

URL: 127.0.0.1:8000/order

请求方式: post

请求数据:  json格式 {consignee":"小李","address":"西安","phone":15566666666,"data":[{"c_id":1,"count":1},{...}] }

返回数据:  json格式  {"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 30001  | 商品不存在 |
| 10004  | 手机号错误 |
| 30002  | 数量不正确 |
|        |            |

#### 4.2.17 查看订单

URL: 127.0.0.1:8000/order

请求方式: get

请求数据:  无

返回数据:  json格式  {"code":200,"order":[{"order_num":10000001,"create_time":"2020-10-10",status":"1","money":1000,consignee:"小李",data":[

 {"code":200,"data": [{"c_id":1,kind":"xx","image":"c_img/1.jpg",price":100,"age":3,"sex":m,"created_time":"2020-10-10","updated_time":"2020-10-10","address":"xxx"},{...}]

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token
- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"

| 异常码 |  说明  |
| :----: | :----: |
| 30000  | 未登录 |

#### 4.2.18 删除订单

URL: 127.0.0.1:8000/order

请求方式: delete

请求数据:  json格式  {"order_num":10000001}

返回数据:  json格式  {"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 40000  | 订单不存在 |

#### 4.2.19 查看售后

URL: 127.0.0.1:8000/after_sale

请求方式: get

请求数据:  

返回数据:   json格式  {"code":200,"data": [{"c_id":1,kind":"xx","image":"c_img/1.jpg",price":100,"age":3,"sex":m,"created_time":"2020-10-10","updated_time":"2020-10-10","address":"xxx"},{...}]

说明:

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token
- js文件中需要设置服务器上图片路径  例: BASE_URL = "http://127.0.0.1:8000/media/"

| 异常码 |  说明  |
| :----: | :----: |
| 30000  | 未登录 |

#### 4.2.20 添加售后

URL: 127.0.0.1:8000/after_sale

请求方式: post

请求数据:  :  json格式  {"c_id":1,"desc":"不喜欢","order_num":10000001}

返回数据:  json格式  {"code":200}

说明:

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 40000  | 订单不存在 |
| 30001  | 商品不存在 |

#### 4.2.21精彩分享

URL: 127.0.0.1:8000/mutual

请求方式: get

请求数据:  无

返回数据:  json格式   {"code":200,"data": {"username":'aaa',"avatar":"avatar/1.jpg",}  [{"c_id":1,kind":"xx","image":"c_img/1.jpg","sex":m,"created_time":"2020-10-10",},{...}]

说明:

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 40000  | 文章不存在 |

#### 4.2.22 照片分享，上传

URL: 127.0.0.1:8000/users/avatar

请求方式: post

请求数据: FormData()

返回数据:  json格式  {"code":200}

说明: 

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |  说明  |
| :----: | :----: |
| 30000  | 未登录 |

#### 4.2.23 添加评价

URL: 127.0.0.1:8000/comment"

请求方式: post

请求数据:  :  json格式  {"c_id":1,"content":"好好好"}

返回数据:  json格式  {"code":200}

说明:

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明     |
| :----: | :---------: |
| 50000  |  评价为空   |
| 30000  |   未登录    |
| 50001  | 字数超过500 |
| 30001  | 商品不存在  |

#### 4.2.24 查看评价

URL: 127.0.0.1:8000/comment"

请求方式: get

请求数据:  :  json格式  {"c_id":1}

返回数据:  json格式  {"code":200}

说明:

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 30001  | 商品不存在 |

#### 4.2.25 加入收藏

URL: 127.0.0.1:8000/collection"

请求方式: post

请求数据:  :  json格式  {"c_id":1}

返回数据:  json格式  {"code":200}

说明:

- 该请求需客户端在HTTP header 里添加 token,  格式如下：Authorization ： token

| 异常码 |    说明    |
| :----: | :--------: |
| 30000  |   未登录   |
| 30001  | 商品不存在 |



## 5.数据库设计

每个模型类需要继承**BaseMosel** 

导包如下：

```python
from db_base import BaseModel
```

### 5.1 用户模块

db_table= ‘‘user“

class_name：User

avartar :   upload_to='avatar'

|      字段      |   数据类型   | null | max_length |  备注  |
| :------------: | :----------: | :--: | :--------: | :----: |
| username(主键) |  CharField   |  /   |     30     | 用户名 |
|    password    |  CharField   |  /   |     32     |  密码  |
|     email      |  EmailField  |  /   |     /      |  邮箱  |
|     phone      | IntegerField |  /   |     11     | 手机号 |
|     avatar     |  imageField  | True |     /      |  头像  |
|    birthday    |  CharField   | True |     10     |  生日  |

### 5.2 分享互动

文章

db_table= ‘mutual“

class_name：Mutual

image :   upload_to=''fx_img"

 {"code":200,"data": {"username":'aaa',"avatar":"avatar/1.jpg",}  [{"c_id":1,kind":"xx","image":"c_img/1.jpg","sex":m,"created_time":"2020-10-10",},{...}]

|      字段      |   数据类型    | null | max_length |   备注   |
| :------------: | :-----------: | :--: | :--------: | :------: |
| username(主键) |   CharField   |  /   |     30     |  用户名  |
|      text      |   CharField   |  /   |     32     |   文章   |
|     image      |  imagelField  |  /   |     /      |   图片   |
|    comment     | IntegerField  |  /   |     11     | 评论数量 |
|     avatar     |  ImageField   | True |     /      |   头像   |
|   collection   | IntegerField  | True |     10     | 收藏数量 |
|  created_time  | DateTimeField | 150  |     /      | 创建时间 |

### 5.3 商品模块

**商品**

db_table= ‘‘commodity“

class_name：Commodity

image :   upload_to=''c_img"

|     字段     |      数据类型       | max_length | default | db_index | verbose_name |
| :----------: | :-----------------: | :--------: | :-----: | :------: | :----------: |
|     kind     |      CharField      |     20     |    /    |   True   |     种类     |
|     age      |    IntegerField     |     20     |    /    |    /     |     年龄     |
|     sex      |      CharField      |     20     |    /    |   True   |     性别     |
| created_time |    DateTimeField    |    150     |    /    |    /     |   创建时间   |
|    price     | DecimalField #(6,1) |     /      |    /    |    /     |     价格     |
| updated_time |    DateTimeField    |     /      |    /    |    /     |   修改时间   |
|   address    |      CharField      |     10     |    /    |          |     地址     |
|    c_img     |      FileField      |     /      |    /    |    /     |   宠物图片   |

 {"code":200,"data": [{"c_id":1,kind":"xx","image":"c_img/1.jpg",price":100,"age":3,"sex":m,"created_time":"2020-10-10","updated_time":"2020-10-10","address":"xxx"},{...}]



**商品详情页大图**

db_table="big_img"     

class_name:Big_img

big_image :   upload_to=''b_img"



|   字段    |       数据类型        | on_delete |  verbose_name  |
| :-------: | :-------------------: | :-------: | :------------: |
|   b_img   |       FileField       |     /     | 商品详情页大图 |
| commodity | ForeignKey(Commodity) |  CASCADE  |    商品编号    |



**轮播图**

db_table="slide"

class_name:Slide

image:   upload_to='slide'

|    字段     |   数据类型   | verbose_name |
| :---------: | :----------: | :----------: |
|  slide_img  |  FileField   |   图片路径   |
| display_seq | IntegerField |   显示顺序   |



### 5.4收藏模块

db_table="collection"

class_name:Collection

|   字段    |       数据类型        | on_delete | verbose_name |
| :-------: | :-------------------: | :-------: | :----------: |
|   user    |   ForeignKey(User)    |  CASCADE  |    用户名    |
| commodity | ForeignKey(Commodity) |  CASCADE  |   商品编号   |



### 5.5 购物车模块

db_table="shopping_cart"

class_name: ShoppingCart

注意： 生成订单后，彻底删除用户的购物车记录

|   字段    |       数据类型        | max_length | on_delete | verbose_name |
| :-------: | :-------------------: | :--------: | :-------: | :----------: |
|   user    |   ForeignKey(User)    |     /      |  CASCADE  |    用户名    |
| commodity | ForeignKey(Commodity) |     /      |  CASCADE  |   商品编号   |
|   count   |     IntegerField      |     /      |     /     |   商品数量   |



### 5.6 订单模块

**订单**

db_table="order"

class_name: Order

comms:  through='Order_Commodity'

|      字段       |          数据类型          | on_delete | max_length | default | verbose_name |
| :-------------: | :------------------------: | :-------: | :--------: | :-----: | :----------: |
| order_num(主键) |        IntegerField        |     /     |     /      |    /    |   订单编号   |
|    consignee    |         CharField          |     /     |     30     |    /    |    收货人    |
|     status      |         CharField          |     /     |     1      |   ’1‘   |     状态     |
|      user       |      ForeignKey(User)      |  CASCADE  |     /      |    /    |    用户名    |
|    commodity    | ManyToManyField(Commodity) |     /     |     /      |    /    |   商品编号   |
|     address     |         CharField          |     /     |     30     |    /    |   收货地址   |
|      phone      |         CharField          |     /     |     11     |    /    |     电话     |

status ： ”1“：待付款   ”2“:待评价  "3":已评价

注意：付款后/评价后，更改订单状态  付款后才能评价，订单删除是更改isDelete字段值为True



**订单商品关系表**

db_table = "order_commodity"

class_name : Order_Commodity

|   字段    |       数据类型        | on_delete | verbose_name | on_delete |
| :-------: | :-------------------: | :-------: | :----------: | :-------: |
|   count   |     IntegerField      |     /     |   商品数量   |     /     |
| commodity | ForeignKey(Commodity) |  CASCADE  |   商品编号   |  CASCADE  |
|   order   |   ForeignKey(Order)   |  CASCADE  |   订单编号   |  CASCADE  |



### 5.7 售后模块

db_table="after_sale"

class_name:AfterSale

image_info :   upload_to='after_sale'

|   字段    |       数据类型        | max_length | null | default | on_delete | verbose_name |
| :-------: | :-------------------: | :--------: | :--: | :-----: | :-------: | :----------: |
|   desc    |       CharField       |    500     |  /   |    /    |     /     |   问题描述   |
|  as_img   |       FileField       |     /      | True |    /    |     /     |     图片     |
|   user    |   ForeignKey(User)    |     /      |  /   |    /    |  CASCADE  |    用户名    |
| commodity | ForeignKey(Commodity) |     /      |  /   |    /    |  CASCADE  |   商品编号   |
|   order   |   ForeignKey(Order)   |     /      |  /   |    /    |  CASCADE  |   订单编号   |
|  status   |       CharField       |     30     |  /   | 处理中  |     /     |   处理进度   |



### 5.8 评论模块

db_table="comment"

class_name:Comment

|      字段      |       数据类型        | max_length | default | on_delete | verbose_name |
| :------------: | :-------------------: | :--------: | :-----: | :-------: | :----------: |
|    content     |       CharField       |    500     |    /    |     /     |     评论     |
|      user      |   ForeignKey(User)    |     /      |    /    |  CASCADE  |    用户名    |
|   commodity    | ForeignKey(Commodity) |     /      |    /    |  CASCADE  |   商品编号   |
| parent_comment |     IntegerField      |     /      |    0    |     /     |  上层评论ID  |


