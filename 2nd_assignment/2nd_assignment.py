import os
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.wrappers import Request, Response
from flask import Flask, render_template

app = Flask(__name__)
root_path = os.path.sep.join(app.instance_path.split(os.path.sep)[:-1])
@app.route("/")

def result():
   dic = dict()
   ta_name_list = ["alice", "joni", "mike"]
   ta_rate_list = [60, 65, 70]
   ta_hour_list = [30, 36, 40]
   for name in range(len(ta_name_list)):
        dic[ta_name_list[name]] = str(ta_hour_list[name] * ta_rate_list[name])

   return render_template('result.html', result = dic)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/static': root_path+'/static',
        '/templates': root_path+'/templates'
     })
    run_simple('localhost', 9000, app)