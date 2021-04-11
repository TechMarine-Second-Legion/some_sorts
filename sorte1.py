import random, xlwt
rw = random.randint

#cnt=0
def merge_sort(alist, start, end, cnt):
    cnt[0] += 1
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid, cnt)
        merge_sort(alist, mid, end, cnt)
        merge_list(alist, start, mid, end)
    #return cnt
 
def merge_list(alist, start, mid, end):
    
    #cnt+=1
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i, j = 0, 0
    
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k +=1
    
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            alist[k] = right[j]
            j += 1
            k += 1

#def good_start(w):
	#return w(w, 0, len(w))

def first_test(ln, cnt):
	
	alist = [rw(1,100) for i in range(ln)]
#alist = ["aa", 'ab', 'ba', 'abb', 'bab','acc','gav', 'asf']
	#print(alist, end = '\n\n')
	return merge_sort(alist, 0, len(alist), cnt)
	#good_start(alist)
	#print(f'Sorted list: \n {alist}', end='\n')

#first_test()

def k1():
	#rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)

#выбираем активный лист
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Test')
	
	for i in range(3, 20):
		cnt = []
		cnt.append(0)
		ws.write(1+i, 0, i)
		first_test(i,cnt)
		ws.write(1+i, 1,cnt[0])
	wb.save('xl_rec.xls')

k1()

#print(cnt)
