
Abhängigkeiten
--------------

Python-Libs:

* pytz
* markdown

Ubuntu-Rollout-Notizen
----------------------

Install dependencies and create new user

	# apt-get install git python-virtualenv
	# useradd -U -m embassy

Clone repo:

	embassy:~$ git clone git://github.com/pyropeter/embassyweb.git

a) On Ubuntu 10.04 virtualenv is too old. Do this and skip the next step:

	embassy:~$ git clone git://github.com/pypa/virtualenv.git
	embassy:~$ python virtualenv/virtualenv.py django.env

b) Create virtualenv for django 1.4:

	embassy:~$ virtualenv django.env

Activate the virtualenv and install requirements:

	embassy:~$ . django.env/bin/activate
	(django.env)embassy:~$ pip install -r embassyweb/requirements.txt

Edit settings.py:

* Admins
* Database setup
* Secrets should be secret (SECRET and DOORSTATE\_SECRET)

Create database and run development server:

	(django.env)embassy:embassyweb$ python manage.py syncdb
	(django.env)embassy:embassyweb$ python manage.py runserver 0.0.0.0:8000

Check if everything works. Click links, be admin, create and view a blogpost.
After that, get a coffee to assist you with the lighttpd configuration.

First, add the following line to settings.py:

	FORCE_SCRIPT_NAME=""

After adding that line, the development server will no longer work. Please
don't ask why. But the fastcgi will work! (I hope) This setting is so secret
that even the writers of django's "Django + Lighttpd + Fastcgi" howto don't
know about it. Even the documentation about this config option (in addition
to being unfindable) is wrong. You are a very lucky person to read this,
because it will save you about a day of debugging.

Now you can create the lighttpd config (mostly the stuff from the django docs).
Put the following into e.g. /etc/lighttpd/conf-available/43-embassy.conf:
(**TODO**: static files müssen irgendwie richtiger gehandhabt werden)

	$HTTP["host"] =~ "^embassy.pyropeter.eu$" {
	  fastcgi.server = (
	    "/embassyweb.fcgi" => (
	      "main" => (
	        #"host" => "127.0.0.1",
	        #"port" => 50000,
	        "socket" => "/home/embassy/sock",
	        "check-local" => "disable",
	        #"broken-scriptfilename" => "enable",
	        "fix-root-path-name" => "enable",
	      )
	    )
	  )
	
	  alias.url = (
	    "/static/admin/" => "/home/embassy/django.env/lib/python2.7/site-packages/django/contrib/admin/static/admin/",
	    "/static/" => "/home/embassy/embassyweb/static/",
	    #"/media/" => "/srv/data/http/embassy.pyropeter.eu/media/",
	  )
	
	  url.rewrite-once = (
	    "^(/static/.*)" => "$1",
	    #"^(/media/.*)" => "$1",
	    "^(/.*)$" => "/embassyweb.fcgi$1",
	  )
	}

Enable fastcgi and your config:

	# lighttpd-enable-mod fastcgi
	# lighttpd-enable-mod embassy
	# invoke-rc.d lighttpd reload

Everything should work fine now. Remember to set DEBUG to False in settings.py.
You should also look into the traceback-by-email-thingie django has built in.
(**TODO**)

Codekonventionen
----------------

* Maximale Zeilenlänge ist 80 Zeichen
* Python-Code wird mit Tabs eingerückt


