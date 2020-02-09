Python Twitter

A Python wrapper around the Twitter API.

Downloads Documentation Status Circle CI Codecov Requirements Status Dependency Status
Introduction
This library provides a pure Python interface for the Twitter API. It works with Python versions from 2.7+ and Python 3.

Twitter provides a service that allows people to connect via the web, IM, and SMS. Twitter exposes a web services API and this library is intended to make it even easier for Python programmers to use.

Installing
You can install python-twitter using:

$ pip install python-twitter
If you are using python-twitter on Google App Engine, see more information about including 3rd party vendor library dependencies in your App Engine project.

Check out the latest development version anonymously with:

$ git clone git://github.com/AlexandreGusson/python
$ cd python-twitter
To install dependencies, run either:

$ make dev
or:

$ pip install -Ur requirements.testing.txt
$ pip install -Ur requirements.txt
Note that `make dev` will install into your local `pyenv` all of the versions needed for test runs using `tox`.

To install the minimal dependencies for production use (i.e., what is installed with pip install python-twitter) run:

$ make env
or:

$ pip install -Ur requirements.txt
Running Tests
The test suite can be run against a single Python version or against a range of them depending on which Makefile target you select.

Note that tests require `pip install pytest` and optionally `pip install pytest-cov` (these are included if you have installed dependencies from `requirements.testing.txt`)

To run the unit tests with a single Python version:

$ make test
to also run code coverage:

$ make coverage
To run the unit tests against a set of Python versions:

$ make tox
Documentation
View the latest python-twitter documentation at https://python-twitter.readthedocs.io. You can view Twitter's API documentation at: https://dev.twitter.com/overview/documentation

Using
The library provides a Python wrapper around the Twitter API and the Twitter data model. To get started, check out the examples in the examples/ folder or read the documentation at https://python-twitter.readthedocs.io which contains information about getting your authentication keys from Twitter and using the library.

Using with Django
Additional template tags that expand tweet urls and urlize tweet text. See the django template tags available for use with python-twitter: https://github.com/radzhome/python-twitter-django-tags

Models
The library utilizes models to represent various data structures returned by Twitter. Those models are:
twitter.Category
twitter.DirectMessage
twitter.Hashtag
twitter.List
twitter.Media
twitter.Status
twitter.Trend
twitter.Url
twitter.User
twitter.UserStatus
To read the documentation for any of these models, run:

$ pydoc twitter.[model]
API
The API is exposed via the twitter.Api class.

The python-twitter requires the use of OAuth keys for nearly all operations. As of Twitter's API v1.1, authentication is required for most, if not all, endpoints. Therefore, you will need to register an app with Twitter in order to use this library. Please see the "Getting Started" guide on https://python-twitter.readthedocs.io for more information.

To generate an Access Token you have to pick what type of access your application requires and then do one of the following:

Generate a token to access your own account
Generate a pin-based token
use the helper script get_access_token.py
For full details see the Twitter OAuth Overview

To create an instance of the twitter.Api with login credentials (Twitter now requires an OAuth Access Token for all API calls):

>>> import twitter
>>> api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
To see if your credentials are successful:

>>> print(api.VerifyCredentials())
{"id": 16133, "location": "Philadelphia", "name": "bear"}
NOTE: much more than the small sample given here will print

To fetch a single user's public status messages, where user is a Twitter user's screen name:

>>> statuses = api.GetUserTimeline(screen_name=user)
>>> print([s.text for s in statuses])
To fetch a list of a user's friends:

>>> users = api.GetFriends()
>>> print([u.name for u in users])
To post a Twitter status message:

>>> status = api.PostUpdate('I love python-twitter!')
>>> print(status.text)
I love python-twitter!
There are many more API methods, to read the full API documentation either check out the documentation on readthedocs, build the documentation locally with:

$ make docs
or check out the inline documentation with:

$ pydoc twitter.Api
Todo
Patches, pull requests, and bug reports are welcome, just please keep the style consistent with the original source.

In particular, having more example scripts would be a huge help. If you have a program that uses python-twitter and would like a link in the documentation, submit a pull request against twitter/doc/getting_started.rst and add your program at the bottom.

The twitter.Status and twitter.User classes are going to be hard to keep in sync with the API if the API changes. More of the code could probably be written with introspection.

The twitter.Status and twitter.User classes could perform more validation on the property setters.

More Information
Please visit the google group for more discussion.

Contributors
Originally two libraries by DeWitt Clinton and Mike Taylor which were then merged into python-twitter.

Now it's a full-on open source project with many contributors over time. See AUTHORS.rst for the complete list.

License
Copyright 2007-2016 The Python-Twitter Developers

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
