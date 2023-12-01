# Copyright (c) 2023, khan and contributors
# For license information, please see license.txt
import random
import datetime
import frappe
from frappe.model.document import Document

class TINApplication(Document):
	def validate(self):
		self.generate_tin()

	def generate_tin(self):
		eleven_digit_number = ''.join([str(random.randint(0, 9)) for _ in range(11)])

		# Add '2' at the beginning to make it 12 digits
		twelve_digit_number = '2' + eleven_digit_number
		self.tin = twelve_digit_number
		self.full_name = self.first_name + " " + self.last_name
			