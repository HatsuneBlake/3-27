def method_Tracer(f):
	f.calls = 0
	def wrapper(*args,**kargs):
		f.calls += 1
		print 'Call %s:%r times'%(f.__name__,f.calls)
		return f(*args,**kargs)
	return wrapper
	
class N(object):
	def __init__(self,data):
		self.data = data
	
	@method_Tracer
	def g(self):
		print self.data
	
	@method_Tracer
	def f(self):
		print 'func 2'
		
if __name__ == '__main__':
	a = N('stuff')
	a.g()
	a.f()
	a.g()
	a.g()
	a.f()