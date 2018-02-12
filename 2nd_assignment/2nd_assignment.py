import os
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.wrappers import Request, Response
from flask import Flask, render_template

app = Flask(__name__)
root_path = os.path.sep.join(app.instance_path.split(os.path.sep)[:-1])
@app.route("/")


@app.route('/result')
def result():
    ta_name_list = ["alice", "joni", "mike"]
    ta_hourly_rate_list = [60, 65, 70]
    ta_hours_list = [30, 36, 40]
    
    index = 0 
    output =[]
    
    for number in ta_name_list:
        n = ta_name_list[index]
        r = ta_hourly_rate_list[index]
        h = ta_hours_list[index] 
        
        index = index + 1
        TA_fees = n + " has received $" + str(h * r) +"."
         
        output.append(TA_fees)
         
    output = dict(zip(ta_name_list,output))
    
    return render_template('result.html', result = output)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/static': root_path+'/static',
        '/templates': root_path+'/templates'
     })
    run_simple('localhost', 7000, app)