import numpy as np
import matplotlib.pyplot as plt
from exact import u_exact

def visualize(u, t, I, w, dt):
    plt.plot(t, u, 'r--o')
    t_fine = np.linspace(0, t[-1], 1001)
    u_e = u_exact(t_fine, I, w)
    plt.hold('on')
    plt.plot(t_fine, u_e, 'b-')
    plt.legend(['numerical with dt = {}'.format(dt), 'exact'], loc='upper left')
    plt.xlabel('t')
    plt.ylabel('u')
    Dt = t[1] - t[0]
    plt.title('dt=%g' % Dt)
    umin = 1.2*u.min(); umax = -umin
    plt.axis([t[0], t[-1], umin, umax])
    plt.savefig('tmp1.png'); plt.savefig('tmp1.pdf')

