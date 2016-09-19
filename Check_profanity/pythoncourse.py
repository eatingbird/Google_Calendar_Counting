import sys, urllib
def print_classes():
    for name, obj in urllib.getmembers(sys.modules[__name__]):
        if urllib.isclass(obj):
            print(obj)
			
