import os
import io
import falcon
import msgpack
import requests

def getBadge(name):
    image_path = os.path.join(os.getcwd(), f"img/{name}.png")
    stream = io.open(image_path, 'rb')
    content_length = os.path.getsize(image_path)

    return stream, content_length


class HerokuBadge():
    def on_get(self, req, resp):
        if not req.params:
            resp.content_type = "text/html"
            resp.status = falcon.HTTP_200
            with io.open("index.html", "rb") as f:
                resp.body = f.read()
                return

        app = req.params.get("app")
        if not app:
            resp.status = falcon.HTTP_501
            return

        url = f"https://{app}.herokuapp.com/"
        r = requests.get(url)
        
        resp.content_type = "image/png"
        resp.cache_control = ("no-cache", "no-store", "must-revalidate")
        if r.status_code == 200:
            resp.stream, resp.content_length = getBadge("deployed")
        else:
            resp.stream, resp.content_length = getBadge("failed")


application = falcon.API()
application.add_route('/', HerokuBadge())
