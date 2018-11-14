#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server.application import create_app
from flask import render_template

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
