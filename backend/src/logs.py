import sys
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger('controller')
handler = StreamHandler(sys.stdout)
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.setLevel(DEBUG)
