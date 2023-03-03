.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

This project is innersource. Feel free to contribute and to submit your
pull-requests.

Implement Features
~~~~~~~~~~~~~~~~~~

This project is innersource. Feel free to contribute and to submit your
pull-requests.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.package_name }}` for local development.

1. Fork the `{{ cookiecutter.package_name }}` repo on github.
2. Clone your fork locally::

    $ git clone  https://github.com/git/your-name/{{ cookiecutter.package_name }}

3. Install your local copy into a virtualenv. This is how you set up your fork for local development::

    $ cd {{ cookiecutter.package_name }}/
    $ python3 -m venv .venv --upgrade-deps
    $ source .venv/bin/activate
    $ pip install -e .

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests::

    $ pip install -r requirements_test.txt -r requirements_mypy.txt
    $ flake8 {{ cookiecutter.package_name }} tests
    $ pylint {{ cookiecutter.package_name }}
    $ pytest tests
    $ mypy {{ cookiecutter.package_name }}

   To get flake8 and pylint, just pip install them into your virtualenv.

6. Commit your changes and push your branch to github::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the github website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst. Please also make sure you update the
   CHANGELOG.rst file to make sure your feature is advertised in the release
   notes.

Tips
----

To run a subset of tests::

{% if cookiecutter.use_pytest == 'y' -%}
    $ pytest tests.test_{{ cookiecutter.package_name }}
{% else %}
    $ python -m unittest tests.test_{{ cookiecutter.package_name }}
{%- endif %}