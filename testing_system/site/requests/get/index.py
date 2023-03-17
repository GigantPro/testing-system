from testing_system.site.app import app

from flask import render_template


__all__ = ("index",)

@app.route('/')
def index():
    return render_template(f'index.html')