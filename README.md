# djangobot-example

This is an example chat application built on Django, [channels](https://channels.readthedocs.org) & [djangobot](https://github.com/djangobot/djangobot).

## Installation and Setup

First, clone this repo and move into it:

```shell
$ git clone https://github.com/djangobot/djangobot-example.git
$ cd djangobot-example
```

Install python and make a virtual environment. The [Python Guide](http://docs.python-guide.org/en/latest/starting/installation/) has documentation for the major platforms.

Install the requirements:

```shell
$ pip install -r requirements.txt
```

Boot up Django:

```shell
$ ./manage.py runserver
```

In another shell, boot up djangobot:

```shell
$ DJANGOBOT_TOKEN=[your slack token] djangobot slackers.asgi:channel_layer
```

Finally, open your [browser](http://localhost:8000/). You should see a page like this:

![](https://www.evernote.com/l/AITb9voIrS1OVrx3Y9cB0q7IwD42CCkOISsB/image.png)

If not, open an issue and we'll help to get you up and running.

## TODO

1. Setup a `procfile` and add instructions for booting up on Heroku.
