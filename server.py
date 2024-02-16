from flask import Flask, request, redirect
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "rendom : <strong>" + str(random.random()) + "</strong>"





# 실제 서버에서는 삭제 port=5001, debug=True
app.run(port=5001, debug=True)
