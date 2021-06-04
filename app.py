from flask import Flask, render_template

app = Flask(__name__)

contents_arr = []
contents_arr.append(["title1", "content1"])
contents_arr.append(["title2", "content2"])
contents_arr.append(["title3", "content3"])

@app.route("/")
def home():
    return render_template("app.html", contents=contents_arr)

if __name__ == "__main__":
    app.run()


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
