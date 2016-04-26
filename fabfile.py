from fabric.api import *


def build():
    with lcd('src/Bolt_wordpresspublish'):
        local('python ./manage.py migrate --noinput --settings=conf.settings.local')
        with lcd('static/'):
            local('bower install')
