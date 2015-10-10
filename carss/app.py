__author__ = 'brendan'
from carss.models import Car
from urlparse import urljoin
from flask import request
from werkzeug.contrib.atom import AtomFeed
from flask import Flask
from flask.templating import render_template_string, render_template
from playhouse.shortcuts import model_to_dict
import os
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask('carss', template_folder=tmpl_dir)

def make_external(url):
    return urljoin(request.url_root, url)


@app.route('/recent.atom')
def recent_feed():
    try:
        feed = AtomFeed('Recent Cars',
                        feed_url=request.url, url=request.url_root)
        cars = Car.select().order_by(Car.updated).limit(15)
        for car in cars:
            html = render_template('layout.html',
                                    **model_to_dict(car)
                                   )
            feed.add(car.title,
                     unicode(html),
                     id=car.id,
                     updated=car.updated,
                     content_type='html',
                     url=car.link)
        return feed.get_response()
    except Exception as ex:
        return ex

@app.route('/')
def home():
    return render_template('layout.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)