from jinja2 import Environment,StrictUndefined

class Renderer:
    def __init__(self):
        self.environment = Environment(autoescape=True)
    
    def render(self,content,token_values) :
        template = self.environment.from_string(content)

        return template.render(**token_values)