#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gouri
#
# Created:     13-08-2014
# Copyright:   (c) gouri 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
from presentationScheduler import *

class TestPresentationScheduler(unittest.TestCase):

    def setUp(self):
        self.testDataFile = ["data1.csv",
                             "data2.csv",
                             "data_not_enough_presenter.csv"]

    def test_normalInput(self):
        '''Test for normal input'''

        CONFERENCE_DURATION = 8
        TOTAL_SLOT = 3
        USED_DATA_FILE = self.testDataFile[0]

        retMxPresenter = getMaxPresenterCombination(TOTAL_SLOT, CONFERENCE_DURATION, USED_DATA_FILE)
        expectedRetVal = [['P1', 'P3', 'P4', 300],
                          ['P1', 'P4', 'P5', 300],
                          ['P3', 'P4', 'P5', 300]]

        retMinCost = getMinCost(TOTAL_SLOT, CONFERENCE_DURATION, USED_DATA_FILE)
        expectedRetVal = [['P6', 50]]

    def test_not_enough_presenter(self):
        '''Test for no data'''

        expectedRetVal = "Not enough presenters"
        CONFERENCE_DURATION = 8
        TOTAL_SLOT = 3
        USED_DATA_FILE = self.testDataFile[2]

        retMxPresenter = getMaxPresenterCombination(TOTAL_SLOT, CONFERENCE_DURATION, USED_DATA_FILE)
        self.assertEqual(retMxPresenter, expectedRetVal)

        retMinCost = getMinCost(TOTAL_SLOT, CONFERENCE_DURATION, USED_DATA_FILE)
        self.assertEqual(retMinCost, expectedRetVal)

    def test_some_date_contains_no_cost(self):
        '''Test for faulty data'''
        CONFERENCE_DURATION = 8
        TOTAL_SLOT = 3
        USED_DATA_FILE = self.testDataFile[1]

        retMxPresenter = getMaxPresenterCombination(TOTAL_SLOT, CONFERENCE_DURATION, USED_DATA_FILE)
        expectedRetVal = [['P1', 'P3', 'P4', 300],
                          ['P1', 'P4', 'P5', 300],
                          ['P3', 'P4', 'P5', 300]]
        self.assertEqual(retMxPresenter, expectedRetVal)

        retMinCost = getMinCost(TOTAL_SLOT, CONFERENCE_DURATION, USED_DATA_FILE)
        expectedRetVal = [['P6', 50]]
        self.assertEqual(retMinCost, expectedRetVal)

if __name__ == '__main__':
    unittest.main()