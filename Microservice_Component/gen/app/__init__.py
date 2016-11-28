from flask import Flask

app = Flask(__name__)

from app import tasks, signalgenerator_with_shift