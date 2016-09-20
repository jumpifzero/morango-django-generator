# ============================================================
# Morango Django Generator Exception classes
#
# (C) Tiago Almeida 2016
#
#
# ============================================================

class CommandFailed(BaseException):
	def __init__(self, cmd_name):
		self.command = cmd_name