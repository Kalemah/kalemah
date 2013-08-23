#-*- coding:utf-8 -*-
"""Kalemah, file-base cms - version 0.0.0-dev

Usage:
    kalemah [options]
    kalemah -h | --help
    kalemah --version

Options:
  -p <no> --port <no>
    Start on Port Number [default: 3000].

  -d --debug
    Start in debug mode.

  -h --help     
    Show this screen.

  -v --version     
    Show version.
"""

from docopt import docopt
from flask import Flask
app = Flask(__name__)

from kalemah import CONFIGS
from kalemah.lib import router


@app.route('/')
@app.route('/<path:rq_url>')
@app.route('/<path:rq_url>/')
def root(rq_url='/'):
    page_content  = "Kalemah — file-base cms"
    page_content += "<br> request: {}".format(rq_url)
    # page_content += "<br><br>"+router.render( router.routes[rq_url] )
    page_content += "<br>"*5
    page_content += CONFIGS.inspect()
    return  page_content


if __name__ == '__main__':
    args = docopt(__doc__, version=__doc__.splitlines()[0])
    

    app.run(port=int(args['--port']), debug=args['--debug'])





