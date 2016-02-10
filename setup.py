from setuptools import setup

setup(
    name='django-suit-redactor',
    version='0.0.3',
    description='Imperavi Redactor (WYSIWYG editor) integration app for Django admin. http://imperavi.com/redactor/',
    author='Kaspars Sprogis (darklow)',
    author_email='info@djangosuit.com',
    url='https://github.com/darklow/django-suit-redactor',
    packages=['suit_redactor'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: Free for non-commercial use',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Topic :: Software Development :: User Interfaces',
    ]
)
