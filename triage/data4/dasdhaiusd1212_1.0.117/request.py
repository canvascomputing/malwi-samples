import sys,requests

#Some people might mistake this module for the popular python requests module
#So let's add an alias of that

sys.modules[__name__] =  sys.modules['requests']
