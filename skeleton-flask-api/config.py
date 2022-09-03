from os import path, getenv
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))

URL_PREFIX = '/api/v1'

VARIABLE1 = getenv('VARIABLE1')
VARIABLE2 = getenv('VARIABLE2')




