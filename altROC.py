import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Sans Serif"],
    "font.size": 14,
    "figure.dpi": 300})

def gaussian(x, mu, sig):
    """
    Computes the gaussian function.
    
    Args:
        x (float): Point of the domain.
        mu (float): Mean value.
        sig (float): Standard deviation.
    
    Returns:
        gaussian(x) (float)
    """
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))) / (np.power(2 * np.pi, 0.5) * sig)

x_values = np.linspace(0, 1, 10001)
bkg_gaussian = []
sig_gaussian = []
bkg2_gaussian = [] #For the random classifier
sig2_gaussian = [] #For the random classifier
FPR_05thres = 0
TPR_05thres = 0
for i in range(len(x_values) - 1, 0, -1):
    bkg_gaussian.append((gaussian(x_values[i], 0.4, 0.1) + gaussian(x_values[i-1], 0.4, 0.1)) / 2 * np.abs(x_values[i-1] - x_values[i]))
    sig_gaussian.append((gaussian(x_values[i], 0.65, 0.1) + gaussian(x_values[i-1], 0.65, 0.1)) / 2 * np.abs(x_values[i-1] - x_values[i]))
    bkg2_gaussian.append((gaussian(x_values[i], 0.5, 0.1) + gaussian(x_values[i-1], 0.5, 0.1)) / 2 * np.abs(x_values[i-1] - x_values[i]))
    sig2_gaussian.append((gaussian(x_values[i], 0.5, 0.1) + gaussian(x_values[i-1], 0.5, 0.1)) / 2 * np.abs(x_values[i-1] - x_values[i]))
    # Getting the coordinates of the point corresponding to the green line in class_distributions.png
    if i == 5000:
        FPR_05thres = 1/np.cumsum(bkg_gaussian)[-1]
        TPR_05thres = np.cumsum(sig_gaussian)[-1]
        print(FPR_05thres, TPR_05thres)

plt.plot(np.cumsum(sig_gaussian), 1/np.cumsum(bkg_gaussian), color='k', linewidth=2.0)
plt.plot(np.cumsum(sig2_gaussian), 1/np.cumsum(bkg2_gaussian), color='k', linestyle='dashed', linewidth=2.0) #ROC curve of random classifier.
plt.scatter([FPR_05thres], [TPR_05thres], s=25, color="#00ff00", alpha=1, zorder=3) #Point corresponding to P_T=0.5.
plt.xlabel(r'signal efficiency ($\epsilon_{\rm sig})$')
plt.ylabel(r'background rejection $\left(\epsilon_{\rm bkg}^{-1}\right)$')
plt.ylim(1, 100000)
plt.xlim(-0.01,1)
plt.yscale('log')
plt.legend([r'AUC=0.96', r'AUC=0.50', r'$P_T=0.50$'], loc='upper right') #These values of AUC are computed using ROC.py
plt.savefig('Plots/ROCs-altROC_curve.png', bbox_inches='tight', pad_inches=0.04)
#plt.show()
