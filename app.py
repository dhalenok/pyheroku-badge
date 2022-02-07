import io
import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import falcon
import requests

ALLOWED_STYLES = ("flat-square", "plastic")


def get_badge(name: str, style: Optional[str] = None):
    if style and style in ALLOWED_STYLES:
        image_path = os.path.join(os.getcwd(), f"img/{name}-{style}.svg")
    else:
        image_path = os.path.join(os.getcwd(), f"img/{name}.svg")

    stream = io.open(image_path, "rb")
    content_length = os.path.getsize(image_path)

    return stream, content_length


class HerokuBadge:
    def on_get(self, req, resp):
        if not req.params:
            resp.content_type = "text/html"
            resp.status = falcon.HTTP_200
            with io.open("index.html", "rb") as f:
                resp.body = f.read()
                return

        app = req.params.get("app")
        path = req.params.get("path")

        if path is None:
            path = "/"

        if not app:
            resp.status = falcon.HTTP_501
            return

        style = req.params.get("style")

        resp.cache_control = ("public, max-age=0",)
        resp.content_type = "image/svg+xml;charset=utf-8"
        resp.date = datetime.now(timezone.utc)
        resp.expires = datetime.now(timezone.utc) + timedelta(minutes=2)
        resp.x_dns_prefetch_control = False

        url = f"https://{app}.herokuapp.com{path}"
        try:
            r = requests.get(url, timeout=3.6)
        except requests.exceptions.Timeout:
            resp.stream, resp.content_length = get_badge(name="timeout", style=style)
        else:
            if r.status_code == 200:
                resp.stream, resp.content_length = get_badge(
                    name="deployed", style=style
                )
            elif r.status_code == 404:
                resp.stream, resp.content_length = get_badge(
                    name="not-found", style=style
                )
            else:
                resp.stream, resp.content_length = get_badge(name="failed", style=style)


application = falcon.API()
application.add_route("/", HerokuBadge())
