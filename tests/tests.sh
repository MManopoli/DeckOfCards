mkdir -p ./Logs
nosetests -v --nocapture tests.py > ./Logs/tests.log 2>&1