from flask import Flask, render_template, request
from t import create_report
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/report-submit/')
def report_submit():
  file = request.args.get("filename")
  release_name = request.args.get("news_release_title")
  release_date = request.args.get("news_release_date")
  pdf_title = request.args.get("report_title")
  release_url = request.args.get("url")
  create_report(file, release_date, release_name, release_url, pdf_title)
  print(file, release_name, release_date, pdf_title, release_url)
  return 'h'

if __name__ == '__main__':
  app.run(debug=True)