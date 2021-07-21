from flask import Flask, render_template

from datetime import date

app = Flask(__name__)

@app.route("/")
def  index():
    current = date.today()
    return render_template("index.html", date=current)

@app.route("/v2")
def  v2():
    current = date.today()
    return "Hello World!" + str(current)


#@app.route('/')
#def example():
 #   return render_template('index.html', datetime = str(datetime.now()))

#@app.route("/getTime", methods=['GET'])
#  print("browser time: ", request.args.get("time"))
#  print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
#    return "Done"


if __name__ == '__main__':
    app.run(debug=True)
