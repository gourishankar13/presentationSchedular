#-------------------------------------------------------------------------------
# Name:        presentationScheduler
# Purpose:
#
# Author:      Gouri Shankar Ghosh
#
# Created:     10/08/2014
#-------------------------------------------------------------------------------

import csv, os

def getRow():
    if os.path.exists(CSV_DATA_FILE):
        data = csv.reader(open(CSV_DATA_FILE))
        fields = data.next()
        for echRow in data:
            try:
                echRow[1] = int(echRow[1])
                echRow[2] = int(echRow[2][1:])
            except:
                continue
            yield echRow


def maxPresenter(data):
    '''
     Maximize the number of presenters -
     Select the case that fits in maximum number of presenters in the given time
     schedule. If multiple cases satisfy this scenario,
     select the ones with minimum cost.

    data : a list of [<presenterName>, <presentationHours><int>, <cost><int>]
    '''
    gotSlotList = []


    def __iscontinue(totCst, curLn, totDr, slotLst):
        if totDr > CONFERENCE_DURATION:
            return True
        elif totDr < CONFERENCE_DURATION:
            return False
        slotLst.append(totCst)
        # There is any data in gotSlotList only then:
        # check for low cost and remove if the previous costs are higher
        if gotSlotList:
            lstIndx = len(gotSlotList) - 1

            # Continue in following cases :
            # If current number of presenter is less or
            # if current total cost is greater than the previous cost

            if (len(gotSlotList[lstIndx]) - 1) > curLn or \
               totCst > gotSlotList[lstIndx][-1]:
                return True

            while lstIndx >= 0:
                # Delete from the list :
                # If current number of presenter is greater or
                # if current total cost is less
                if len(gotSlotList[lstIndx]) - 1 > curLn or \
                   totCst < gotSlotList[lstIndx][-1] :
                    del gotSlotList[lstIndx]
                    lstIndx -= 1
                elif set(slotLst) == set(gotSlotList[lstIndx]):
                    del gotSlotList[lstIndx]
                    lstIndx -= 1
                else:
                    # If last element is greater then we need to check else not
                    break

        gotSlotList.append(slotLst)


    for s1 in data:
        if __iscontinue(s1[2], 1, s1[1], [s1[0]]):
            continue

        for s2 in data:
            # If same data
            if s1 == s2:
                continue
            totCost = s1[2] + s2[2]
            totDur = s1[1] + s2[1]
            if __iscontinue(totCost, 2, totDur, [s1[0], s2[0]]):
                continue

            for s3 in data:
                # If same data
                if s1 == s2 or s2 == s3 or s3 == s1 :
                    continue
                totCost = s1[2] + s2[2] + s3[2]
                totDur = s1[1] + s2[1] + s3[1]
                __iscontinue(totCost, 3, totDur, [s1[0], s2[0], s3[0]])


    if gotSlotList:
        for ei in gotSlotList:
            print ei
        print "-"*100
    else:
        print "Not enough presenters"
    #return gotSlotList

def minCost(data):
    '''
       Minimize the cost - Select the case which results in minimum cost for the organizer.
       If multiple cases satisfy this scenario, then select the ones with maximum number of presenters.

    data : a list of [<presenterName>, <presentationHours><int>, <cost><int>]
    '''
    gotSlotList = []


    def __iscontinue(totCst, curLn, totDr, slotLst):
        if totDr > CONFERENCE_DURATION:
            return True
        elif totDr < CONFERENCE_DURATION:
            return False
        slotLst.append(totCst)
        # There is any data in gotSlotList only then:
        # check for low cost and remove if the previous costs are higher
        if gotSlotList:
            lstIndx = len(gotSlotList) - 1

            # Continue in following cases :
            # if current total cost is greater than the previous cost
            if totCst > gotSlotList[lstIndx][-1]:
                return True

            elif totCst == gotSlotList[lstIndx][-1] and \
                 (len(gotSlotList[lstIndx]) - 1) > curLn:
                return True

            while lstIndx >= 0:
                # Delete from the list :
                # if current total cost is less
                if totCst < gotSlotList[lstIndx][-1] :
                    del gotSlotList[lstIndx]
                    lstIndx -= 1
                elif totCst == gotSlotList[lstIndx][-1] and \
                     (len(gotSlotList[lstIndx]) - 1) < curLn:
                    del gotSlotList[lstIndx]
                    lstIndx -= 1
                elif set(slotLst) == set(gotSlotList[lstIndx]):
                    del gotSlotList[lstIndx]
                    lstIndx -= 1
                else:
                    # If last element is greater then we need to check else not
                    break
        gotSlotList.append(slotLst)


    for s1 in data:
        if __iscontinue(s1[2], 1, s1[1], [s1[0]]):
            continue

        for s2 in data:
            # If same data
            if s1 == s2:
                continue
            totCost = s1[2] + s2[2]
            totDur = s1[1] + s2[1]
            if __iscontinue(totCost, 2, totDur, [s1[0], s2[0]]):
                continue

            for s3 in data:
                # If same data
                if s1 == s2 or s2 == s3 or s3 == s1 :
                    continue
                totCost = s1[2] + s2[2] + s3[2]
                totDur = s1[1] + s2[1] + s3[1]
                __iscontinue(totCost, 3, totDur, [s1[0], s2[0], s3[0]])


    if gotSlotList:
        for ei in gotSlotList:
            print ei
        print "-"*100
    else:
        print "Not enough presenters"
    #return gotSlotList


if __name__ == '__main__':

    # Global Constants
    CONFERENCE_DURATION = 8
    CSV_DATA_FILE = "data.csv"

    data = list(getRow())
    maxPresenter(data)
    minCost(data)

