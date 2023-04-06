# The context of this Dockerfile is expected to be ../ from this directory and
# not the current directory of this file. This is due to the common folder as
# a dependency.
# Example:
# PS C:\Source\HelloWorldService> docker build --tag hello-world-service ./

FROM python:3.7-slim-bullseye

WORKDIR /app/service
COPY ./* ./

# hadolint ignore=DL3013
RUN pip3 install \
        --no-cache-dir \
        --upgrade pip && \
    pip3 install \
        --no-cache-dir \
        -r /app/service/requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
