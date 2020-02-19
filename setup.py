from setuptools import setup

setup(
    name="django-suit-redactor-django2",
    version="0.0.5",
    description="Imperavi Redactor (WYSIWYG editor) integration app for Django admin. http://imperavi.com/redactor/",
    author="Kaspars Sprogis (darklow)",
    author_email="info@djangosuit.com",
    url="https://github.com/darklow/django-suit-redactor",
    packages=["suit_redactor"],
    zip_safe=False,
    include_package_data=True,
    install_requires=["django<3.0", "django-suit"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "License :: Free for non-commercial use",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Topic :: Software Development :: User Interfaces",
    ],
)
