import os, sys

PROJECT_DIR = '/www/ec2-50-19-38-82.compute-1.amazonaws.com/hackny'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from hackny import app as application
