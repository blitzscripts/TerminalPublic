"""_Summary
#* Default Terminal API:
    Contains packet functions
"""

class Packet:
	def __init__(self, pheader):
		self.opcode=pheader
		self.buffer='0x%0*X ' % (4, pheader)

	
	def Encode1(self, n):
		append = '0x%0*X ' % (2, n)
		self.buffer = self.buffer+append
		print("Appended: "+append)

	
	def Encode2(self, n):
		append = '0x%0*X ' % (4, n)
		self.buffer = self.buffer+append
		print("Appended: "+append)

	
	def Encode4(self, n):
		append = '0x%0*X ' % (8, n)
		self.buffer = self.buffer+append
		print("Appended: "+append)

	
	def Encode8(self, n):
		append = '0x%0*X ' % (16, n)
		self.buffer = self.buffer+append
		print("Appended: "+append)
	
	
	def EncodeBuffer(self, str):
		print("Packet print not yet supported")

	
	def EncodeString(self, str):
		print("Packet print not yet supported")

	@staticmethod
	def COutPacket(nType):
		p = Packet(nType)
		print("Packet created with header: "+p.buffer)
		return p	
	
	@staticmethod
	def SendPacket(oPacket):
		print("Sending Packet: "+oPacket.buffer)

def WaitForRecv(header):
	print("Packet print not yet supported")
