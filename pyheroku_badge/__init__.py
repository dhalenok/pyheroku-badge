import io
import re

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

from pyheroku_badge.utils import get_badge_file_path

app = FastAPI()


@app.get("/")
async def root(
    app: str | None = None, path: str | None = None, style: str | None = None
):
    if app is None and path is None:
        with io.open("public/index.html", "rb") as f:
            return HTMLResponse(content=f.read(), status_code=200)

    if app is None:
        raise HTTPException(status_code=501)

    clean_app = re.sub("[^A-Za-z0-9]+", "", app)
    if not clean_app:
        raise HTTPException(status_code=400)

    if path is None:
        path = "/"

    try:
        r = httpx.get(f"https://{clean_app}.herokuapp.com{path}", timeout=3.6)
    except httpx.TimeoutException:
        return FileResponse(get_badge_file_path(name="timeout", style=style))
    else:
        if r.status_code == 200:
            return FileResponse(get_badge_file_path(name="deployed", style=style))
        elif r.status_code == 404:
            return FileResponse(get_badge_file_path(name="not-found", style=style))
        else:
            return FileResponse(get_badge_file_path(name="failed", style=style))
