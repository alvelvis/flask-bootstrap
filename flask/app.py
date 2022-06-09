from flask import Flask, render_template, request
import os
import sys
import shutil
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html', 
        title=""
        )
