'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the main effects plots for the full framework design (see Manuscript/chapter 6 in thesis), under the expanded model.
The plots are generated for the following outcomes of crowding:
    a) Egg to wandering survivorship
    b) Mean Time to wandering
    c) Mean Mass at wandering
    d) Variance in Time to wandering
    e) Variance in Mass at wandering
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Total_Data = pd.read_excel('Results/Compiled_Total30.xlsx', sheet_name = 'TotalData')


# Total_Data['vWander'] = np.log(Total_Data['vWander'])
# Total_Data['vMass'] = np.log(Total_Data['vMass'])

sns.set_theme(style='white', font = 'Arial', rc = {
    'axes.spines.right' : False,
    'axes.spines.top' : False,
    'xtick.bottom' : True,
    'ytick.left' : True,
    'axes.edgecolor' : 'black',
    'xtick.color' : 'black',
    'ytick.color' : 'black',
    'text.color' : 'black', 
    'figure.facecolor' : 'white', 
    'axes.labelcolor' : 'black'
    })

############ Surv ############################################################


# Height

fig1, ax1 = plt.subplots()

sns.boxplot(ax=ax1, data = Total_Data, x = 'Height', y = 'Surv', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'lightcyan', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
             'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax1, data = Total_Data, x = 'Height', y = 'Surv', marker = 'o', edgecolor = 'darkcyan', facecolor = 'lightcyan', size = 6, alpha = 0.5, linewidth = 1)

# Eggs

fig2, ax2 = plt.subplots()

sns.boxplot(ax=ax2, data = Total_Data, x = 'Eggs', y = 'Surv', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'papayawhip', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'royalblue', 
             'markeredgecolor': 'royalblue', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax2, data = Total_Data, x = 'Eggs', y = 'Surv', marker = 'o', edgecolor = 'saddlebrown', facecolor = 'papayawhip', size = 6, alpha = 0.5, linewidth = 1)


# SA

fig3, ax3 = plt.subplots()

sns.boxplot(ax=ax3, data = Total_Data, x = 'SA', y = 'Surv', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'mintcream', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'crimson', 
             'markeredgecolor': 'crimson', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax3, data = Total_Data, x = 'SA', y = 'Surv', marker = 'o', edgecolor = 'darkgreen', facecolor = 'mintcream', size = 6, alpha = 0.5, linewidth = 1)


for axis in ['left', 'bottom']:
    ax1.spines[axis].set_linewidth(3)
    ax2.spines[axis].set_linewidth(3)
    ax3.spines[axis].set_linewidth(3)


ax1.set_ylabel("Egg to Wandering Survivorship")
ax2.set_ylabel("Egg to Wandering Survivorship")
ax3.set_ylabel("Egg to Wandering Survivorship")



############ mWander ##########################################################


# Height

fig4, ax4 = plt.subplots()

sns.boxplot(ax=ax4, data = Total_Data, x = 'Height', y = 'mWander', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'lightcyan', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
             'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax4, data = Total_Data, x = 'Height', y = 'mWander', marker = 'o', edgecolor = 'darkcyan', facecolor = 'lightcyan', size = 6, alpha = 0.5, linewidth = 1)

# Eggs

fig5, ax5 = plt.subplots()

sns.boxplot(ax=ax5, data = Total_Data, x = 'Eggs', y = 'mWander', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'papayawhip', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'royalblue', 
             'markeredgecolor': 'royalblue', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax5, data = Total_Data, x = 'Eggs', y = 'mWander', marker = 'o', edgecolor = 'saddlebrown', facecolor = 'papayawhip', size = 6, alpha = 0.5, linewidth = 1)


# SA

fig6, ax6 = plt.subplots()

sns.boxplot(ax=ax6, data = Total_Data, x = 'SA', y = 'mWander', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'mintcream', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'crimson', 
             'markeredgecolor': 'crimson', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax6, data = Total_Data, x = 'SA', y = 'mWander', marker = 'o', edgecolor = 'darkgreen', facecolor = 'mintcream', size = 6, alpha = 0.5, linewidth = 1)


for axis in ['left', 'bottom']:
    ax4.spines[axis].set_linewidth(3)
    ax5.spines[axis].set_linewidth(3)
    ax6.spines[axis].set_linewidth(3)


ax4.set_ylabel("Time to Wandering (hrs)")
ax5.set_ylabel("Time to Wandering (hrs)")
ax6.set_ylabel("Time to Wandering (hrs)")


############ mMass ##########################################################


# Height

fig7, ax7 = plt.subplots()

sns.boxplot(ax=ax7, data = Total_Data, x = 'Height', y = 'mMass', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'lightcyan', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
             'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax7, data = Total_Data, x = 'Height', y = 'mMass', marker = 'o', edgecolor = 'darkcyan', facecolor = 'lightcyan', size = 6, alpha = 0.5, linewidth = 1)

# Eggs

fig8, ax8 = plt.subplots()

sns.boxplot(ax=ax8, data = Total_Data, x = 'Eggs', y = 'mMass', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'papayawhip', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'royalblue', 
             'markeredgecolor': 'royalblue', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax8, data = Total_Data, x = 'Eggs', y = 'mMass', marker = 'o', edgecolor = 'saddlebrown', facecolor = 'papayawhip', size = 6, alpha = 0.5, linewidth = 1)


# SA

fig9, ax9 = plt.subplots()

sns.boxplot(ax=ax9, data = Total_Data, x = 'SA', y = 'mMass', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'mintcream', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'crimson', 
             'markeredgecolor': 'crimson', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax9, data = Total_Data, x = 'SA', y = 'mMass', marker = 'o', edgecolor = 'darkgreen', facecolor = 'mintcream', size = 6, alpha = 0.5, linewidth = 1)


for axis in ['left', 'bottom']:
    ax7.spines[axis].set_linewidth(3)
    ax8.spines[axis].set_linewidth(3)
    ax9.spines[axis].set_linewidth(3)


ax7.set_ylabel("Mass at Wandering (ug)")
ax8.set_ylabel("Mass at Wandering (ug)")
ax9.set_ylabel("Mass at Wandering (ug)")


############ vDev ##########################################################


# Height

fig10, ax10 = plt.subplots()

sns.boxplot(ax=ax10, data = Total_Data, x = 'Height', y = 'vWander', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'lightcyan', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
             'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax10, data = Total_Data, x = 'Height', y = 'vWander', marker = 'o', edgecolor = 'darkcyan', facecolor = 'lightcyan', size = 6, alpha = 0.5, linewidth = 1)

# Eggs

fig11, ax11 = plt.subplots()

sns.boxplot(ax=ax11, data = Total_Data, x = 'Eggs', y = 'vWander', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'papayawhip', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'royalblue', 
             'markeredgecolor': 'royalblue', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax11, data = Total_Data, x = 'Eggs', y = 'vWander', marker = 'o', edgecolor = 'saddlebrown', facecolor = 'papayawhip', size = 6, alpha = 0.5, linewidth = 1)


# SA

fig12, ax12 = plt.subplots()

sns.boxplot(ax=ax12, data = Total_Data, x = 'SA', y = 'vWander', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'mintcream', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'crimson', 
             'markeredgecolor': 'crimson', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax12, data = Total_Data, x = 'SA', y = 'vWander', marker = 'o', edgecolor = 'darkgreen', facecolor = 'mintcream', size = 6, alpha = 0.5, linewidth = 1)


for axis in ['left', 'bottom']:
    ax10.spines[axis].set_linewidth(3)
    ax11.spines[axis].set_linewidth(3)
    ax12.spines[axis].set_linewidth(3)


ax10.set_ylabel("Variance Time to Wandering")
ax11.set_ylabel("Variance Time to Wandering")
ax12.set_ylabel("Variance Time to Wandering")

############ vMass ##########################################################


# Height

fig13, ax13 = plt.subplots()

sns.boxplot(ax=ax13, data = Total_Data, x = 'Height', y = 'vMass', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'lightcyan', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
             'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax13, data = Total_Data, x = 'Height', y = 'vMass', marker = 'o', edgecolor = 'darkcyan', facecolor = 'lightcyan', size = 6, alpha = 0.5, linewidth = 1)

# Eggs

fig14, ax14 = plt.subplots()

sns.boxplot(ax=ax14, data = Total_Data, x = 'Eggs', y = 'vMass', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'papayawhip', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'royalblue', 
             'markeredgecolor': 'royalblue', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax14, data = Total_Data, x = 'Eggs', y = 'vMass', marker = 'o', edgecolor = 'saddlebrown', facecolor = 'papayawhip', size = 6, alpha = 0.5, linewidth = 1)


# SA

fig15, ax15 = plt.subplots()

sns.boxplot(ax=ax15, data = Total_Data, x = 'SA', y = 'vMass', 
            showmeans = True, width = 0.65,
            boxprops={"facecolor": 'mintcream', 'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'crimson', 
             'markeredgecolor': 'crimson', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : None},
capwidths = 0.45, zorder = 3)

sns.stripplot(ax=ax15, data = Total_Data, x = 'SA', y = 'vMass', marker = 'o', edgecolor = 'darkgreen', facecolor = 'mintcream', size = 6, alpha = 0.5, linewidth = 1)


for axis in ['left', 'bottom']:
    ax13.spines[axis].set_linewidth(3)
    ax14.spines[axis].set_linewidth(3)
    ax15.spines[axis].set_linewidth(3)


ax13.set_ylabel("Variance Dry Mass")
ax14.set_ylabel("Variance Dry Mass")
ax15.set_ylabel("Variance Dry Mass")


# fig1.savefig('Results/Plots/SurvMainEffHeight.png', dpi=300)

# fig2.savefig('Results/Plots/SurvMainEffEggs.png', dpi=300)

# fig3.savefig('Results/Plots/SurvMainEffSA.png', dpi=300)

# fig4.savefig('Results/Plots/mDevMainEffHeight.png', dpi=300)

# fig5.savefig('Results/Plots/mDevMainEffEggs.png', dpi=300)

# fig6.savefig('Results/Plots/mDevMainEffSA.png', dpi=300)

# fig7.savefig('Results/Plots/mMassMainEffHeight.png', dpi=300)

# fig8.savefig('Results/Plots/mMassMainEffEggs.png', dpi=300)

# fig9.savefig('Results/Plots/mMassMainEffSA.png', dpi=300)

# fig10.savefig('Results/Plots/vDevMainEffHeight.png', dpi=300)

# fig11.savefig('Results/Plots/vDevMainEffEggs.png', dpi=300)

# fig12.savefig('Results/Plots/vDevMainEffSA.png', dpi=300)

# fig13.savefig('Results/Plots/vMassMainEffHeight.png', dpi=300)

# fig14.savefig('Results/Plots/vMassMainEffEggs.png', dpi=300)

# fig15.savefig('Results/Plots/vMassMainEffSA.png', dpi=300)


