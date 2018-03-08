# Flask Application Configuration
import os


DEBUG = True
BASEDIR = os.path.abspath(os.path.dirname(__file__))

if DEBUG:
    TEMPLATES_AUTO_RELOAD = True
