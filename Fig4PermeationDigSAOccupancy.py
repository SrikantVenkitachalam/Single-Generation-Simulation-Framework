'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the data for a single run each of the "deep" and "shallow" variants of the 600 eggs, 3 mL culture type, each at a total density of 200 eggs/mL (see Manuscript/chapter 6 in thesis), using the expanded model.

The following are plotted for the generated data:
    Permeation of waste across 'waste bands'.
    Digging depth given various criteria.
    Surface area occupancy of the food cross-section vs. total larval cross-section surface area.

NOTE: Please change the required directories for saving/reading data!!!
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

from Culture_class import Culture
from Traits import TraitGen

Cult3mLShallow = Culture(Surface_area=600, Height=5, Diffuse=True, 
                       W_band=0.01, Saturate = 0.045)


Cult3mLDeep = Culture(Surface_area=200, Height=15, Diffuse=True, 
                       W_band=0.01, Saturate = 0.045)


Eggs = 600
Time = 1000
Conditions = [1, 2]

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

Cult3mLShallow.Add_eggs(Eggs, Trait_array, calibrated_min_crit = 180,
                      Post_crit_lim = 36, Waste_conversion = 0.025,
                      BS_initial = 0.00007, BS_final_ratio = 0.5)

Cult3mLShallow.Culture_run(Time, Conditions, 
                         StartSA = 0.015, GrowSA = 0.002, Excrete_timer=1)


Cult3mLDeep.Add_eggs(Eggs, Trait_array, calibrated_min_crit = 180,
                      Post_crit_lim = 36, Waste_conversion = 0.025,
                      BS_initial = 0.00007, BS_final_ratio = 0.5)

Cult3mLDeep.Culture_run(Time, Conditions, 
                         StartSA = 0.015, GrowSA = 0.002, Excrete_timer=1)

# Dev = CultureDemo.Dev_time
# Final_mass = CultureDemo.Mass_profile[-1]
# Mort = CultureDemo.Mort_time


# Massarray = CultureDemo.Mass_profile
# Mass_mean = np.mean(Massarray, axis=1)
# Mass_std = np.std(Massarray, axis=1)

########## Shallow ##########################################################

WBprofShallow = Cult3mLShallow.WB_profile

DigprofShallow = Cult3mLShallow.DigLen_profile

DigminShallow = np.zeros(Eggs)
Dig100Shallow = np.zeros(Eggs)
DigmaxShallow = np.zeros(Eggs)

for e in range(Eggs):
    DigminShallow[e] = np.min(DigprofShallow[:, e][DigprofShallow[:, e] > 0])
    Dig100Shallow[e] = DigprofShallow[100, e]
    DigmaxShallow[e] = np.max(DigprofShallow[:, e][DigprofShallow[:, e] > 0])
    
SA_availableShallow = Cult3mLShallow.SA_available
LSA_totalShallow = Cult3mLShallow.L_SA_total


############# Deep ##########################################################

WBprofDeep = Cult3mLDeep.WB_profile

DigprofDeep = Cult3mLDeep.DigLen_profile

DigminDeep = np.zeros(Eggs)
Dig100Deep = np.zeros(Eggs)
DigmaxDeep = np.zeros(Eggs)

for e in range(Eggs):
    DigminDeep[e] = np.min(DigprofDeep[:, e][DigprofDeep[:, e] > 0])
    Dig100Deep[e] = DigprofDeep[100, e]
    DigmaxDeep[e] = np.max(DigprofDeep[:, e][DigprofDeep[:, e] > 0])
    
SA_availableDeep = Cult3mLDeep.SA_available
LSA_totalDeep = Cult3mLDeep.L_SA_total

#############################################################################
######################## PLOTS ##############################################
#############################################################################

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

sns.set_context("notebook", rc={"font.size":10,
                                "axes.titlesize":10,
                                "axes.labelsize":10})

# sns.axes_style(rc = 
#                {'axes.spines.right' : True,
#                 'axes.spines.left' : True,
#                 'axes.spines.top' : True,
#                 'axes.spines.bottom' : True})

# Waste permeation Shallow ###################################################

coltheme = cm.get_cmap('Greens_r', 4096)
newcolors = coltheme(np.linspace(0, 1, 4096))
empty = np.array([(230*16)/4096, (230*16)/4096, (250*16)/4096, 1])
unaccess = np.array([(210*16)/4096, (232*16)/4096, (186*16)/4096, 1])
wband = np.array([(2*16)/4096, (108*16)/4096, (69*16)/4096, 1])
extremewaste = np.array([(255*16)/4096, (1*16)/4096, (1*16)/4096, 1])
newcolors[0:1, :] = empty
newcolors[1:2, :] = unaccess
newcolors[65:4096, :] = extremewaste
# newcolors[2:100, :] = wband
newcmp = ListedColormap(newcolors)

fig1a, ax1a = plt.subplots()
sns.heatmap(ax = ax1a, data = np.transpose(WBprofShallow[0:-1, :]), cmap = newcmp)
ax1a.set_ylabel("Food layer (bottom = 1)")
ax1a.set_xlabel("Time (hrs)")
ax1a.set_xlim(0, 400)
ax1a.set_xticks(np.arange(0, 401, 50), np.arange(0, 401, 50))
ax1a.set_yticks(np.arange(0, 501, step = 100),np.arange(0, 501, step = 100))

ax1a.axhline(y = 0, color = 'k', linewidth = 2)
ax1a.axhline(y = 500, color = 'k', linewidth = 2)
ax1a.axvline(x = 0, color = 'k', linewidth = 2)
ax1a.axvline(x = 400, color = 'k', linewidth = 2)

fig1a.gca().invert_yaxis()
fig1a.suptitle('Shallow')


# Waste permeation Deep ###################################################
coltheme = cm.get_cmap('summer_r', 4096)
newcolors = coltheme(np.linspace(0, 1, 4096))
empty = np.array([(230*16)/4096, (230*16)/4096, (250*16)/4096, 1])
unaccess = np.array([(210*16)/4096, (232*16)/4096, (186*16)/4096, 1])
newcolors[0:1, :] = empty
newcolors[1:400, :] = unaccess
newcmp = ListedColormap(newcolors)

fig1b, ax1b = plt.subplots()
sns.heatmap(ax = ax1b, data = np.transpose(WBprofDeep[0:-1, :]), cmap = newcmp)
ax1b.set_ylabel("Food layer (bottom = 1)")
ax1b.set_xlabel("Time (hrs)")
ax1b.set_xlim(0, 400)
ax1b.set_xticks(np.arange(0, 401, 50), np.arange(0, 401, 50))
ax1b.set_yticks(np.arange(0, 1501, step = 300), np.arange(0, 1501, step = 300))
fig1b.gca().invert_yaxis()

ax1b.axhline(y = 0, color = 'k', linewidth = 2)
ax1b.axhline(y = 1500, color = 'k', linewidth = 2)
ax1b.axvline(x = 0, color = 'k', linewidth = 2)
ax1b.axvline(x = 400, color = 'k', linewidth = 2)

fig1b.suptitle('Deep')



# Digging depth Shallow ######################################################
fig2a, ax2a = plt.subplots()
sns.boxplot(ax = ax2a, data = [DigminShallow, Dig100Shallow, DigmaxShallow], showmeans = True,
            width = 0.65,
            boxprops={"facecolor": 'lightskyblue', 
                      'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
                         'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            capwidths = 0.25)

ax2a.set_xticks([0, 1, 2], ['DigminShallow', 'Dig100Shallow', 'DigmaxShallow'])
ax2a.set_ylabel("Digging depth (mm)")
ax2a.set_ylim(0, 8.2)
ax2a.xaxis.tick_top()
ax2a.spines['top'].set_visible(True)
ax2a.spines['bottom'].set_visible(False)
fig2a.gca().invert_yaxis()

for axis in ['left', 'bottom']:
    ax2a.spines[axis].set_linewidth(2)

fig2a.suptitle('Shallow')


# Digging depth Deep ######################################################
fig2b, ax2b = plt.subplots()
sns.boxplot(ax = ax2b, data = [DigminDeep, Dig100Deep, DigmaxDeep], showmeans = True,
            width = 0.65,
            boxprops={"facecolor": 'lightskyblue', 
                      'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
                         'markeredgecolor': 'coral', 'markersize' : 8},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            capwidths = 0.25)

ax2b.set_xticks([0, 1, 2], ['DigminDeep', 'Dig100Deep', 'DigmaxDeep'])
ax2b.set_ylabel("Digging depth (mm)")
ax2b.set_ylim(0, 8.2)
ax2b.xaxis.tick_top()
ax2b.spines['top'].set_visible(True)
ax2b.spines['bottom'].set_visible(False)
fig2b.gca().invert_yaxis()

for axis in ['left', 'bottom']:
    ax2b.spines[axis].set_linewidth(2)

fig2b.suptitle('Deep')


# SA Occupancy Shallow #######################################################
fig3a, ax3a = plt.subplots()
sns.lineplot(ax = ax3a, x = np.arange(Time), y = SA_availableShallow, color = 'royalblue')
sns.lineplot(ax = ax3a, x = np.arange(Time), y = LSA_totalShallow, color = 'crimson')
ax3a.set_xlim(0, 400)
ax3a.set_ylim(0, 600)
ax3a.set_ylabel("summed surface area (mm^2)")
ax3a.set_xlabel("Time (hrs)")

for axis in ['left', 'bottom']:
    ax3a.spines[axis].set_linewidth(2)

fig3a.suptitle('Shallow')


# SA Occupancy Deep #######################################################
fig3b, ax3b = plt.subplots()
sns.lineplot(ax = ax3b, x = np.arange(Time), y = SA_availableDeep, color = 'royalblue')
sns.lineplot(ax = ax3b, x = np.arange(Time), y = LSA_totalDeep, color = 'crimson')
ax3b.set_xlim(0, 400)
ax3b.set_ylim(0, 200)
ax3b.set_ylabel("summed surface area (mm^2)")
ax3b.set_xlabel("Time (hrs)")

for axis in ['left', 'bottom']:
    ax3b.spines[axis].set_linewidth(2)
    
fig3b.suptitle('Deep')


################# SAVES #####################################################

# fig1a.savefig('/Results/Plots/WastePermShallow.png', dpi=300)

# fig1b.savefig('/Results/Plots/WastePermDeep.png', dpi=300)

# fig2a.savefig('/Results/Plots/DigDepthShallow.png', dpi=300)

# fig2b.savefig('/Results/Plots/DigDepthDeep.png', dpi=300)

# fig3a.savefig('/Results/Plots/SAOccShallow.png', dpi=300)

# fig3b.savefig('/Results/Plots/SAOccDeep.png', dpi=300)

