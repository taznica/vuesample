#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


def create_app(app_name='FLASK_VUE'):
    app = Flask(
        import_name=app_name,
        static_folder='./dist/static',
        template_folder='./dist'
    )

    app.config.from_object('server.config.BaseConfig')

    return app
