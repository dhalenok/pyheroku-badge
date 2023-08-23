import os

AVAILABLE_STYLES = ("flat-square", "plastic")


def get_badge_file_path(name: str, style: str | None = None):
    if style and style in AVAILABLE_STYLES:
        return os.path.join(os.getcwd(), f"public/img/{name}-{style}.svg")
    return os.path.join(os.getcwd(), f"public/img/{name}.svg")
