from flask import Flask, render_template, request
from transformers import pipeline
res = "<transalated text>"
app = Flask(__name__)
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/',methods=['GET','POST'])
def home():
    global res
    if request.method == 'POST':
        name= request.form.get('english')
        res = pipe(name)
        res = res[0]['translation_text']
        print(name)
    return render_template("index.html", res=res)
if __name__ == '__main__':
    app.run(debug=True)















