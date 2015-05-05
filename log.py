from time import strftime
log_location = 'log.txt'


def write(message, critcal = False):
    time = strftime("%Y-%m-%d %H:%M:%S")
    log = '| ' + str(time) + ' | [' + str(message) + '] \n'
    if critcal:
        log = '! ' + str(time) + ' ! [' + str(message) + '] \n'
    f = open(log_location, 'a')
    f.write(log)
    f.close()
