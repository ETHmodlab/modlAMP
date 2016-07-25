import unittest
import re
from modlamp.sequences import Hepahelices


class TestHepa(unittest.TestCase):
	H = Hepahelices(12, 30, 1)
	H.generate_sequences()

	def test_seq_length(self):
		self.assertIn(len(self.H.sequences[0]), range(12, 31))

	def test_binding_domain(self):
		self.assertIsNotNone(re.search('[AGILPVFWYSTNQ][KR][KR][KR][AGILPVFWYSTNQ][AGILPVFWYSTNQ][KR][AGILPVFWYSTNQ]',
							   self.H.sequences[0]))

if __name__ == '__main__':
	unittest.main()
