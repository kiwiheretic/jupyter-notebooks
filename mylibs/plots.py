import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


def plotfn(f, x1, x2, ks=None, points=100, legend_var="k", title=None, xlabel=None, ylabels=None, ax_loc = 'upper left', figsize=(4,3)):
    xs = np.linspace(x1, x2, num=200)
    # Each axis needs its own locator or only one axis will be marked with minor ticks
    minorLocatorX = AutoMinorLocator(5)
    minorLocatorY = AutoMinorLocator(5)
    
    def subplot(f):
        if ks:
            for k in ks:
                ys = f(xs, k)
                plt.plot(xs, ys,'-', linewidth=2, label=legend_var+'='+str(k))
        else:
            ys = f(xs)
            plt.plot(xs, ys,'-', linewidth=2)
        ax = plt.gca()
        if xlabel:
            ax.set_xlabel(xlabel)
        ax.yaxis.set_minor_locator(minorLocatorY)
        ax.xaxis.set_minor_locator(minorLocatorX)
        if ks:
            ax.legend(loc=ax_loc)
        plt.tick_params(axis='both', which='minor', length=4)   
    
    fig = plt.figure(figsize=figsize)
    ax = plt.gca()
    ax.grid(axis='both', which='major')  
    if type(f)==list:
        for ii, fn in enumerate(f):
            plt.subplot(len(f),1,ii+1)
            if ylabels:
                ylabel = ylabels[ii]
                plt.ylabel(ylabel)
            if ii==0 and title:
                plt.title(title)
            subplot(fn)
    else:
        if title: plt.title(title)
        subplot(f)
        
    return ax, plt


