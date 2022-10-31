from flask import Flask

app=Flask(__name__)

@app.route("/")
def test():
    return "<body bgcolor='blue' text='white'><center><h2>****Flask running in Heroku Cloud****</h2></center></body>"


if __name__=='__main__':
    app.run()


    

