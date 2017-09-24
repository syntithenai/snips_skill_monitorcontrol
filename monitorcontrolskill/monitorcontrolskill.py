"""
Prerequisites:
uhubctl is on the path
"""

import subprocess

class MonitorControlSkill:

    def __init__(self,tts_service=None):
        """ Initialisation.
        :param db: the json database.
        :param tts_service: A TTS service, i.e. an object which has a
                            `speak(text)` method for speaking the result.
        """
        self.tts_service = tts_service
        
    def monitor_power_on(self):
        output = subprocess.check_output('ddcutil setvcp D6 1',shell = True)
        
    def monitor_power_off(self):
        output = subprocess.check_output('ddcutil setvcp D6 4',shell = True)

    def monitor_select_input(self,monitorInputNumber):
        output = subprocess.check_output('ddcutil setvcp 60 {}'.format(monitorInputNumber),shell = True)

        #if self.tts_service:
            #self.tts_service.speak(response)
