# from django.core.serializers import json
from django.forms import Textarea
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.templatetags.staticfiles import static

try:
    import json
except ImportError:
    import django.utils.simplejson as json


class RedactorWidget(Textarea):
    class Media:
        css = {
            'all': (static('suit-redactor/redactor/redactor.css'),)
        }
        js = (
            static('suit-redactor/redactor/ensure.jquery.js'),
            static('suit-redactor/redactor/redactor.min.js'),
        )

    def __init__(self, attrs=None, editor_options={}):
        super(RedactorWidget, self).__init__(attrs)
        self.editor_options = editor_options

    def render(self, name, value, attrs=None):
        output = super(RedactorWidget, self).render(name, value, attrs)
        blank_element = '-__prefix__-'
        editor_options = json.dumps(self.editor_options)
        if blank_element in name:
            try:
                prefix, suffix = name.split(blank_element)
            except KeyError:
                return output
            dom_id = r'/id_{}-\d+-{}/g'.format(prefix, suffix)
            output += mark_safe("""
<script type="text/javascript">
document.addEventListener("DOMContentLoaded", function() {
    Suit.after_inline.register('%s', function (prefix, row) {
        if(row === undefined || row[0] === undefined || !row[0].childNodes){
            return;
        }
        row[0].childNodes.forEach(function(child) {
            if(!child.childNodes){
                return;
            }
            child.childNodes.forEach(function(subChild) {
                if(subChild.id){
                    var id = subChild.id.match(%s);
                    if(id !== null && id[0] !== undefined){
                        $('#' + id[0]).redactor(%s);
                    };
                }
            });
        });
    });
});
</script>
            """ % (prefix, dom_id, editor_options))
        else:
            output += mark_safe(
                '<script type="text/javascript">$("#id_%s").redactor(%s);</script>'
                % (name, editor_options))
        return output
