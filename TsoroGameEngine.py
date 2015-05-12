from queue import *
from random import randrange
from enum import Enum


class UnitAction(Enum):

	ACTION_UNIT_DRAW  = 0
	ACTION_UNIT_SEED = 1
	ACTION_UNIT_EAT = 2
	ACTION_UNIT_PUNISH = 3
	ACTION_GO_FORWARD = 4
	ACTION_EAT = 5
	ACTION_EAT_BACKWARDS = 6
	ACTION_UNIT_NONE = 16

class TsoroGameEngine:

	NOT_INITIALIZED = None
	HUMAN = 1
	COMPUTER = 2	
	unit = {}
	unit['index_begin'] = 0
	unit['index_end'] = 0
	unit['unit_action'] = 0	
	unit_action_queue = Queue()
	board = [[0 for x in range(16)] for x in range(16)] 

	def __init__(self, level=None):

		self.player = self.HUMAN
		self.can_play = True
		self.is_start = True
		self.player = self.HUMAN		
		self.index_current = self.NOT_INITIALIZED
		self.eat_active = False

		pawns_human = 0
		pawns_computer = 0
		rand = 0
		index = 0

		if level == None:
			self.count = 0
			for i in range(0, 16):
				if i >= 8:
					self.board[self.HUMAN-1][i] = 4
					self.board[self.COMPUTER-1][i] = 4
				else:
					self.board[self.HUMAN-1][i] = 0
					self.board[self.COMPUTER-1][i] = 0
		else:
			self.count = 5
			if level == 1:
				pawns_human = 48
				pawns_computer = 16
			elif level == 2:
				pawns_human = 32
				pawns_computer = 32
			elif level == 3:
				pawns_human = 16
				pawns_computer = 48

			for i in range(0, 16):
				self.board[self.HUMAN-1][i] = 0
				self.board[self.COMPUTER-1][i] = 0

			while pawns_human > 0:
				index = randrange(0, 16)

				if pawns_human < 5:
					self.board[self.HUMAN-1][index] += pawns_human
					pawns_human = 0
				else:
					rand = randrange(0, 5)
					self.board[self.HUMAN-1][index] += rand
					pawns_human -= rand

			while pawns_computer > 0:
				index = randrange(0, 16)

				if pawns_computer < 5:
					self.board[self.COMPUTER-1][index] += pawns_computer
					pawns_computer = 0
				else:
					rand = randrange(0, 5)
					self.board[self.COMPUTER-1][index] += rand
					pawns_computer -= rand
	
	def get_current_hole(self):
		return self.index_current

	def get_current_player(self):
		return self.player

	def set_current_player(self, player):
		self.player = player

	def get_can_play(self):
		return self.can_play

	def set_can_play(self, state):
		self.can_play = state

	def get_is_start(self):
		return self.is_start

	def set_is_start(self, state):
		self.is_start = state

	def get_pawns(self, player, index):
		if (player == self.COMPUTER or player == self.HUMAN) and index >= 0 and index < 16:
			return self.board[player-1][index]
		else:
			return None

	def get_computer_move():
		move = None

	def computer_start(self):
		self.player = self.COMPUTER

	def print_board(self):
		#  Board configuration
		#  07 06 05 04 03 02 01 00
		#  08 09 10 11 12 13 14 15
		#  =======================
		#  15 14 13 12 11 10 09 08
		#  00 01 02 03 04 05 06 07

		board_human = self.board[self.HUMAN-1]
		board_human.extend(range(1,17))
		board_computer = self.board[self.COMPUTER-1]
		board_computer.extend(range(1,17))

		print(' ---------------------------------------------------------------------------------------------------------------')
		print('|             |             |             |             |             |             |             |             |')
		print('|    '+str(board_computer[7])+'             '+str(board_computer[6])+'              '+str(board_computer[5])+'              '+str(board_computer[4])+'              '+str(board_computer[3])+'            '+str(board_computer[2])+'            '+ str(board_computer[1])+'             '+str(board_computer[0])+'      ')
		print('|             |             |             |             |             |             |             |             |')
		print(' ---------------------------------------------------------------------------------------------------------------')
		print('|             |             |             |             |             |             |             |             |')
		print('|    '+str(board_computer[8])+'             '+str(board_computer[9])+'              '+str(board_computer[10])+'              '+str(board_computer[11])+'              '+str(board_computer[12])+'             '+str(board_computer[13])+'            '+ str(board_computer[14])+'            '+str(board_computer[15])+'      ')
		print('|             |             |             |             |             |             |             |             |')
		print(' ---------------------------------------------------------------------------------------------------------------')
		print(' ---------------------------------------------------------------------------------------------------------------')
		print('|             |             |             |             |             |             |             |             |')
		print('|    '+str(board_human[15])+'             '+str(board_human[14])+'              '+str(board_human[13])+'              '+str(board_human[12])+'             '+str(board_human[11])+'             '+str(board_human[10])+'            '+ str(board_human[9])+'            '+str(board_human[8])+'      ')
		print('|             |             |             |             |             |             |             |             |')
		print(' ---------------------------------------------------------------------------------------------------------------')
		print('|             |             |             |             |             |             |             |             |')
		print('|    '+str(board_human[0])+'             '+str(board_human[1])+'              '+str(board_human[2])+'              '+str(board_human[3])+'            '+str(board_human[4])+'              '+str(board_human[5])+'            '+ str(board_human[6])+'            '+str(board_human[7])+'      ')
		print('|             |             |             |             |             |             |             |             |')
		print(' ---------------------------------------------------------------------------------------------------------------')


	def action_to_units(self, player, move):
		pawns	= 0
		pawns_first_row = 0
		pawns_second_row	= 0
		index = 0
		i = 0
		player = (self.COMPUTER if self.player == self.HUMAN else self.HUMAN)

		if move.action == UnitAction.ACTION_GO_FORWARD:
			
			if ((move.index_begin >= 8) and (move.index_begin < 16) and (self.board[self.player - 1][move.index_begin] > 1) and (self.count > 4) and (self.index_current != -1) and (self.eat_active == True)):
				pawns_first_row = self.board[player - 1][23 - move.index_begin]								
				pawns_second_row = self.board[player - 1][move.index_begin - 8]	

				if (pawns_first_row > 0) and (pawns_second_row > 0):
					self.unit.unit_action = UnitAction.ACTION_UNIT_PUNISH
					self.unit.index_begin = move.index_begin
					self.unit.index_end = self.NOT_INITIALIZED
					self.unit_action_queue.push(self.unit)

			self.eat_active = True
			self.index_previous_current = move.index_begin

			pawns = self.board[self.player - 1][move.index_begin]
			self.unit.unit_action = UnitAction.ACTION_UNIT_DRAW
			self.unit.index_begin = move.index_begin
			self.unit.index_end = self.NOT_INITIALIZED
			self.unit_action_queue.push(self.unit)

			for i in range(move.index_begin+1, move.index_begin+pawns):
				self.unit.unit_action = UnitAction.ACTION_UNIT_SEED
				self.unit.index_begin = i % 16
				self.unit.index_end = (move.index_begin+pawns) % 16
				self.unit_action_queue.push(self.unit)

		elif move.action == UnitAction.ACTION_EAT:
			self.eat_active = False
			self.unit.unit_action = UnitAction.ACTION_UNIT_EAT
			self.unit.index_begin = move.index_begin
			self.unit.index_end = self.NOT_INITIALIZED
			self.unit_action_queue.push(self.unit)

		elif move.action == UnitAction.ACTION_EAT_BACKWARDS:
			
			if (move.index_begin >= 8) and (move.index_begin < 16) and (self.board[self.player - 1][move.index_begin] > 1) and (self.count > 4) and (self.index_current != -1) and (self.eat_active == True):
				pawns_first_row = self.board[player - 1][23 - move.index_begin]								
				pawns_second_row = self.board[player - 1][move.index_begin - 8]	

				if (pawns_first_row > 0) and (pawns_second_row > 0):
					self.unit.unit_action = UnitAction.ACTION_UNIT_PUNISH
					self.unit.index_begin = move.index_begin
					self.unit.index_end = self.NOT_INITIALIZED
					self.unit_action_queue.push(self.unit)

			self.eat_active = True
			self.index_previous_current = move.index_begin

			pawns = self.board[self.player - 1][move.index_begin]
			self.unit.unit_action = UnitAction.ACTION_UNIT_DRAW
			self.unit.index_begin = move.index_begin
			self.unit.index_end = self.NOT_INITIALIZED
			self.unit_action_queue.push(self.unit)

			for i in range(move.index_begin+1, move.index_begin+pawns):
				self.unit.unit_action = UnitAction.ACTION_UNIT_SEED
				self.unit.index_begin = i % 16
				self.unit.index_end = (move.index_begin+pawns) % 16
				self.unit_action_queue.push(self.unit)

		else:
			return False

		return self.unit.unit_action

	def execute_unit_action(self, unit):
		pawns	= 0
		pawns_first_row = 0
		pawns_second_row = 0		
		player = (self.COMPUTER if self.player == self.HUMAN else self.HUMAN)

		if unit.unit_action == UnitAction.ACTION_UNIT_DRAW:
			self.board[self.player - 1][unit.index_begin] = 0							
			self.index_current = self.index_begin

		elif unit.unit_action == UnitAction.ACTION_UNIT_SEED:
			self.board[self.player - 1][unit.index_begin] += 1
			
			if (unit.index_begin == unit.index_end) and (self.board[self.player - 1][unit.index_begin] == 1) and (self.unit_action_queue.empty()):
				self.player = self.COMPUTER if self.player == self.HUMAN else self.HUMAN
				self.count += 1
				self.index_current = self.NOT_INITIALIZED
			else:
				self.index_current = unit.index_begin

		elif unit.unit_action == UnitAction.ACTION_UNIT_EAT:			
			pawns_first_row = self.board[player - 1][23 - unit.index_begin]								
			pawns_second_row = self.board[player - 1][unit.index_begin - 8]

			self.board[player - 1][23 - unit.index_begin] = 0							
			self.board[player - 1][unit.index_begin - 8] = 0

			self.board[self.player - 1][unit.index_end] += pawns
			self.index_current = unit.index_end

		elif unit.unit_action == UnitAction.ACTION_UNIT_PUNISH:
			pawns_first_row = self.board[player - 1][23 - unit.index_begin]								
			pawns_second_row = self.board[player - 1][unit.index_begin - 8]

			pawns = pawns_first_row + pawns_second_row

			self.board[player - 1][23 - unit.index_begin] += pawns_second_row							
			self.board[player - 1][unit.index_begin - 8] = 0
			self.index_current = unit.index_end
		else:
			return UnitAction.ACTION_UNIT_NONE

		return unit.unit_action

	def execute(self):

		if self.unit_action_queue.empty():
			return UnitAction.ACTION_UNIT_NONE
		else:
			unit = self.unit_action_queue.get()

			return execute_unit_action(unit)