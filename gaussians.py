import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as stats

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Sans Serif"],
    "font.size": 14,
    "figure.dpi": 300})

plt.rcParams['axes.spines.left'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False

x=np.linspace(0, 1, 10000)
iq1=stats.norm(0.4, 0.1) #Gaussian for y=0
iq2=stats.norm(0.65, 0.1) #Gaussian for y=1

plt.plot(x, iq1.pdf(x), 'b')
plt.plot(x, iq2.pdf(x), 'r')
plt.vlines(0.5, 0.0, 4, colors='#00ff00', linestyles='solid', linewidth=2.0) #Probability threshold

px1=np.linspace(0.0, 0.5, 100)
px2=np.linspace(0.5, 1.0, 100)
plt.fill_between(px2, iq2.pdf(px2), color='r', alpha=0.3) #Filling TPR area
plt.fill_between(px2, iq1.pdf(px2), facecolor='none', hatch='X', edgecolor='b', linewidth=2.0, alpha=0.5) #Filling FPR area

plt.xlabel(r'$f(\hat{\mathbf{x}},\mathbf{w}^\star)$')
plt.ylim(0)
plt.tick_params(top=False, bottom=True, left=False, right=False,
                labelleft=False, labelbottom=True)

plt.legend([r'$\hat{y}=0$', r'$\hat{y}=1$', r'$P_T$', r'TPR', r'FPR'])
plt.savefig('Plots/ROCs-class_dists.png', bbox_inches='tight', pad_inches=0.01)
#plt.show()
