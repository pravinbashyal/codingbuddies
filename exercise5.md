## Question 1

Below is a simple code to do an api request and read from it.

```python
from urllib.request import Request, urlopen
import json
url = "https://api.forismatic.com/api/1.0/?&method=getQuote&format=json&lang=en"
req = Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

contents = urlopen(req).read()
jsonContent = json.loads(contents)

print(jsonContent)
```

running the above code gives an output like below:

`{'quoteText': 'To succeed, we must first believe that we can. ', 'quoteAuthor': 'Michael Korda', 'senderName': '', 'senderLink': '', 'quoteLink': 'http://forismatic.com/en/78e93cb12d/'}`

Read the code and add an comment what each line is doing. <br/>

If you are using python 2.7 and you encounter error:

```
Traceback (most recent call last):
  File "lesson6.py", line 1, in <module>
    from urllib import Request, urlopen
ImportError: cannot import name Request
```
use this to solve the issue:
https://stackoverflow.com/questions/24652074/importerror-no-module-named-request

## Question 2

Using code above, the library [Vocabulary](https://github.com/tasdikrahman/vocabulary) and your imagination 🌈, create a quote plagiarizer that:
  - replaces all the words that are longer than 4 letters with the *first* synonym provided from the vocabulary library.
  - gives following output:

  ```
  To succeed, we must first believe that we can.
    - Michael Korda

  To come through, we must start with trust that we can.
  - Pravin Bashyal
  ```

Resources:
You need to install pip to install the package `Vocabulary`
To install pip:
Read through this https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x

I also highly encourage you to read through and know about [python virtual environment](https://docs.python.org/3/library/venv.html) and use it to manage your library/module dependencies:

virtual env TLDR;
  - it is an isolated environment for python
  - it is useful for:
    - managing the project specific dependencies
    - not pollute the global python with dependencies that is project specific.(which is basically the same point mentioned above)

```bash
# create env
$ python3 -m venv <any_arbitrary_env_name>
# use env
$ source ./env/bin/activate
# install dependency using the env
$ python -m pip install vocabulary
```
