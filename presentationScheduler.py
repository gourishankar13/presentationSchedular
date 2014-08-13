#-------------------------------------------------------------------------------
# Name:        presentationScheduler
# Purpose:
#
# Author:      Gouri Shankar Ghosh
#
# Created:     10/08/2014
#-------------------------------------------------------------------------------

import csv, os
import itertools

def getRow(csvFile):
    if os.path.exists(csvFile):
        data = csv.reader(open(csvFile))
        fields = data.next()
        for echRow in data:
            try:
                echRow[1] = int(echRow[1])
                echRow[2] = int(echRow[2][1:])
            except:
                continue
            yield echRow


def findCombination(mxPresenterNum, data, totDur):
    return filter(lambda x: sum([ei[1] for ei in x]) == totDur, list(itertools.combinations(data, mxPresenterNum)))

def sortData(data):
    return sorted(data, key=lambda x: sum([int(i[2]) for i in x]))

def getMaxPresenterCombination(totSlot, confDuration, csvFile):
    data = list(getRow(csvFile))
    result = []
    for mxPresenterNum in range(totSlot, 0, -1):
        result = findCombination(mxPresenterNum, data, confDuration)
        if result:
            result = sortData(result)
            # As got max presenter
            break
    lstCost = None
    res = []
    for echSet in result:
        tmp = [0]
        for echPresenter in echSet:
            tmp.insert(-1, echPresenter[0])
            tmp[-1] += echPresenter[2]
        if lstCost == None:
            lstCost = tmp[-1]
        elif lstCost < tmp[-1]:
            break
        res.append(tmp)

    return res if res else "Not enough presenters"

def getMinCost(totSlot, confDuration, csvFile):
    data = list(getRow(csvFile))
    result = []
    for mxPresenterNum in range(1, totSlot+1):
        result.extend(findCombination(mxPresenterNum, data, confDuration))

    result = sortData(result)

    lstCost = None
    res = []
    for echSet in result:
        tmp = [0]
        for echPresenter in echSet:
            tmp.insert(-1, echPresenter[0])
            tmp[-1] += echPresenter[2]
        if lstCost == None:
            lstCost = tmp[-1]
        elif lstCost < tmp[-1]:
            break
        res.append(tmp)

    return res if res else "Not enough presenters"


if __name__ == '__main__':

    # Global Constants
    CONFERENCE_DURATION = 8
    TOTAL_SLOT = 3
    CSV_DATA_FILE = "data.csv"
    from pprint import pprint
    print "*"*100
    pprint(getMaxPresenterCombination(TOTAL_SLOT, CONFERENCE_DURATION, CSV_DATA_FILE))
    print "*"*100
    pprint(getMinCost(TOTAL_SLOT, CONFERENCE_DURATION, CSV_DATA_FILE))
    print "*"*100

