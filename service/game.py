from datetime import datetime
import random
import json

# simple options
OPT = ["P", "S", "R"]

# options names
OPT_NAMES = { 
	"P": "Paper",
	"S": "Scissor",
	"R": "Rock"
}

# who win from who
OPT_WIN = {
	"P": "R",
	"R": "S",
	"S": "P"
}

# try to increase stats
OPT_LOSE = {
	"P": "S",
	"R": "P",
	"S": "R"
}

# Move object
class Move:
	opt = ""
	optName = ""
	player = ""

	def __init__(self, player, opt):
		self.opt = opt
		self.optName = OPT_NAMES[opt]
		self.player = player

# Game instance
class Game:
	data = []
	resolution = 1000
	results = { 
		"CPU": 0,
		"Player": 0,
		"DRAW": 0,
		"TOTAL": 0,
	}

	# resolution to determine stats to cpu moves
	def __init__(self, resolution = 1000):
		self.resolution = resolution

		# fill the stats with balanced values from start
		for r in range(resolution):
			for o in OPT:
				self.data.append(o)

	# Test a row of events
	def Test(self, count):
		for i in range(count):
			self.Execute(OPT[random.randint(0, len(OPT)-1)])

	# execute a player move
	def Execute(self, opt):
		mv = Move("Player", opt)
		cpu = self.CPUMove()
		result = self.evaluate(mv, cpu)

		self.results[result] = self.results[result] + 1
		self.results["TOTAL"] = self.results["TOTAL"] + 1
		
		return {
			"timestamp": datetime.now().time(),
			"player": mv,
			"cpu": cpu,
			"result": result
		}			

	# evaluate two moves to determine who wins
	def evaluate(self, move1, move2):
		# don't computate CPU moves
		if move1.player != "CPU":
			# increase the winner awser for future
			self.data.append(OPT_LOSE[move1.opt])

		# don't computate CPU moves, again
		if move2.player != "CPU":
			# increase the winner awser for future, again
			self.data.append(OPT_LOSE[move2.opt])

		# fits data to limit array size
		while len(self.data) > self.resolution:
			del self.data[0]

		if move1.opt == move2.opt:
			return "DRAW"
		
		if OPT_WIN.get(move1.opt) == move2.opt:
			return move1.player

		return move2.player

	# use a random number to get an almost random cpu move
	def CPUMove(self):
		return Move("CPU", self.data[random.randint(0, len(self.data)-1)])

	# get the stats from cpu moves
	def Stats(self):
		ret = {}

		# fill the return object
		for o in OPT:
			ret[o] = 0

		# sumarize data
		for o in self.data:
			ret[o] = ret.get(o) + 1

		# convert data to percenet values
		for r in ret:
			ret[r] = round(ret[r]/len(self.data)*100, 2)

		# include other usefull data on return object
		ret["resolution"] = self.resolution
		ret["len"] = len(self.data)
		ret["score"] = self.results
		
		return ret

