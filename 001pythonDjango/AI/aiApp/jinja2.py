from django.template.backends.jinja2 import Jinja2
from django.template.context import BaseContext

class Jinja2Context(BaseContext):
    def __init__(self, dict_=None, **kwargs):
        super().__init__(dict_=dict_, **kwargs)
        self.update({
            'request': None,
        })

    def __copy__(self):
        return self.__class__(dict_=self)

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, dict(self))

class Jinja2(Jinja2):
    def get_template(self, template_name):
        return super().get_template(template_name)

    def from_string(self, template_code):
        return super().from_string(template_code)

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
        return super().render(context)

    def get_context(self, context, request=None):
        return Jinja2Context(context, request=request)