from flask import Flask,jsonify
from flask_caching import Cache

def create_app():
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'caches:'
    CACHE_REDIS_URL = 'redis://localhost:64067/0'
    DEBUG = True
    CACHE_DEFAULT_TIMEOUT = 5 * 60  # seconds

    app = Flask(__name__)
    app.config.from_object(__name__)

    cache = Cache(app)


    @app.route('/')
    @cache.cached(query_string=True)
    def index():
        return jsonify({"message": "Hello world"})

    return app