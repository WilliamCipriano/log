from time import strftime
import os

#find local path, should still work if py2exe is used.
path = os.path.dirname(__file__).replace('\\library.zip','')

#default log location
log_default = 'log.html'
log_path = path + '\logs\\'

#Program details (these are just placed at the start of the log file, might help with version tracking etc)
app_name = 'Undefined Program'
app_version = '0.0.0'
app_author = 'Will Cipriano'
app_email = 'logs@wfc.help'
email_subject = 'Logfile Error'



def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def check_file(path, file):
    time = strftime("%Y-%m-%d %H:%M:%S")
    if os.path.isfile(path + file) == False:
        f = open(path + file, 'a')
        html = "<HEAD><TITLE>" + app_name + " log</TITLE><HEAD>\n"
        html += "<center><H2>" + app_name + " Log file</H2><br>\n"
        html += "originally created: " + time + "<br>\n"
        html += "creator version: " + app_version + "<br>\n"
        html += "author: " + app_author + "<br>\n"
        html += "contact: <a href='mailto:" + app_email + "?Subject=" + email_subject + "'>" + app_email + "</a><br></center>\n\n"
        html += "<hr>\n"
        f.write(html)
        f.close()

def write(message, critcal = False,file = False):
    #Get current time/date.
    time = strftime("%Y-%m-%d %H:%M:%S")

    #Create log text, and set critical flag.
    if critcal:
        log = "<B><font color = 'red'>! " + str(time) + " !</B></font> [" + str(message) + "] <br>\n"
    else:
        log = '| ' + str(time) + ' | [' + str(message) + '] <br>\n'

    #Check path and create if needed.
    check_path(log_path)

    #Check file then open it, using location defined by function call if defined.
    if file == False:
        check_file(log_path, log_default)
        f = open(log_path + log_default, 'a')
    else:
        check_file(log_path, file)
        f = open(log_path + file, 'a')

    #Write a close file.
    f.write(log)
    f.close()
