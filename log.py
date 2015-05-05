from time import strftime
log_location = 'log.txt'


def write(message, critcal = False):
    time = strftime("%Y-%m-%d %H:%M:%S")
    log = '| ' + time + ' | [' + message + '] \n'
    if critical:
        log = '! ' + time + ' ! [' + message + '] \n'
    f.open(log_location)
    f.write(log)
    f.close()
    
    
