class Rules(object):
	"""docstring for Rules"""
	def __init__(self):
		super(Rules, self).__init__()
	

	def apply(self, neiburghs, state):
		if neiburghs < 2:
			return False

		if state == True and (neiburghs == 2 or neiburghs == 3):
			return True

		if neiburghs > 3:
			return False

		if neiburghs == 3:
			return True

		return False 