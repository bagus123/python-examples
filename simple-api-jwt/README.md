## Python+Flask+JWT

###Installation

1. install [Python 3.7](https://www.python.org/downloads/ "Python 3.7") (Bundle with pip, no need install pip)
2. Install VirtualEnv, after python installed in your pc, goto command and run this command
   `pip install virtualenv`
3. Install VirtualEnvWrapper-win
   `pip install virtualenvwrapper-win`
4. make folder pyjwt in your drive
5. goto into your folder, set virtual env by command
```shell
		#make virtual env
		mkvirtualenv pyjwt
		#set project virtual env
		setprojectdir .

```

6. clone git
   `git clone https://github.com/bagus123/python-examples.git`
7. goto into folder simple-api-jwt
8. download all library
   `pip install -r requirements.txt`
9. running application (windows)
   `SET FLASK_ENV = development && SET FLASK_APP=run.py && flask run`

---

##### source

- [pip docs](https://pip.pypa.io/en/stable/user_guide/ "pip docs")
- [step by step install pyhton](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/ "step by step install pyhton")
- [active/deactive env](https://www.codingforentrepreneurs.com/blog/activate-reactivate-deactivate-your-virtualenv/ "active/deactive env")
- [SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/ "SQLAlchemy")
