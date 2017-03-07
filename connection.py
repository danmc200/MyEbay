import os
class Connection ():
	def __init__(self, app_id):
		self.app_id = app_id
		self.url = ""

	def build(self):
		base_url="http://svcs.ebay.com/services/search/FindingService/v1?"
		operation_name="OPERATION-NAME=findItemsByKeywords"
		security_appname="&SECURITY-APPNAME=" + self.app_id 
		response_format="&RESPONSE-DATA-FORMAT=XML"
		keywords="&keywords=nintendo%20ds"
		item_filter_name_value="&itemFilter%280%29.name=Condition&itemFilter%280%29.value=New"
		item_filter_name_value2="&itemFilter%281%29.name=ListingType&itemFilter%281%29.value=FixedPrice"
		sort_order="&sortOrder=PricePlusShippingLowest"
		self.url=base_url + operation_name + security_appname + response_format + keywords + item_filter_name_value + item_filter_name_value2 + sort_order

	def run(self):
		os.system('echo "' + self.url + '" | xargs curl > out.html')
