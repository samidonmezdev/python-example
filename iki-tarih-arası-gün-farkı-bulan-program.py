from datetime import datetime
tarih=str(input("tarih griniz :(gg/aa/yyyy) "))
tarih2=str(input(" ikinci tarihi giriniz : "))
pt1=tarih.split('/')
pt2=tarih2.split('/')
t1 = datetime.datetime(year =pt[2] , month = pt[1], day = pt[0])
t2 = datetime.datetime(year = pt2[2], month = pt2[1], day = pt2[0])
print("1. tarih : ",tarih)
print("2. tarih : ",tarih2)
print("iki tarih arası gün sayısı : ",str(t2-t1))
