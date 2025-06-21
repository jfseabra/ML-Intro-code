import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "xtick.direction": "inout",
    "ytick.direction": "inout",    
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Sans Serif"],
    "figure.dpi": 300})

plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.linewidth'] = 1.5

def make_logic_plot(gate):
    """
    Encodes instructions to plot the outputs of logic gates, as well as decision boundaries found by the artificial neuron of McCulloch and Pitts.
    
    Args:
        gate ('NOT', 'AND', 'OR', 'XOR', 'XOR2'): Logic gate. Apart from 'NOT' that assumes one binary input (0 or 1), all the other options assume two binary inputs. 'XOR2' shows a decision boundary found when the logic gate is seen as a combination of other gates.
    """
    xi = [0, 0, 1, 1]
    yi = [0, 1, 0, 1]
    xi2 = [0, 1] #For 'NOT' gate
    yi2 = [0, 0] #For 'NOT' gate
    utol = 10.
    ltol = -10.
    x = np.linspace(-2, 2, 10000)
    yy = (x - 1) / (2*x - 1) #Decision boundary for 'XOR2'.
    
    ###AND###
    if gate == 'AND':
        c = ['b', 'b', 'b', 'r']
        ann = [0, 0, 0, 1]
        for i, txt in enumerate(ann):
            plt.scatter(xi[i], yi[i], s=25, color=c[i], marker='o')
            plt.annotate(txt, (xi[i], yi[i]), xytext=(xi[i] + 0.02, yi[i] + 0.02), fontsize=16)
        plt.plot(x, 2 - x, color="C3", zorder=0) #Decision boundary
        plt.text(0.65, 1.24, r'$z>0$', rotation=-45, fontsize=16)
        plt.text(0.57, 1.18, r'$z<0$', rotation=-45, fontsize=16)
        plt.title(gate, fontsize=20)
        plt.xlim(-0.1, 1.5)
        plt.ylim(-0.1, 1.5)
        
    ###OR###
    if gate == 'OR':
        c = ['b', 'r', 'r', 'r']
        ann = [0, 1, 1, 1]
        for i, txt in enumerate(ann):
            plt.scatter(xi[i], yi[i], s=25, color=c[i], marker='o')
            plt.annotate(txt, (xi[i], yi[i]), xytext=(xi[i] + 0.02, yi[i] + 0.02), fontsize=16)
        plt.plot(x, 1 - x, color="C3", zorder=0) #Decision boundary
        plt.text(0.16, 0.76, r'$z>0$', rotation=-45, fontsize=16)
        plt.text(0.1, 0.71, r'$z<0$', rotation=-45, fontsize=16)
        plt.title(gate, fontsize=20)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)
        
    ###XOR###
    if gate == 'XOR':
        c = ['b', 'r', 'r', 'b']
        ann = [0, 1, 1, 0]
        for i, txt in enumerate(ann):
            plt.scatter(xi[i], yi[i], s=25, color=c[i], marker='o')
            plt.annotate(txt, (xi[i], yi[i]), xytext=(xi[i] + 0.02, yi[i] + 0.02), fontsize=16)
        plt.text(0.5, 0.5, '?', fontsize=20) #No decision boundary to show in this case
        plt.title(gate, fontsize=20)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)
        
    ###XOR2###
    if gate == 'XOR2':
        c = ['b', 'r', 'r', 'b']
        ann = [0, 1, 1, 0]
        for i, txt in enumerate(ann):
            plt.scatter(xi[i], yi[i], s=25, color=c[i], marker='o')
            if ann[i] == 0:
                plt.annotate(txt, (xi[i], yi[i]), xytext=(xi[i] + 0.02, yi[i] + 0.02))
            if ann[i] == 1:
                plt.annotate(txt, (xi[i], yi[i]), xytext=(xi[i], yi[i] + 0.04))
        yy[yy>utol] = np.inf
        yy[yy<ltol] = -np.inf        
        plt.plot(x, yy, color="C3", zorder=0)
        plt.text(1.2, 0.18, r'$z<0$', rotation=15)
        plt.text(1.2, 0.07, r'$z>0$', rotation=18)
        plt.text(-0.4, 0.81, r'$z>0$', rotation=12)
        plt.text(-0.4, 0.71, r'$z<0$', rotation=12)        
        plt.title('XOR', fontsize=20)
        plt.xlim(-0.5, 1.5)
        plt.ylim(-0.5, 1.5)
        
    ###NOT###
    if gate == 'NOT':
        c = ['r', 'b']
        ann = [1, 0]
        for i, txt in enumerate(ann):
            plt.scatter(xi2[i], yi2[i], s=25, color=c[i], marker='o')
            plt.annotate(txt, (xi2[i], yi2[i]), xytext=(xi2[i] + 0.02, yi2[i] + 0.02))
        plt.plot(np.zeros(10000), np.linspace(-0.1, 1.1, 10000), color="C3", zorder=0)
        plt.text(-0.08, 0.85, r'$z>0$', rotation=90, fontsize=16)
        plt.text(0.02, 0.85, r'$z<0$', rotation=90, fontsize=16)        
        plt.title(gate, fontsize=20)
        plt.xlim(-0.2, 1.1)
        plt.ylim(-0.1, 1.01) 
        plt.tick_params(top=False, bottom=True, left=False, right=False,
                labelleft=False, labelbottom=True)
    
    #Set of instructions common to all plots.
    plt.xlabel(r'$x_1$', fontsize=16)
    plt.ylabel(r'$x_2$', fontsize=16)
    plt.xticks([0, 1], ['0', '1'], fontsize=16)
    plt.yticks([0, 1], ['0', '1'], fontsize=16)   
    plt.savefig('Plots/Logic-' + gate + '.png', bbox_inches='tight', pad_inches=0.01)
    #plt.show()

make_logic_plot('XOR2')
