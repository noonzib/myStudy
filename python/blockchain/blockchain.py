class Blockchain(object):
	"""docstring for Blockchain"""
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		#Create genesis block
		self.new_block(previous_hash=1, proof=100)

		 

	def new_block(self, proof, previous_hash=None):
		 
		"""
		Creates a new Block and adds it to the chain
		
		:param proof: <int> proof는 Proof of Work 알고리즘에 의해서 제공된다
		:param previous_hash: (Optional) <str> 이전 블록의 해쉬값 
		:return : <dict> 새로운 블록

		"""

		block = {
			'index' : len(self.chain) + 1,
			'timestamp' : time(),
			'transactions' : self.current_transactions,
			'proof' :proof,
			'previous_hash' :previous_hash or self.hash(self.chain[-1]).
		}
		pass

	def new_transaction(self, sender, recipient, amount):
		#Adds a new transaction
		"""
		Creates a new transaction to go into the next mined Block


		:param sender : <str> Sender's address
		:param recipient: <str> Recipient's address
		:param amount: <int> Amount
		:return: <int> 이 거래를 포함할 블록의 index 값 
		"""

		self.current_transactions.append({
			'sender': sender, 
			'recipient': recipient,
			'amount': amount,
		})

		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		#Hashes a Block
		pass

	@property
	def last_block(self):
		# Returns the last Block in the chain
		pass
	
		