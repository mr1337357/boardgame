from flask import Flask, request, render_template, make_response

lobbies = []
games = []
users = []

app = Flask(__name__)

@app.route("/",methods = ['POST','GET'])
def landing():
    global users
    user = None
    is_loggedin = False
    if request.method == 'GET':
        if 'user' in request.cookies:
            user = request.cookies['user']
            if not user in users:
                users.append(user)
    
    
    if request.method == 'POST':
        user = request.form['user']
        if not user in users:
            users.append(user)
        else:
            user = None
            
    resp = make_response(render_template('homepage.html',user=user))
    if user:
        resp.set_cookie('user',user)
    print(user)
    print(users)
    return resp
    
@app.route("/lobbylist/")
def lobby_page():
    global lobbies
    
        
@app.route('/game/')
def showgame():
    with open('../htmlclient/boardgame.html','r') as bg:
        return bg.read(999999)