# sample_behave
Sample framework for using behave

Installation

1) Install browser firefox 46 (this version is still compatible with selenium library)
2) Install python 3.5 on your system
3) Clone repo with tests to a separate folder
4) Move inside the folder
5) Install virtual environment for python with a terminal command -

    $  pip3 install virtualenv
6) Create new virtual environment from inside folder with cloned repo with command -

    $  virtualenv venv
7) Activate new environment with command -

    $  source ./venv/bin/activate  (for mac)
    
    $  venv\Scripts\Activate       (for windows)

8) Install requirements with command -

    $  pip3 install -r requirements.txt

9) Run tests from within folder with test repo with command -

    $  behave
    
    (for specific feature - behave\features\{feature_name})

Please keep in mind - as its impossible to delete user from packlink.es website,
to repeat sucessful run of the tests, you should change email for newly registered users
in file 01_register.feature
