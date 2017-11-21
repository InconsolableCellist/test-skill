import sys
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.messagebus.message import Message
from os.path import dirname, abspath, basename
from pprint import pprint, pformat

sys.path.append(abspath(dirname(__file__)))

__author__ = 'InconsolableCellist'

LOGGER = getLogger(__name__)

class TestSkill(MycroftSkill): 
    def __init__(self): 
        super(TestSkill, self).__init__(name="TestSkill")

    def initialize(self):
        LOGGER.info("initializing TestSkill")

        # below, change to .optionally("Artist"). \ 
        # to replicate bug 
        test_intent = IntentBuilder("TestIntent"). \
                require("TestKeyword"). \
                require("Artist"). \
                build()
        self.register_intent(test_intent, self.handle_test_intent)

    def stop(self):
        pass

    def handle_test_intent(self, message):
        LOGGER.info("message.data is {}".format(pformat(message.data)))

        if 'Artist' in message.data:
            LOGGER.info("Artist found! {}".format(message.data['Artist']))

def create_skill(): 
    return TestSkill()

