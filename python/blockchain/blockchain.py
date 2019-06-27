import hashlib
import json
import requests
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request
from urllib.parse import urlparse

class Blockchain(object):
	"""docstring for Blockchain"""
	def __init__(self):
		self.chain = []
		self.current_transactions = []
		self.nodes = set()
		#Create genesis block
		self.new_block(previous_hash=1, proof=100)

	def valid_chain(self, chain):
		"""
		주어진 블록 체인이 유효한지 판단 
		
		:param chain: <list> 블록체인
		:return :<bool> 유효한 경우 True, 그렇지 않으면 False
		"""

		last_block = chain[0]
		current_index = 1

		while current_index < len(chain):
			block = chain[current_index]
			print(f'{last_block}')
			print(f'{block}')
			print("\n--------------\n")
			if block['previous_hash'] != self.hash(last_block):
				return False
			
			if not self.valid_proof(last_block['proof'], block['proof']):
				return False

			last_block = block
			current_index += 1
		
		return True
	
	def resolve_conflicts(self):
		"""
		이곳이 합의 알고리즘, 노드 중에서 가장 긴 체인을 가지고 있는 노드의 체인을 유효한 것으로 인정한다. 
		"""
		
		neighbours = self.nodes
		new_chain = None

		max_length = len(self.chain)

		for node in neighbours:
			response = requests.get(f'http://{node}/chain')

			if response.status_code == 200:
				length = response.json()['length']
				chain = response.json()['chain']

				if length > max_length and self.valid_chain(chain):
					max_length = length
					new_chain = chain
		
		if new_chain:
			self.chain = new_chain
			return True
		
		return False
		

	def register_node(self, address):
		"""
		새로운 노드가 기존의 노드의 list에 등록되는 곳이다
		'http://172.0.0.1:5002 와 같은 형태로 등록을 요청하면된다
		"""

		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc)



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
			'previous_hash' :previous_hash or self.hash(self.chain[-1]),
		}

		#거래 내역 초기화
		self.current_transactions = []
		self.chain.append(block)
		return block

	def new_transaction(self, sender, recipient, amount):
		#Adds a new transaction
		"""
		Creates a new transaction to go into the next mined Block

		:param sender : <str> sender의 주소
		:param recipient: <str> Recipient의 주소
		:param amount: <int> Amount
		:return: <int> 이 거래를 포함할 블록의 index 값 
		"""

		self.current_transactions.append({
			'sender': sender, 
			'recipient': recipient,
			'amount': amount,
		})

		return self.last_block['index'] + 1

	@property
	def last_block(self):
		return self.chain[-1]

	@staticmethod
	def hash(block):
		"""
		Creates a SHA-256 hash of Block

		:param block: <dict> Block
		:return : <str>
		"""
		
		#we must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()
		
	def proof_of_work(self, last_proof):
		"""
		POW 알고리즘 설명:
		- 앞에서 0의 개수가 4개가 나오는 hash(pp')을 만족시키는 p'을 찾는다.
		- p는 이전 블록의 proof, p' 는 새로운 블록의 proof

		:param last_proof : <int>
		:return : <int>
		"""

		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	@staticmethod
	def valid_proof(last_proof, proof):
		"""
		Proof 검증 방법 : hash(last_proof, proof)의 값의 앞의 4자리가 0인가?

			:param last_proof: <int> 이전 블록의 proof 값 
			:param proof: <int> 현재 블록의 proof 값
			:return : <bool> 옳다면 true 값 아니면 false 값 반환
		"""
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
	#다음 블록의 proof 값을 얻어내기 위해 POW 알고리즘을 수행
	last_block = blockchain.last_block
	last_proof = last_block['proof']
	proof = blockchain.proof_of_work(last_proof)

	#proog 값을 찾으면(채굴에 성공하면) 보상을 준다.
	#sender의 주소를 0 으로한다. (원래 거래는 송신자, 수신자가 있어야 하는데 채굴에 대한 보상으로 얻은 코인은 sender가 없다.)
	blockchain.new_transaction(
		sender="0",
		recipient=node_identifier,
		amount=1,
	)

	#
	previous_hash = blockchain.hash(last_block)
	block = blockchain.new_block(proof, previous_hash)
	response = {
		'message' : "New Block Forged",
		'index' : block['index'],
		'transactions' : block['transactions'],
		'proof' : block['proof'],
		'previous_hash': block['previous_hash'],
	}
	return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transactions():
	values = request.get_json()

	#요청된 필드가 POST 된 데이터인지 확인하는 
	required = ['sender', 'recipient', 'amount']
	if not all(k in values for k in required):
		return 'Missing values', 400

	# 새로운 거래 생성
	index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

	response = {'message' : f'Transaction will be added to Block {index}'}
	return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200
if __name__ == '__main__':
	app.run(host='127.0.0.1', port= 5000)
