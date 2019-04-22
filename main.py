import sys
import os
import datetime
import platform

# trying to send changes from git to vs code
print('Current date :{}'.format(datetime.datetime.now()))
print('Current python path :{}'.format(sys.executable))
print('{} {}: {}'.format(platform.system(),platform.release(),platform.version()))
print('Hello World')
