# pytest-flask-issue-101

A reproducible example for `issue #101`_

To run, create a virtual env and activate it

    .. code-block::

        python -m venv venv && source venv/bin/activate

Installd dependencies

    .. code-block::

        pip istall -r requirements.txt

Run tests

    .. code-block::

        pytest

Obs. Make sure redis is running before executing tests

.. _issue #101: https://github.com/pytest-dev/pytest-flask/issues/101
