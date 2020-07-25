from datetime import datetime

epoch = datetime.utcfromtimestamp(0)
def epochtime(dt):
    '''Returns a datetime object as epoch time in seconds'''
    return (dt - epoch).total_seconds()
