docker build -t log-severity-test .

docker run --log-driver=gcplogs log-severity-test