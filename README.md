Firebase Admin CLI script
-------------------------
Used to manage my firebase projects like auth users and realtime database using this commandline script.


Requirements
------------
- python3.6
- pip
- virtualenv
- Firebase Service Config json file

Installation
------------
- create a virtualenv with python3 and activate it: `virtualenv -p python3.6 Firebaseadmin; cd Firebaseadmin ; source bin/activate`
- clone the project from git: `git clone git@github.com:omaraljazairy/firebase-admin.git`
- move inside the folder and pip install the requirements.txt: `cd firebase-admin; pip install -r requirements.txt`
- add the Friebase Service config file to the shell env: `export GOOGLE_APPLICATION_CREDENTIALS="myfirbaseserviceconfig.json"`

Usage
-----

- from the command run the command: `python main.py` 
- select on of the options you will get.

TODO
----
- refactoring
- unit test
- documentation