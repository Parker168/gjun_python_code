

'''A file'''

from B import identityB
def identityA():
    print('\n\n\n')
    print('A: __name__ = ' + __name__)


identityA() 
identityB()