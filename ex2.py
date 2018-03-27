import time

class tracer(object):
	def __init__(self,func):
		self.func = func
		self.calls = 0
		self.alltime = 0
	def __call__(self,*args,**kargs):
		start = time.clock()
		result = self.func(*args,**kargs)
		elapse = time.clock() - start
		self.calls += 1
		self.alltime += elapse
		format = 'Call function:%s %r times,Alltime used:%.5f'
		value = (self.func.__name__,self.calls,self.alltime)
		print format%value
		return result
		
		
@tracer
def f(N):
	return [x*2 for x in range(N)]
	
@tracer
def g(N):
	return list(map((lambda x:x*2),range(N)))
	

	
if __name__ == '__main__':
	for turn in range(10):
		for i in (f,g):
			i(10000)