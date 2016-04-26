from fabric.api import *


def build():
    with lcd('src/Bolt_wordpresspublish'):
        local('python ./manage.py migrate --noinput')
        with lcd('static/'):
            local('bower install')
