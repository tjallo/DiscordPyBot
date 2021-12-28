import sys, os

# Dirty hack to make pytest get the correct path
# TODO: Fix
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
