FROM ubuntu:latest
LABEL authors="eshan"

ENTRYPOINT ["top", "-b"]