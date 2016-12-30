# config.py
# main configuration file
import os

DEBUG                           = True
HOST                            = '127.0.0.1'
PORT                            = 5000
SQLALCHEMY_DATABASE_URI         = 'postgresql://fin:toor@localhost/fgraph_alchemy'  
SQLALCHEMY_TRACK_MODIFICATIONS  = True
