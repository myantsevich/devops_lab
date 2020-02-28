#!/bin/bash

pyenv install 2.7.5
pyenv virtualenv 2.7.5 flaskage

pyenv install 3.7.1
pyenv virtualenv 3.7.1 new-flaskage

pyenv versions