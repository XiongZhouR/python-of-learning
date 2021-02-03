places=['jiuzhaigou','xilinxueshan','changbaishan','mogaoku']
print(places) #打印列表
print(sorted(places)) #临时按字母顺序打印列表
print(places) # 核实列表原始顺序未改变
print(sorted(places,reverse=True)) #临时按照字母相反顺序打印列表
print(places) # 核实列表原始顺序未改变
places.reverse()
print(places) #反转打印列表
places.reverse()
print(places) #再次反转列表使列表恢复到原始顺序
places.sort()
print(places)#永久性按照字母顺序打印列表
places.sort(reverse=True)
print(places) #永久性按照字母相反顺序打印列表
print(places) #打印确认列表确实已经永久改变顺序
print(len(places)) #打印列表长度

