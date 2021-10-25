from solver import solver
from exact import u_exact
from visualize import visualize
import argparse
import numpy as np
#from parser import parser

def main():
	#main function
	parser = argparse.ArgumentParser()
	parser.add_argument('--I', type=float, default=1.0)
	parser.add_argument('--w', type=float, default=2*np.pi)
	parser.add_argument('--dt', type=float, default=0.05)
	parser.add_argument('--num_periods', type=float, default=5)
	a = parser.parse_args()
	I, w, dt, num_periods = a.I, a.w, a.dt, a.num_periods
	visualize(solver(I, w, 0.1, 10)[0], solver(I, w, 0.1, 10)[1], I, w, dt)
	print("hasta ahora todo jevi")

if __name__ == '__main__':
	main()
