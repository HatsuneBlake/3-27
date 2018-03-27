import time 

def timer(label='',trace=True):
	class Timer:
		def __init__(self,func):
			self.alltime = 0
			self.func = func
		def __call__(self,*args,**kargs):
			start = time.clock()
			result = self.func(*args,**kargs)
			elapse = time.clock() - start
			self.alltime += elapse
			if trace:
				format = '%s %s:Time:%.5f;All:%.5f'
				value = (label,self.func.__name__,elapse,self.alltime)
				print format%value
			return result
	return Timer
	
@timer(label='[L]---')
def f(N):
	return [x*2 for x in range(N)]
	
@timer(label='[M]---')
def g(N):
	return list(map((lambda x:x*2),range(N)))
	

	
if __name__ == '__main__':
	for i in (f,g):
		i(10000)