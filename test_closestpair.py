''' Instantiates test for closest pair in a plan Algorithm'''
import unittest
import Closest_pair as cp
import random
import pdb 
import operator
import math


class Test(unittest.TestCase):


	def test_pointclass(self):
		point_list = [random.randint(-100, 100) for x in range(4)]
		point1 = cp.Point(point_list[0], point_list[1])
		point2 = cp.Point(point_list[2], point_list[3])

		self.assertEqual(point1.x, point_list[0])
		self.assertEqual(point1.y, point_list[1])
		self.assertEqual(point2.x, point_list[2])
		self.assertEqual(point2.y, point_list[3])

	def test_mergesort(self):
		input_list = [cp.Point(random.randint(-100, 100), random.randint(-100, 100)) for x in range(10)]

		x_sort = sorted(input_list, key = operator.attrgetter('x'))
		mergesort_x = cp.mergesort(input_list, 'x')
		y_sort = sorted(input_list, key = operator.attrgetter('y'))
		mergesort_y = cp.mergesort(input_list, 'y')
		
		[self.assertEqual(a.x, b.x, 'X sorting not working correctly') for a, b in zip(x_sort, mergesort_x)]
		[self.assertEqual(a.y, b.y, 'Y sorting not working correctly') for a, b in zip(y_sort, mergesort_y)]


	def test_splitpair(self):
		input_list = [cp.Point(random.randint(-100, 100), random.randint(-100, 100)) for x in range(7)]
		i, j = 0,0
		best_delta = 100

		sort_delta, sort_pair = cp.split_sort(input_list, best_delta)
		distances = [(cp.Euclidian_distance(input_list[i], input_list[j]), (input_list[i], input_list[j])) for i in range(len(input_list)) for j in range(i, len(input_list)) if i != j]
		sorted_distances = sorted(distances, key = lambda x: x[0])
		best_delta = sorted_distances[0][0]
		best_pair = sorted_distances[0][1]
	
		self.assertEqual(best_pair[0].x, sort_pair[0].x)
		self.assertEqual(best_pair[0].y, sort_pair[0].y)	

	def test_euc_distance(self):
		input_list = [cp.Point(random.randint(-100, 100), random.randint(-100, 100)) for x in range(2)]

		euc_dist = cp.Euclidian_distance(input_list[0], input_list[1])
		#pdb.set_trace()
		brute_distance = math.sqrt(math.pow(input_list[0].x - input_list[1].x, 2) + math.pow(input_list[0].y - input_list[1].y, 2))

		print("Algo Dif %s" %euc_dist)
		print("Brute Dif %s" %brute_distance)
		self.assertEqual(brute_distance, euc_dist)



	def test_closest_pair(self):
		input_list = [cp.Point(random.randint(-100, 100), random.randint(-100, 100)) for x in range(10)]
		sorted_input_x = cp.mergesort(input_list, 'x')
		sorted_input_y = cp.mergesort(input_list, 'y')
		[print((x.x, x.y)) for x in input_list]
		print("Sorted X")
		[print((x.x, x.y)) for x in sorted_input_x]
		print("Sorted Y")
		[print((x.x, x.y)) for x in sorted_input_y]

		final_delta, final_pair = cp.closest_points(input_list, sorted_input_x, sorted_input_y)

		brute_force_delta, brute_force_pair = cp.brute_force(input_list)
		
		print("Algo delta %s Algo Pair %s, %s and %s, %s" %(final_delta, final_pair[0].x, final_pair[0].y, final_pair[1].x, final_pair[1].y ))			


		print("Brute force delta %s Brute Force Pair %s, %s and %s, %s" %(brute_force_delta, brute_force_pair[0].x, brute_force_pair[0].y, brute_force_pair[1].x, brute_force_pair[1].y ))			



		


if __name__ == '__main__':
	unittest.main()