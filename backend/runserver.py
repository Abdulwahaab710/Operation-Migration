from birdWatchers import app
from birdWatchers import download, cache
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
app.run(debug=True)
