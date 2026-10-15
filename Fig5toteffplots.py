'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the survivorship and mean time to wandering plots at various egg number and food volume combinations, each at a "deep" and "shallow" variant, at a total density of 200 eggs/mL food but at varying effective densities (see Manuscript/chapter 6 in thesis), under the expanded model.

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Total_Data = pd.read_excel('Results/Compiled_Total30.xlsx', sheet_name = 'TotalData')


SAInc200 = Total_Data[(Total_Data['Height'] == 5) &
                              (Total_Data['TotDens'] == 200)]

SurvSAInc200Mean = pd.DataFrame(SAInc200.groupby('SA')['Surv'].mean())
mWanderSAInc200Mean = pd.DataFrame(SAInc200.groupby('SA')['mWander'].mean())
vWanderSAInc200Mean = pd.DataFrame(SAInc200.groupby('SA')['vWander'].mean())

xaxis = np.array(SAInc200.groupby('SA')['FoodVol'].mean())

HeightInc200 = Total_Data[(Total_Data['SA'] == 200) &
                              (Total_Data['TotDens'] == 200)]

SurvHeightInc200Mean = pd.DataFrame(HeightInc200.groupby('Height')['Surv'].mean())
mWanderHeightInc200Mean = pd.DataFrame(HeightInc200.groupby('Height')['mWander'].mean())
vWanderHeightInc200Mean = pd.DataFrame(HeightInc200.groupby('Height')['vWander'].mean())

testX = np.array(HeightInc200.groupby('Height')['FoodVol'].mean())

assert np.all(xaxis == testX)

xaxiseggs = np.array(SAInc200.groupby('SA')['Eggs'].mean())

xlabels = []

for x in range(len(xaxis)):
    a = str(int(xaxiseggs[x])) + ' e\n'+ str(xaxis[x]/1000) + ' mL'
    xlabels.append(a)

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



############## Survivorship ##################################################

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()


for axis in ['left', 'bottom']:
    ax1.spines[axis].set_linewidth(2)
    ax2.spines[axis].set_linewidth(2)
    ax3.spines[axis].set_linewidth(2)

sns.lineplot(ax = ax1, data = SurvSAInc200Mean, x = xaxis, y = 'Surv', 
             color = 'lightcoral', linewidth = 3, alpha = 0.8)

sns.lineplot(ax = ax1, data = SurvHeightInc200Mean, x = xaxis, y = 'Surv', 
             color = 'lightsteelblue', linewidth = 3, alpha = 0.8)


sns.scatterplot(ax = ax1, data = SAInc200, x = 'FoodVol', y = 'Surv', s = 150, marker = 'o', facecolor = 'lightcoral', edgecolor = 'firebrick', alpha = 0.6)
        
sns.scatterplot(ax = ax1, data = HeightInc200, x = 'FoodVol', y = 'Surv', s = 150, marker = 'o', facecolor = 'lightsteelblue', edgecolor = 'navy', alpha = 0.6)

sns.scatterplot(ax = ax1, data = SurvSAInc200Mean, x = xaxis, y = 'Surv', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder = 2)

sns.scatterplot(ax = ax1, data = SurvHeightInc200Mean, x = xaxis, y = 'Surv', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder = 2)


ax1.set_ylim(0, 0.6)
ax1.set_xticks(xaxis, xlabels)
ax1.set_xlabel('Total Density = 200 e/mL')
ax1.set_ylabel('Survivorship')

# Surv Total Density Regression

sns.scatterplot(ax = ax2, data = Total_Data, x = 'TotDens', y = 'Surv', 
                s = 100, marker = 'o', facecolor = 'plum', 
                edgecolor = 'purple', alpha = 0.9)


ax2.set_ylim(0, 1.1)
ax2.set_xlim(0, 620)
ax2.set_xlabel('Total Density')
ax2.set_ylabel('Survivorship')

# Surv Effective Density Regression

sns.scatterplot(ax = ax3, data = Total_Data, x = 'EffDens', y = 'Surv', 
                s = 100, marker = 'o', facecolor = 'lemonchiffon', 
                edgecolor = 'gold', alpha = 0.9)


ax3.set_ylim(0, 1.1)
ax3.set_xlim(0, 620)
ax3.set_xlabel('Effective Density')
ax3.set_ylabel('Survivorship')


########### Mean Wandering Time ############################################

fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
fig6, ax6 = plt.subplots()


for axis in ['left', 'bottom']:
    ax4.spines[axis].set_linewidth(2)
    ax5.spines[axis].set_linewidth(2)
    ax6.spines[axis].set_linewidth(2)
    

sns.lineplot(ax = ax4, data = mWanderSAInc200Mean, x = xaxis, y = 'mWander', 
             color = 'lightcoral', linewidth = 3, alpha = 0.8)

sns.lineplot(ax = ax4, data = mWanderHeightInc200Mean, x = xaxis, y = 'mWander', 
             color = 'lightsteelblue', linewidth = 3, alpha = 0.8)


sns.scatterplot(ax = ax4, data = SAInc200, x = 'FoodVol', y = 'mWander', s = 150, marker = 'o', facecolor = 'lightcoral', edgecolor = 'firebrick', alpha = 0.6)
        
sns.scatterplot(ax = ax4, data = HeightInc200, x = 'FoodVol', y = 'mWander', s = 150, marker = 'o', facecolor = 'lightsteelblue', edgecolor = 'navy', alpha = 0.6)

sns.scatterplot(ax = ax4, data = mWanderSAInc200Mean, x = xaxis, y = 'mWander', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder = 2)

sns.scatterplot(ax = ax4, data = mWanderHeightInc200Mean, x = xaxis, y = 'mWander', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder=2)


# ax4.set_ylim(0, 0.6)
ax4.set_xticks(xaxis, xlabels)
ax4.set_xlabel('Total Density = 200 e/mL')
ax4.set_ylabel('Mean Time to Wandering (hrs)')

# mWander Total Density Regression

sns.scatterplot(ax = ax5, data = Total_Data, x = 'TotDens', y = 'mWander', 
                s = 100, marker = 'o', facecolor = 'plum', 
                edgecolor = 'purple', alpha = 0.9)


# ax5.set_ylim(0, 1.1)
ax5.set_xlim(0, 620)
ax5.set_xlabel('Total Density')
ax5.set_ylabel('Mean Time to Wandering (hrs)')

# mWander Effective Density Regression

sns.scatterplot(ax = ax6, data = Total_Data, x = 'EffDens', y = 'mWander', 
                s = 100, marker = 'o', facecolor = 'lemonchiffon', 
                edgecolor = 'gold', alpha = 0.9)


# ax6.set_ylim(0, 1.1)
ax6.set_xlim(0, 620)
ax6.set_xlabel('Effective Density')
ax6.set_ylabel('Mean Time to Wandering (hrs)')



#         # Variance Wandering Time #########################################

fig7, ax7 = plt.subplots()
fig8, ax8 = plt.subplots()
fig9, ax9 = plt.subplots()


for axis in ['left', 'bottom']:
    ax7.spines[axis].set_linewidth(2)
    ax8.spines[axis].set_linewidth(2)
    ax9.spines[axis].set_linewidth(2)

sns.lineplot(ax = ax7, data = vWanderSAInc200Mean, x = xaxis, y = 'vWander', 
             color = 'lightcoral', linewidth = 3, alpha = 0.8)

sns.lineplot(ax = ax7, data = vWanderHeightInc200Mean, x = xaxis, y = 'vWander', 
             color = 'lightsteelblue', linewidth = 3, alpha = 0.8)


sns.scatterplot(ax = ax7, data = SAInc200, x = 'FoodVol', y = 'vWander', s = 150, marker = 'o', facecolor = 'lightcoral', edgecolor = 'firebrick', alpha = 0.6)
        
sns.scatterplot(ax = ax7, data = HeightInc200, x = 'FoodVol', y = 'vWander', s = 150, marker = 'o', facecolor = 'lightsteelblue', edgecolor = 'navy', alpha = 0.6)

sns.scatterplot(ax = ax7, data = vWanderSAInc200Mean, x = xaxis, y = 'vWander', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder = 2)

sns.scatterplot(ax = ax7, data = vWanderHeightInc200Mean, x = xaxis, y = 'vWander', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder=2)


# ax7.set_ylim(0, 0.6)
ax7.set_xticks(xaxis, xlabels)
ax7.set_xlabel('Total Density = 200 e/mL')
ax7.set_ylabel('Variance Time to Wandering (hrs^2)')

# vWander Total Density Regression

sns.scatterplot(ax = ax8, data = Total_Data, x = 'TotDens', y = 'vWander', 
                s = 100, marker = 'o', facecolor = 'plum', 
                edgecolor = 'purple', alpha = 0.9)


# ax8.set_ylim(0, 1.1)
ax8.set_xlim(0, 620)
ax8.set_xlabel('Total Density')
ax8.set_ylabel('Variance Time to Wandering (hrs^2)')


# vWander Effective Density Regression

sns.scatterplot(ax = ax9, data = Total_Data, x = 'EffDens', y = 'vWander', 
                s = 100, marker = 'o', facecolor = 'lemonchiffon', 
                edgecolor = 'gold', alpha = 0.9)


# ax9.set_ylim(0, 1.1)
ax9.set_xlim(0, 620)
ax9.set_xlabel('Effective Density')
ax9.set_ylabel('Variance Time to Wandering (hrs^2)')
        



fig1.savefig('Results/Plots/SurvTotEffComp.png', dpi=300)

fig2.savefig('Results/Plots/SurvTotReg.png', dpi=300)

fig3.savefig('Results/Plots/SurvEffReg.png', dpi=300)


fig4.savefig('Results/Plots/mWanderTotEffComp.png', dpi=300)

fig5.savefig('Results/Plots/mWanderTotReg.png', dpi=300)

fig6.savefig('Results/Plots/mWanderEffReg.png', dpi=300)


fig7.savefig('Results/Plots/vWanderTotEffComp.png', dpi=300)

fig8.savefig('Results/Plots/vWanderTotReg.png', dpi=300)

fig9.savefig('Results/Plots/vWanderEffReg.png', dpi=300)
