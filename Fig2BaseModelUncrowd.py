'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates (single run) the data and the plots for the larval growth profile over time, and boxplots for time to wandering and mass at wandering, under uncrowded conditions, using the BASE model without waste (see Manuscript/chapter 6 in thesis).

Change the plot save directory as required.
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from Culture_class import Culture
from Traits import TraitGen

CultureDemo = Culture(Surface_area=400, Height=15, Diffuse=False, 
                       W_band=0.01, Saturate = 0.045)

Eggs = 70
Time = 150
Conditions = [0, 0]

Trait_array = TraitGen(Eggs, ID = 1, 
                       HT_m = 20, HT_v = 0.01,
                       EL_m = 0.500, EL_v = 0.05,
                       EW_m = 0.180, EW_v = 0.05,
                       BR_start_m = 3000, BR_start_v = 0.05,
                       BR_inf_m = 1.05, BR_inf_v = 0.05,
                       BR_plast_m = 1, BR_plast_v = 0.05,
                       Eff_larv_m = 0.3, Eff_larv_v = 0.05,
                       Eff_var_m = 0.05, Eff_var_v = 0.05,
                       MC_m = 180, MC_v = 0.05,
                       WT_m = 0.095, WT_v = 0.1,
                       Dig_m = 1.5, Dig_v = 0.05)

assert np.all(Trait_array > 0)

CultureDemo.Add_eggs(Eggs, Trait_array, calibrated_min_crit = 180,
                      Post_crit_lim = 36, Waste_conversion = 0.025,
                      BS_initial = 0.00007, BS_final_ratio = 0.5)

CultureDemo.Culture_run(Time, Conditions, 
                         StartSA = 0.015, GrowSA = 0.002, Excrete_timer=1)



Dev = CultureDemo.Dev_time
Final_mass = CultureDemo.Mass_profile[-1]
Mort = CultureDemo.Mort_time


Massarray = CultureDemo.Mass_profile
Mass_mean = np.mean(Massarray, axis=1)
Mass_std = np.std(Massarray, axis=1)


# Font Arial used for manuscript plots

sns.set_theme(style='white', rc = {
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

sns.set_context("notebook", rc={"font.size":10,
                                "axes.titlesize":10,
                                "axes.labelsize":10})

fig, ax = plt.subplots()
ax.plot(np.arange(Time), Mass_mean, 'dodgerblue', linewidth = 1.8)
ax.fill_between(np.arange(Time), Mass_mean + Mass_std, Mass_mean - Mass_std,
                 alpha = 0.4, color = 'dodgerblue')
ax.set_ylabel("Larval Mass (v-ug)")
ax.set_xlabel("Time (v-hrs)")
ax.hlines(180, 0, Time, 'red', linewidth = 1, linestyle = 'dashed')
ax.set_xlim(0, Time)
ax.set_ylim(0, 620)

for axis in ['left', 'bottom']:
    ax.spines[axis].set_linewidth(2)
    



# Dev and Mass distributions
fig2, ax2 = plt.subplots(1, 2)
sns.boxplot(ax = ax2[0], y = Dev[Dev>0], showmeans = True,
            width = 0.65,
            boxprops={"facecolor": 'lightskyblue', 
                      'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
                         'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            capwidths = 0.25)

ax2[0].set_ylabel("Time to Wandering (v-hrs)")

sns.boxplot(ax = ax2[1], y = Final_mass[Final_mass>0], showmeans = True,
            width = 0.65,
            boxprops={"facecolor": 'white', 
                      'edgecolor' : 'black'},
            meanprops = {'markerfacecolor' : 'coral', 
                         'markeredgecolor': 'coral', 'markersize' : 8},
            whiskerprops = {'color' : 'black'},
            medianprops = {'color' : 'indigo'},
            capprops = {'color' : 'black'},
            capwidths = 0.25)

ax2[1].set_ylabel("Mass at Wandering (v-ug)")

for axis in ['left', 'bottom']:
    ax2[0].spines[axis].set_linewidth(2)
    ax2[1].spines[axis].set_linewidth(2)

plt.tight_layout()


# fig.savefig('Results/Plots/BaseUncrowdGrowth.png', dpi=300)
# fig2.savefig('Results/Plots/BaseUncrowdDevMass.png', dpi=300)
