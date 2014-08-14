#-------------------------------------------------------------------------------
# Name:        presentationScheduler
#
# Author:      Gouri Shankar Ghosh
#
# Created:     10/08/2014
#-------------------------------------------------------------------------------

import csv, os
import itertools

def getRow(csvFile):
    '''
    Parameter:
    csvFile <str> : CSV file name, from where the data will be fetched
    return an generator of the row from the csv file
    '''
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
    '''
    Parameter:
    mxPresenterNum <int> : The max number of presenter(s) for the combination
    data <list of list> : the confrenence data
    totDur <int> : Total confrenence duration in hour
    '''
    return filter(lambda x: sum([ei[1] for ei in x]) == totDur, list(itertools.combinations(data, mxPresenterNum)))

def sortData(data):
    '''
    Parameter:
    data <list of list> : sort the data according to the cumulative cost for each
    combination
    '''
    return sorted(data, key=lambda x: sum([int(i[2]) for i in x]))

def getMaxPresenterCombination(totSlot, confDuration, csvFile):
    '''
    Parameters :
    totSlot <int> : Total available slot, for which we need to find max num of presenter
    confDuration <int> : Total confrenence duration in hour
    csvFile <str> : The csv file name from which we will fetch the data

    Maximize the number of presenters - Select the case that fits in maximum number of
    presenters in the given time schedule. If multiple cases satisfy this scenario,
    select the ones with minimum cost.
    '''
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
    '''
    Parameters :
    totSlot <int> : Total available slot, for which we need to find minimum cost
    confDuration <int> : Total confrenence duration in hour
    csvFile <str> : The csv file name from which we will fetch the data

    Minimize the cost - Select the case which results in minimum cost for the organizer.
    If multiple cases satisfy this scenario, then select the ones with maximum number of
    presenters.
    '''
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

