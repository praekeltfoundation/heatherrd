heatherrd
=============================

.. image:: https://img.shields.io/travis/smn/heatherrd.svg
        :target: https://travis-ci.org/smn/heatherrd

.. image:: https://img.shields.io/pypi/v/heatherrd.svg
        :target: https://pypi.python.org/pypi/heatherrd

.. image:: https://coveralls.io/repos/smn/heatherrd/badge.png?branch=develop
    :target: https://coveralls.io/r/smn/heatherrd?branch=develop
    :alt: Code Coverage

A simple Python microservice that turns RTM into a synchronous HTTP interface.

::

    $ pip install heatherrd
    $ heatherrd --listen=tcp:8001 --url=http://example.com/callback-url/

::

    $ curl --user <bot-user-id>:<bot-access-token> http://localhost:8001/connect

I'll maintain the RTM connections for the bot and relay incoming RTM messages
as JSON to the URL provided.

The URL can echo a list of RTM responses as JSON which will be sent back
over the RTM connection as a reply.
