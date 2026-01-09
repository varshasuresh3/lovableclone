from calculator import Calculator
from flask import render_template

class Calculator:
    def __init__(self):
        self.render_template = render_template

    def render_template(self, template_name, **kwargs):
        return render_template(template_name, **kwargs)
