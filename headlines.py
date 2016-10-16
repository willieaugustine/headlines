import feedparser
from flask import Flask
from flask import render_template

app = Flask (__name__)
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml','cnn':'http://rss.cnn.com/rss/edition.rss','fox': 'http://feeds.foxnews.com/foxnews/latest','ioL': 'http://www.ioL.co.za/cmlink/1.640'}
@app.route("/")
@app.route("/<publication>")
def get_news(publication= "bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])
    """<html>
    <body>
    <h1> BBC Headlines</h1>
    <b>{0}</b> <br/>
    <i>{1}</i><br/>
    <p>{2}</p> <br/>
    </body>
    </html>""".format(first_article.get("title"), first_article.get("published"),first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
