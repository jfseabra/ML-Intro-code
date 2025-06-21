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
FPR_05thres = 0
TPR_05thres = 0
for i in range(len(x_values) - 1, 0, -1):
    bkg_gaussian.append((gaussian(x_values[i], 0.4, 0.1) + gaussian(x_values[i-1], 0.4, 0.1)) / 2 * np.abs(x_values[i-1] - x_values[i]))
    sig_gaussian.append((gaussian(x_values[i], 0.65, 0.1) + gaussian(x_values[i-1], 0.65, 0.1)) / 2 * np.abs(x_values[i-1] - x_values[i]))
    # Getting the coordinates of the point corresponding to the green line in class_distributions.png
    if i == 5000:
        FPR_05thres = np.cumsum(bkg_gaussian)[-1]
        TPR_05thres = np.cumsum(sig_gaussian)[-1]
        print(FPR_05thres, TPR_05thres)

AUC = 0
for j in range(0, len(np.cumsum(bkg_gaussian)) - 1):
    AUC += (np.cumsum(sig_gaussian)[j+1] + np.cumsum(sig_gaussian)[j]) * (np.cumsum(bkg_gaussian)[j+1] - np.cumsum(bkg_gaussian)[j]) / 2.0
print("Classifier's AUC: " + str(AUC))


plt.plot(np.cumsum(bkg_gaussian), np.cumsum(sig_gaussian), color='k', linewidth=2.0)
plt.plot(x_values, x_values, color='k', linestyle='dashed') #ROC curve of random classifier.
plt.scatter([FPR_05thres], [TPR_05thres], s=25, color="#00ff00", alpha=1, zorder=4) #Point corresponding to P_T=0.5.
plt.fill_between(np.cumsum(bkg_gaussian), np.cumsum(sig_gaussian), color='k', alpha=0.25, edgecolor=None)
plt.xlabel(r'FPR')
plt.ylabel(r'TPR')
plt.ylim(0, 1.01)
plt.xlim(-0.01,1)
#plt.yscale('log')
plt.legend([r'AUC=0.96', r'AUC=0.50', r'$P_T=0.50$'], loc='lower right')
plt.savefig('Plots/ROCs-ROC_curve.png', bbox_inches='tight', pad_inches=0.01)
#plt.show()
