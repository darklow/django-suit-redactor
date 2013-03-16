from django.forms import Textarea
from django.utils.safestring import mark_safe
from django import forms
from django.contrib.admin.templatetags.admin_static import static



class RedactorTextarea(Textarea):
    """
    Autosized Textarea - textarea height dynamically grows based on user input
    """

    def __init__(self, attrs=None):
        attrs = attrs or {}
        new_attrs = {'rows': 2}
        new_attrs.update(attrs)
        new_attrs['class'] = 'redactor %s' % (
            attrs['class'] if 'class' in attrs else '')
        super(RedactorTextarea, self).__init__(new_attrs)

    @property
    def media(self):
        return forms.Media(js=[static('suit-redactor/redactor/redactor.min.js')])

    def render(self, name, value, attrs=None):
        output = super(RedactorTextarea, self).render(name, value, attrs)
        output += mark_safe(
            "<script type=\"text/javascript\">$('#id_%s').redactor();</script>"
            % name)
        return output
