# ------
# Logger
# ------
# this code uses 'logging' to create a basic log file

# import
import logging

# logger setup
logging.basicConfig(filename='/var/log/myLog.log',level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")
log = logging.getLogger('myLog')

# log 1 - info
log.info("this in an 'info' log")

# log 2 - warning
log.warning("this in an 'warning' log")

# log 3 - error
log.error("this in an 'error' log")

# log 4 - info with {}
myVariable = 4477
log.info("myVariable is: {}".format(str(myVariable)))
