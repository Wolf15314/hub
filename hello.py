from flask import Flask, render_template

import datetime

app = Flask(__name__)

@app.route("/")
def  index():
        return render_template("index.html")

#@app.route('/')
#def example():
 #   return render_template('index.html', datetime = str(datetime.now()))

#@app.route("/getTime", methods=['GET'])
#  print("browser time: ", request.args.get("time"))
#  print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
#    return "Done"


if __name__ == '__main__':
    app.run(debug=True)
