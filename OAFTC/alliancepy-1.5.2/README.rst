alliancepy
==========

.. image:: https://travis-ci.com/karx1/alliancepy.svg?branch=master
    :target: https://travis-ci.com/karx1/alliancepy
.. image:: https://badge.fury.io/py/alliancepy.svg
    :target: https://badge.fury.io/py/alliancepy
    :alt: PyPI package
.. image:: https://readthedocs.org/projects/alliancepy/badge/?version=latest
	:target: https://alliancepy.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status


A library to access The Orange Alliance API.
This module makes it easy to access the official First Tech Challenge database and use it in your Python projects for things like data science and more.

View the full documentation `here <https://alliancepy.readthedocs.io/en/latest/>`__

Install with:

.. code:: bash
  
  pip install alliancepy
 
Here's a simple example:

.. code:: py
  
  import alliancepy
  from alliancepy import Season
  
  client = alliancepy.Client(api_key="api_key_goes_here", application_name="application_name_goes_here")
  team = client.team(16405)
  print(team.opr(Season.SKYSTONE))

Supports
--------
Supports Python 3.6 and up.
