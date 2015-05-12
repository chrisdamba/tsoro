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
		pawns   = 0
		pawns_first_row = 0
		pawns_second_row    = 0
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
		pawns   = 0
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

	def play_turn(current_player, next_player, Won, turn1):

		turn1 +=1
		os.system('cls')
		os.system('color %s' %current_player.color)

		raw_input(current_player.name+", hit enter to start turn.")

		turn = 1
		
		if current_player.name[-1] == 'S': #Just some proper grammer
			print "\nIt is "+current_player.name+"' Turn\n"
		else:
			print "\nIt is "+current_player.name+"'s Turn\n"

		print "FOOD from MILLs:",current_player.buildings["MILL"]["num"]*5*current_player.advances['CROP ROTATION']
		print "WOOD from LUMBER YARDs:",current_player.buildings["LUMBER YARD"]["num"]*5*current_player.advances['SHARPER AXES']
		print "GOLD from QUARRYs:",current_player.buildings["QUARRY"]["num"]*5*current_player.advances['SHARPER PICKS']

		if current_player.buildings["FACTORY"]["num"] >0:
			print "WOOD, FOOD, and GOLD from FACTORIES:",current_player.buildings["FACTORY"]["num"]*20
		
		current_player.food["num"]+=current_player.buildings["MILL"]["num"]*5*current_player.advances['CROP ROTATION']+(current_player.buildings["FACTORY"]["num"]*20)
		current_player.wood["num"]+=current_player.buildings["LUMBER YARD"]["num"]*5*current_player.advances['SHARPER AXES']+(current_player.buildings["FACTORY"]["num"]*20)
		current_player.gold["num"]+=current_player.buildings["QUARRY"]["num"]*5*current_player.advances['SHARPER PICKS']+(current_player.buildings["FACTORY"]["num"]*20)

		research = False

		while turn and Won==False:

			if current_player.buildings["WONDER"]["num"]>0:
				Won = True

			if Won == True:
				raw_input(str(current_player.name)+" Won! ")
				return(0, 0, Won)			
			
			
			choice = raw_input("What do you want to do?: ").upper()
			print "\n"
			
			if choice == "BUILD" or choice == "B":          #Build buildings to help supply resources
				print "WOOD: "+str(current_player.resources["WOOD"]["num"])+"\n"
				for keys in current_player.buildings.keys():
					print keys+"----------------"
					print "Current number: "+str(current_player.buildings[keys]["num"])
					print "WOOD required to build: "+str(current_player.buildings[keys]["price"])
					print current_player.buildings[keys]["desc"]
					print "\n"

				build_choice = raw_input("What would you like to build?: ").upper()
				print "\n"
				
				if build_choice in current_player.buildings:
					if current_player.resources["WOOD"]["num"]>=current_player.buildings[build_choice]["price"]:
						current_player.resources["WOOD"]["num"]-=current_player.buildings[build_choice]["price"]
						current_player.buildings[build_choice]["num"]+=1
						print "Current WOOD: "+str(current_player.resources["WOOD"]["num"])
						print "Current number of "+str(build_choice)+":", current_player.buildings[build_choice]["num"]
					else:
						print "Not enough WOOD!"
				else:
					print "Please choose a valid option."

				raw_input("\nPress enter to continue ")

			elif choice == "RESEARCH" or choice == "R":     #Research advanced ways to gather resources
				print "GOLD: "+str(current_player.resources["GOLD"]["num"])+"\n"
				if research == False:
					for keys in current_player.advances.keys():
						print keys+"----------------"
						print "Current level: "+str(current_player.advances[keys])
						print "GOLD required to upgrade: "+str((current_player.advances[keys]*2)**2)
						print "\n"

					research_choice = raw_input("What would you like to upgrade?: ").upper()
					print "\n"
					if research_choice in current_player.advances:
						if current_player.resources["GOLD"]["num"]>=(current_player.advances[research_choice]*2)**2:
							current_player.resources["GOLD"]["num"]-=(current_player.advances[research_choice]*2)**2
							current_player.advances[research_choice]+=1
							print "Current GOLD: "+str(current_player.resources["GOLD"]["num"])
							print "Current",research_choice,"level:", current_player.advances[research_choice]
							#research = True
						else:
							print "Not enough GOLD!"
					else:
						print "Please choose a valid option."
				elif research:
					print "You can only research one thing per turn!"

				raw_input("\nPress enter to continue ")

			elif choice == "TRAIN" or choice == "T":
				print "FOOD: "+str(current_player.resources["FOOD"]["num"])+"\n"
				for keys in current_player.units.keys():
					print keys+"----------------"
					print "FOOD required to use: "+str(current_player.units[keys]["price"])
					print current_player.units[keys]["desc"]
					print "\n"

				train_choice = raw_input("What would you like to train?: ").upper()
				if train_choice in current_player.units:
					if current_player.resources["FOOD"]["num"]>=current_player.units[train_choice]["price"]:
						current_player.resources["FOOD"]["num"]-=current_player.units[train_choice]["price"]
						current_player.units[train_choice]["num"]+=1
						print "Current FOOD: "+str(current_player.resources["FOOD"]["num"])
						print "Current "+train_choice+":",current_player.units[train_choice]["num"]
					else:
						print "Not enough FOOD!"
				else:
					print "Please choose a valid option."

				raw_input("\nPress enter to continue ")

			elif choice == "DEPLOY" or choice == "D":
				for i in current_player.units:
					print i, current_player.units[i]["num"]

				deploy_choice = raw_input("What would you like to deploy?: ").upper()
				print "\n"
				
				if deploy_choice in current_player.units and current_player.units[deploy_choice]["num"]>0:
					if deploy_choice == "SPY":
						print "*REPORT*\n*ENEMY HAS*\n"
						for i in next_player.buildings:
							print i, next_player.buildings[i]["num"]
						for i in next_player.resources:
							print i, next_player.resources[i]["num"]
						for i in next_player.advances:
							print i, next_player.advances[i]
						print "/n*END REPORT*"

						current_player.units["SPY"]["num"]-=1

					elif deploy_choice == "RAIDER">0:
						list1 = []
						for i in next_player.buildings:
							list1.append((next_player.buildings[i]["num"], i))
						
						destroyed = max(list1)
						if destroyed[0]>0:
							next_player.buildings[destroyed[1]]["num"]-=1
							print "Enemy %s destroyed!" %destroyed[1]
							current_player.units["RAIDER"]["num"]-=1
						else:
							print "Nothing to destroy!"

					elif deploy_choice == "THIEF">0:
						available_resources = []
						for i in next_player.resources:
							if next_player.resources[i]["num"]>=5:
								available_resources.append(i)
								
						if len(available_resources)>0:
							print "You could steal 5 of:"
							for i in available_resources:
								print i
						else:
							print "Nothing to steal!"

						succeded = False
						if len(available_resources)>0:
							while succeded == False:
								steal = raw_input("What would you like to steal?: ").upper()
								if steal in available_resources:

									next_player.resources[steal]["num"]-=5
									current_player.resources[steal]["num"]+=5
									succeded = True
									
								else:
									print "Error"

								if succeded == True:
									current_player.units["THIEF"]["num"]-=1

				raw_input("\nPress enter to continue ")


			elif choice == "END" or choice == "E":
				turn = False
				everything = [current_player, next_player, Won, turn]

				output = open('.\Saves\\'+current_player.name[:6]+next_player.name[:6]+str(turn1)+'.pkl', 'wb')

				pickle.dump(everything, output, -1)

				output.close()
				
			elif choice == "QUIT" or choice == "Q":
				exit("QUITTING")


			else:
				print "Not an option"



		if turn==0:
			raw_input("\nHit enter to end your turn. ")
			return(next_player, current_player, Won, turn1)

	def execute(self):

		if self.unit_action_queue.empty():
			return UnitAction.ACTION_UNIT_NONE
		else:
			unit = self.unit_action_queue.get()

			return execute_unit_action(unit)