#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A short and simple redirecting service"""
from app.api import app

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)