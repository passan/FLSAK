from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
    ]

# html template 중복으로 함수화
def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">web</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''    
# html getContents 중복으로 함수화
def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'    
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>welcome</h2>Hello, WEB2')

# getContents 함수 적용전 코드
    # liTags = ''
    # for topic in topics:
    #     liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'    
    # return template(liTags, '<h2>welcome</h2>Hello, WEB2')
    
# template 함수 적용 적용전 코드
    # return f'''<!doctype html>
    # <html>
    #     <body>
    #         <h1><a href="/">web</a></h1>
    #         <ol>
    #             {liTage}
    #         </ol>
    #         <h2>welcome</h2>
    #         hello, web
    #     </body>
    # </html>
    # '''
    
    
    # return 'hello' + str(random.random())
    # return "rendom : <strong>" + str(random.random()) + "</strong>"

@app.route('/read/<int:id>/')
def read(id):
    # liTags = ''
    # for topic in topics:
    #     liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    title = ''
    body = ''    
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            
    return template(getContents(), f'<h2>{title}</h2>{body}')                    
            
    # return f'''<!doctype html>
    # <html>
    #     <body>
    #         <h1><a href="/">web</a></h1>
    #         <ol>
    #             {liTage}
    #         </ol>
    #         <h2>{title}</h2>
    #         {body}            
    #     </body>
    # </html>
    # '''
        

@app.route('/create/')
def create():
    return 'Create'



# rout 폴더 read2로 변경 후 동작 안됨 나중에 확인 필요
# @app.route('/read2/<int:id>/')
# def read(id):
#     print(id)
#     return 'read2'+ id

# 실제 서버에서는 삭제 port=5001, debug=True
app.run(port=5001, debug=True)
