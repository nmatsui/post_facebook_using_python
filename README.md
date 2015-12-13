# Sample app to post facebook timeline using python

## Description
This sample app has two features.

* CGI to get access token
* Script to post a message

## Requirement
* python 2.7
* Facebook Application

## Install
```text
$ pip install -r requirements.txt
```

## Usage
### Create conf.json
Create `conf.json` first.

```json
{
  "app": {
    "app_id": "<App ID>",
    "app_secret": "<App Secret>",
    "redirect_uri": "<callback url>"
  },
  "page": {
    "name": "<facebook page name>"
  }
}
```

### Start CGIServer
Start CGIServer.

```text
$ python -m CGIHTTPServer
```

### Access CGI
Access the next URL with your browser.

`http://localhost:8000/cgi-bin/index`

Then, you can get your "User Access Token" and "Page Access Token" of facebook. These tokens will be written to "token.json".

### Post message to facebook
You can post message to facebook using these tokens like below:

```text
$ ./post.py token.json me "test message to my timeline"
```

```text
$ ./post.py token.json page "test message to facebook page"
```

## License
[MIT License](https://github.com/nmatsui/post_facebook_using_python/blob/master/LICENSE)

## Author
Nobuyuki Matsui nobuyuki.matsui@gmail.com
