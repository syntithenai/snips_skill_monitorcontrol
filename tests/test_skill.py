from unittest import TestCase

from monitorcontrolskill.monitorcontrolskill import MonitorControlSkill
import time


class BaseTest(TestCase):

    def setUp(self):
        self.skill = MonitorControlSkill()


class MonitorControlSkillTest(BaseTest):
    def test_basic(self):
        pass
