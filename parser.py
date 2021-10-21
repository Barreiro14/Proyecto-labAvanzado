import argparse
import numpy as np

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--I', type=float, default=1.0)
    parser.add_argument('--w', type=float, default=2*np.pi)
    parser.add_argument('--dt', type=float, default=0.05)
    parser.add_argument('--num_periods', type=float, default=5)
    a = parser.parse_args()
    I, w, dt, num_periods = a.I, a.w, a.dt, a.num_periods