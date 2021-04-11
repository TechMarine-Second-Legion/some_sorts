import pytest, random
from sorte import *

@pytest.mark.parametrize("test_input",[0, 1, 2, 10, 10**5])
def test_ri(test_input):
	alist = [rw(1,100) for i in range(test_input)]
	assert alist.copy().sort() == merge_sort(alist, 0, len(alist))
	print(cnt)
	
@pytest.mark.parametrize("test_input",[0, 1, 2, 10, 10**5])
def test_ri_alf(test_input):
	alf = "ёйфячыцувсмакепитрнгоьблшщдюзхъэ"
	alist = [''.join([alf[rw(0,len(alf)-1)] for i in range(rw(1,15))]) for i in range(test_input)]
	assert alist.copy().sort() == merge_sort(alist, 0, len(alist))
	print(cnt)


