import time


# USE FOR LOGS
def say_operation(message, text):
    f = open('log.txt', 'a', encoding='utf-8') 
    f.write(time.ctime()+' || UID: '+str(message.from_user.id)+' || FULL NAME: '+message.from_user.full_name+' || MESSAGE: '+str(text)+'\n')
    f.close()

