import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        pass
    def test_sumSales(self):
        salesLog= {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
        summedLog = {'Fri': 30, 'Mon': 80, 'Sat': 220, 'Thu': 80, 'Tue': 180, 'Wed': 225}
        self.assertDictEqual(sumSales(salesLog),summedLog)

#NEW TESTS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def test_sumSalesNEW1(self):#emptyList
        salesLog= {}
        summedLog = {}
        self.assertDictEqual(sumSales(salesLog),summedLog)

    def test_sumSalesNEW2(self):#emptyList diff type
         salesLog= {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':-100,'Tue':20,'Wed':-100,'Fri':30}}#testNegative
         summedLog = {'Mon': -70, 'Wed': 0, 'Sat': 200, 'Tue': 20, 'Fri': 30}
         self.assertDictEqual(sumSales(salesLog),summedLog)
#endNEW TESTS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def test_sumSalesN(self):
        salesLogN = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':245,'Sat':285,'Sun': 88,'Thu': 120,'Tue':180,'Wed':225}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)

#NEW TESTS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def test_sumSalesNNEW1(self):#emptyList
        salesLog= []
        summedLog = {}
        self.assertDictEqual(sumSalesN(salesLog),summedLog)

    def test_sumSalesNNEW2(self):#emptyList diff type
         salesLog= [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':-100,'Tue':20,'Wed':-100,'Fri':30}}]#testNegative
         summedLog = {'Mon': -70, 'Wed': 0, 'Sat': 200, 'Tue': 20, 'Fri': 30}
         self.assertDictEqual(sumSalesN(salesLog),summedLog)

#endNEW TESTS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 

    def test_searchDicts(self):
        #searchDicts inputs
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        self.assertEqual(searchDicts(dictList,"y"),False)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),None)

        L2 = []
        self.assertEqual(searchDicts(L2,"t"),None)
        self.assertEqual(searchDicts(L2,None),None)

    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"t"),None)

        L2 = [(0,{0:"ten"}),(0,{1:"ten"})]
        self.assertEqual(searchDicts2(L2,1),"ten")
        self.assertEqual(searchDicts2(L2,0),"ten")

    def test_busStops(self):
        routes = {
            "Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
            "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
            "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
            "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
            "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
        }
        self.assertEqual(busStops(routes,"Stadium"),['Lentil', 'Silver', 'Gray'])
        self.assertEqual(busStops(routes,"Bishop"),['Lentil', 'Wheat', 'Silver'])
        self.assertEqual(busStops(routes,"EECS"),[])

        routes2 = {
            "NewRoute1":["1","2","3","4","5","6"],"NewRoute2":["1","2","3","4","5","6"],"NewRoute3":[]
        }
        self.assertEqual(busStops(routes2,"1"),['NewRoute1','NewRoute2'])
        self.assertEqual(busStops(routes2,""),[])

    def test_palindromes(self):
        self.assertEqual(palindromes ('cabbbaccab'),['abbba', 'acca', 'baccab', 'bb', 'bbb', 'cabbbac', 'cc'] )
        self.assertEqual(palindromes ('bacdcabdbacdc') ,['abdba', 'acdca', 'bacdcab', 'bdb', 'cabdbac', 'cdc', 'cdcabdbacdc', 'dcabdbacd'])
        self.assertEqual(palindromes (' myracecars')  ,['aceca', 'cec', 'racecar'])

        self.assertEqual(palindromes ('')  ,[])
        self.assertEqual(palindromes ('ab')  ,[])

    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    #This function assumes that the first value in L is less than or equal to N.
    def getUntilN(self,L,N):
        tempL = []
        for item in L:
            tempL.append(item)
            if item>=N: break
        return tempL

    def test_interlaceIter(self):
    	#test 1
        iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(iSequence.__next__(),1)
        self.assertEqual(iSequence.__next__(),'a')
        self.assertEqual(iSequence.__next__(),2)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['b',3,'c',4,'d',5,'e',6,'f',7,'g'])

        #test2
        naturals = interlaceIter(self.OddsEvens(1),self.OddsEvens(2))
        self.assertEqual(naturals.__next__(),1)
        first20 = self.getUntilN(naturals,20)
        self.assertEqual(first20,[x for x in range(2,21)])
        self.assertEqual(naturals.__next__(),21)

        #test3 (smallest size)
        iSequence = interlaceIter(iter([1]),iter([1]))
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,[1,1])

        #test4 (no iters)
        iSequence = interlaceIter([1,2,3,4],[1,2,3,4])
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,[1,1,2,2,3,3,4,4])


    def test_typeHistogram(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('str', 3), ('int', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 2), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [])
        #test 2
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequence2 = interlaceIter(iSequence1, iter([(1,'a'),(2,'b'),(3,'c'),(4,'d')]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)),sorted([('int', 2), ('str', 2),('tuple',4)]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)), [])

        #test 3
        iSequence1= interlaceIter("hello darkness my old friend",iter("abcdefg"))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)),[('str', 5)])
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [('str', 5)])
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [('str', 4)])
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [])

        #test 4
        iSequence1= interlaceIter([1,2,3],[1,2,3])
        self.assertEqual(sorted(typeHistogram(iSequence1,5)),[('int', 5)])
        self.assertEqual(sorted(typeHistogram(iSequence1,5)),[('int', 1)])
        self.assertEqual(sorted(typeHistogram(iSequence1,5)),[])
        self.assertEqual(sorted(typeHistogram(iSequence1,5)),[])

if __name__ == '__main__':
    unittest.main()

