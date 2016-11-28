from flask import Flask

app = Flask(__name__)

from app import tasks, signal_shift_calculator