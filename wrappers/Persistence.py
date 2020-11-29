import maglev
import persistence

from typing import Any, List, Callable

class Persistence:
	"""
	Persistence
	"""
	def __init__(self):
		bus = maglev.maglev_MagLev.getInstance("default")
		lib = persistence.persistence_Persistence(bus)

	def EnglishAuction_Auction_CreateNew(self, obj: object) -> str:
		"""		
		Args:
			obj (object):
		Returns:
			
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = [obj]
		ret = None
		def EnglishAuction_Auction_CreateNew_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Auction.CreateNew', args, EnglishAuction_Auction_CreateNew_Ret)
		return ret

	def EnglishAuction_Auction_FindById(self):
		"""		
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def EnglishAuction_Auction_FindById_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Auction.FindById', args, EnglishAuction_Auction_FindById_Ret)

	def EnglishAuction_Auction_FindStarting(self):
		"""		
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def EnglishAuction_Auction_FindStarting_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Auction.FindStarting', args, EnglishAuction_Auction_FindStarting_Ret)

	def EnglishAuction_Auction_FindEnding(self):
		"""		
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def EnglishAuction_Auction_FindEnding_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Auction.FindEnding', args, EnglishAuction_Auction_FindEnding_Ret)

	def EnglishAuction_Auction_FindOpen(self):
		"""		
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def EnglishAuction_Auction_FindOpen_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Auction.FindOpen', args, EnglishAuction_Auction_FindOpen_Ret)

	def EnglishAuction_Bid_CountForAuction(self):
		"""		
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def EnglishAuction_Bid_CountForAuction_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Bid.CountForAuction', args, EnglishAuction_Bid_CountForAuction_Ret)

	def EnglishAuction_Bid_FindByHighestPriceForAuction(self):
		"""		
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def EnglishAuction_Bid_FindByHighestPriceForAuction_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Bid.FindByHighestPriceForAuction', args, EnglishAuction_Bid_FindByHighestPriceForAuction_Ret)

	def EnglishAuction_Bid_New(self):
		"""		
		"""
		pybus = maglev.maglev_MagLevPy.getInstance("default")
		args = []
		ret = None
		def EnglishAuction_Bid_New_Ret(async_ret):
			ret = async_ret
		ret = pybus.call('Persistence.EnglishAuction.Bid.New', args, EnglishAuction_Bid_New_Ret)


