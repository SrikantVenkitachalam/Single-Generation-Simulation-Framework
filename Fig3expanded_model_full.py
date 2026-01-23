'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the plots from the data for the full framework design (see Manuscript/chapter 6 in thesis), under the expanded model.

The plots are generated for the following outcomes of crowding:
    a) Egg to wandering survivorship
    b) Mean Time to wandering
    c) Mean Mass at wandering
    d) Variance in Time to wandering
    e) Variance in Mass at wandering
    

NOTE: Please change the required directories for saving/reading data!!!
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Total_Data = pd.read_excel('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Compiled_Total30.xlsx', sheet_name = 'TotalData')


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

fig1, ax1 = plt.subplots(nrows=3, ncols=3, sharex = 'col', sharey = True,
                         figsize = (12, 8),
                         gridspec_kw= {'hspace': 0.18, 'wspace': 0.05})


fig2, ax2 = plt.subplots(nrows=3, ncols=3, sharex = 'col', sharey = True,
                          figsize = (12, 8),
                          gridspec_kw= {'hspace': 0.18, 'wspace': 0.05})


fig3, ax3 = plt.subplots(nrows=3, ncols=3, sharex = 'col', sharey = True,
                          figsize = (12, 8),
                          gridspec_kw= {'hspace': 0.18, 'wspace': 0.05})


fig4, ax4 = plt.subplots(nrows=3, ncols=3, sharex = 'col', sharey = True,
                          figsize = (12, 8),
                          gridspec_kw= {'hspace': 0.18, 'wspace': 0.05})


fig5, ax5 = plt.subplots(nrows=3, ncols=3, sharex = 'col', sharey = True,
                          figsize = (12, 8),
                          gridspec_kw= {'hspace': 0.18, 'wspace': 0.05})

Heights = [15, 10, 5]
SA = [200, 400, 600]

for i in range(len(Heights)):
    for j in range(len(SA)):
        
        DataTemp = Total_Data[(Total_Data['Height'] == Heights[i]) &
                              (Total_Data['SA'] == SA[j])]
        
        # Survivorship ##################################################
        TempMeanSurv = pd.DataFrame(DataTemp.groupby('Eggs')['Surv'].mean())
        
        sns.lineplot(ax=ax1[i, j], data= TempMeanSurv, x = 'Eggs', y = 'Surv', 
                     color = 'coral', linewidth = 3, alpha = 0.8)
        
        sns.scatterplot(ax=ax1[i, j], data= DataTemp, x = 'Eggs', y = 'Surv', s = 150, marker = 'o', facecolor = 'coral', edgecolor = 'maroon', alpha = 0.6)
        
        sns.scatterplot(ax=ax1[i, j], data= TempMeanSurv, x = 'Eggs', y = 'Surv', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder = 2)
        
        
        ax1[i, j].set_ylim(0, 1.1)
        ax1[i, j].set_xticks([200, 400, 600])
        ax1[i, j].set_title("SA : " + str(SA[j]) + " mm^2; Height : " + 
                            str(Heights[i]) + " mm")
        ax1[i, j].set_xlabel(None)
        ax1[i, j].set_ylabel(None)
        
        ax1[i, j].grid(axis='y', c = 'grey', alpha = 0.5)
        
        
        # Mean Wandering Time ############################################
        
        TempMeanMDev = pd.DataFrame(DataTemp.groupby('Eggs')['mWander'].mean())
        
        sns.lineplot(ax=ax2[i, j], data= TempMeanMDev, x = 'Eggs', y = 'mWander', color = 'lightskyblue', linewidth = 3, alpha = 0.8)
        
        sns.scatterplot(ax=ax2[i, j], data= DataTemp, x = 'Eggs', y = 'mWander', marker = 'o', facecolor = 'lightskyblue', edgecolor = 'dodgerblue', s = 150, alpha = 0.6)
        
        sns.scatterplot(ax=ax2[i, j], data= TempMeanMDev, x = 'Eggs', y = 'mWander', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder=2)
        
        ax2[i, j].set_ylim(100, 310)
        ax2[i, j].set_xticks([200, 400, 600])
        ax2[i, j].set_title("SA : " + str(SA[j]) + " mm^2; Height : " + 
                            str(Heights[i]) + " mm")
        ax2[i, j].set_xlabel(None)
        ax2[i, j].set_ylabel(None)
        
        ax2[i, j].grid(axis='y', c = 'grey', alpha = 0.5)
        
        # Variance Wandering Time #########################################
        TempMVarDev = pd.DataFrame(DataTemp.groupby('Eggs')['vWander'].mean())
        
        sns.lineplot(ax=ax3[i, j], data= TempMVarDev, x = 'Eggs', y = 'vWander', color = 'paleturquoise', linewidth = 3, alpha = 0.8)
        
        sns.scatterplot(ax=ax3[i, j], data= DataTemp, x = 'Eggs', y = 'vWander', marker = 'o', facecolor = 'paleturquoise', edgecolor = 'turquoise', s = 150, alpha = 0.6)
        
        sns.scatterplot(ax=ax3[i, j], data= TempMVarDev, x = 'Eggs', y = 'vWander', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder=2)
        
        ax3[i, j].set_ylim(0, 82000)
        ax3[i, j].set_xticks([200, 400, 600])
        ax3[i, j].set_title("SA : " + str(SA[j]) + " mm^2; Height : " + 
                            str(Heights[i]) + " mm")
        ax3[i, j].set_xlabel(None)
        ax3[i, j].set_ylabel(None)
        
        ax3[i, j].grid(axis='y', c = 'grey', alpha = 0.5)
        
        # Mean Dry Mass ############################################
        TempMeanMMass = pd.DataFrame(DataTemp.groupby('Eggs')['mMass'].mean())
        
        sns.lineplot(ax=ax4[i, j], data= TempMeanMMass, x = 'Eggs', y = 'mMass', color = 'plum', linewidth = 3, alpha = 0.8)
        
        sns.scatterplot(ax=ax4[i, j], data= DataTemp, x = 'Eggs', y = 'mMass', marker = 'o', facecolor = 'plum', edgecolor = 'indigo', s = 150, alpha = 0.6)
        
        sns.scatterplot(ax=ax4[i, j], data= TempMeanMMass, x = 'Eggs', y = 'mMass', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder=2)
        
        ax4[i, j].set_ylim(200, 600)
        ax4[i, j].set_xticks([200, 400, 600])
        ax4[i, j].set_title("SA : " + str(SA[j]) + " mm^2; Height : " + 
                            str(Heights[i]) + " mm")
        ax4[i, j].set_xlabel(None)
        ax4[i, j].set_ylabel(None)
        
        ax4[i, j].grid(axis='y', c = 'grey', alpha = 0.5)
        
        # Variance Dry Mass #########################################
        TempMVarMass = pd.DataFrame(DataTemp.groupby('Eggs')['vMass'].mean())
        
        sns.lineplot(ax=ax5[i, j], data= TempMVarMass, x = 'Eggs', y = 'vMass', color = 'navajowhite', linewidth = 3, alpha = 0.8)
        
        sns.scatterplot(ax=ax5[i, j], data= DataTemp, x = 'Eggs', y = 'vMass', marker = 'o', facecolor = 'navajowhite', edgecolor = 'darkorange', s = 150, alpha = 0.6)
        
        sns.scatterplot(ax=ax5[i, j], data= TempMVarMass, x = 'Eggs', y = 'vMass', s = 250, marker = '_', facecolor = 'black', linewidth = 3, zorder=2)
        
        ax5[i, j].set_ylim(0, 26000)
        ax5[i, j].set_xticks([200, 400, 600])
        ax5[i, j].set_title("SA : " + str(SA[j]) + " mm^2; Height : " + 
                            str(Heights[i]) + " mm")
        ax5[i, j].set_xlabel(None)
        ax5[i, j].set_ylabel(None)
        
        ax5[i, j].grid(axis='y', c = 'grey', alpha = 0.5)
        
        for axis in ['left', 'bottom']:
            ax1[i, j].spines[axis].set_linewidth(3)
            ax2[i, j].spines[axis].set_linewidth(3)
            ax3[i, j].spines[axis].set_linewidth(3)
            ax4[i, j].spines[axis].set_linewidth(3)
            ax5[i, j].spines[axis].set_linewidth(3)



ax1[1, 0].set_ylabel("Egg to Wandering Survivorship")

ax2[1, 0].set_ylabel("Mean Time to Wandering (hrs)")

ax3[1, 0].set_ylabel("Variance Time to Wandering (hrs^2)")

ax4[1, 0].set_ylabel("Mean Dry Mass (ug)")

ax5[1, 0].set_ylabel("Variance Dry Mass (ug^2)")
# fig1.tight_layout()


# fig1.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/SurvFullFrame.png', dpi=300)

# fig2.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/MDevFullFrame.png', dpi=300)

# fig3.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/VDevFullFrame.png', dpi=300)

# fig4.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/MMassFullFrame.png', dpi=300)

# fig5.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/VMassFullFrame.png', dpi=300)




