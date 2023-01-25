# FlaskOAuthServer

This repository contains a proof of concept for an OAuth 2.0 server in Python with Flask. This PoC is needed for an university project.
This implementation is inspired by the [Authlib server example](https://github.com/authlib/example-oauth2-server).

## Authlib
This PoC uses [Authlib](https://authlib.org/) as a library to make the implementation easier. Authlib is used because the university 
project has already used Authlib for other scenarios.

## Testing
If you want to test the OAuth server with your own client please have a look at the [OAuth 2.0 Client PoC](https://github.com/AnsgarLichter/FlaskOAuthClient).

## Tips
You may have to install the following if you use Ubuntu:
``sudo apt-get install python3-tk``
