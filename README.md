# NewsBoard API
API that allows to manage posts and comments of the NewsBoard. 

API usage documentaion can be found here: https://documenter.getpostman.com/view/18156181/UVByKqLS
https://www.getpostman.com/collections/6dd88d4cf5e60c14de1a

Can be deployed locally using docker/docker-compose (API and PostgreSQL containers):
```shell
docker-compose up -d
```
(in the root directory)
API listens on 8000 port on localhost. PostgreSQL database located on docker volume (../newsboarddb). Custom DB can be specified using DATABASE_URL environment variable.

The test version of API is also deployed on Heroku at https://caty-news-board-api.herokuapp.com/api


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
