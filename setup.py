from distutils.core import setup


setup(
    name = "django-csrf",
    version = "0.1",
    author = "Brian Rosner",
    author_email = "brosner@gmail.com",
    description = "CSRF protection pre-1.2",
    long_description = open("README").read(),
    license = "BSD",
    url = "http://github.com/brosner/django-csrf",
    packages = [
        "django_csrf",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)