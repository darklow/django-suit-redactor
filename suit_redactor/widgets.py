# from django.core.serializers import json
from django.forms import Textarea
from django.utils.safestring import mark_safe

try: import json
except ImportError: import django.utils.simplejson as json

FOCUS_SCRIPT = """
    $('.redactor_box').click(function(e){if(!$(e.srcElement).is('.redactor_toolbar')){$('.redactor_editor').focus();}});
"""


class RedactorWidget(Textarea):
    class Media:
        css = {
            'all': ('suit-redactor/redactor/redactor.css',)
        }
        js = ('suit-redactor/redactor/redactor.min.js',)

    def __init__(self, attrs=None, editor_options={}):
        super(RedactorWidget, self).__init__(attrs)
        self.editor_options = editor_options


    def render(self, name, value, attrs=None):
        output = super(RedactorWidget, self).render(name, value, attrs)
        output += mark_safe(
            '<script type="text/javascript">$("#id_%s").redactor(%s);%s</script>'
            % (name, json.dumps(self.editor_options), FOCUS_SCRIPT))
        return output
