# Oauth2 Proxy + Redis Example
This repository serves as an example to setup a docker oauth2-proxy, redis, and
IdP environment using a simple Hello World python flask service.

## Setup
- Add this line to your hosts file: `127.0.0.1 idp.localhost`
- Make sure you have Docker Desktop installed or have docker compose available
  in your cli.

## Usage
1. Open the command-line and make sure your working directory is the same as
the root of this repository.
2. Run this command: `docker compose up --detach`
3. Navigate in your browser to: `http://localhost/`
4. You will be prompted to login from `http://idp.localhost`. **Any username or password is accepted.**
5. Hello World! should display in your browser.