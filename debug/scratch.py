import logging

logging.basicConfig(filename="logtestgile.txt", 
                level = logging.DEBUG, 
                format = '%(levelname)s: %(asctime)s %(message)s',
                datefmt = '/%m/%d/%Y %I:%M:%S') 

i=0 
while i<10:
    logging.info("Logging test: {}".format(i))
    i+=1 

