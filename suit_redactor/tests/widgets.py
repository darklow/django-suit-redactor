from django.test import TestCase
from suit_redactor.widgets import RedactorWidget
from django.contrib.admin.templatetags.admin_static import static


class WidgetsTestCase(TestCase):
    def test_RedactorWidget(self):
        widget = RedactorWidget()
        self.assertEqual({}, widget.editor_options)

    def test_RedactorWidget_with_editor_options(self):
        options = {'iframe': True}
        widget = RedactorWidget(editor_options=options)
        self.assertEqual(options, widget.editor_options)


    def test_RedactorWidget_output(self):
        widget = RedactorWidget()
        name = 'body'
        value = '123'
        output = widget.render(name, value)
        self.assertHTMLEqual(output, (
            '<textarea cols="40" name="%s" rows="10">%s</textarea><script '
            'type="text/javascript">$("#id_%s").redactor({});</script>' % (
                name, value, name)))

    def test_RedactorWidget_output_with_editor_options(self):
        widget = RedactorWidget(editor_options={'iframe': True})
        name = 'body'
        value = '123'
        output = widget.render(name, value)
        self.assertHTMLEqual(output, (
            '<textarea cols="40" name="%s" rows="10">%s</textarea><script '
            'type="text/javascript">$("#id_%s").redactor({"iframe": '
            'true});</script>' % (
                name, value, name)))

    def test_RedactorWidget_media(self):
        widget = RedactorWidget()
        js_url = static(widget.Media.js[0])
        css_url = static(widget.Media.css['all'][0])
        self.assertHTMLEqual(str(widget.media),
                             '<link href="%s" media="all" rel="stylesheet" '
                             'type="text/css" /><script src="%s" '
                             'type="text/javascript" />'
                             % (css_url, js_url))
