export SETTINGS="config.DevelopmentConfig"

py.test --junitxml=TEST-flask-forum.xml --cov-report term-missing --cov application tests
