'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the plots for the outcomes of crowding with increasing egg number at 2 mL food. This uses the base model with effects of waste included.
The outcomes of crowding are:
    a) Egg to wandering survivorship
    b) Time to wandering
    c) Mass at wandering
    

NOTE: Please change the required directories for saving/reading data!!!
'''


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

from Culture_class import Culture
from Traits import TraitGen

Runs = 10

Surface_area = np.zeros(Runs, dtype = int) + 400
Height = np.zeros(Runs, dtype = int) + 5
Diffuse = np.zeros(Runs, dtype = bool)
W_band = np.zeros(Runs) + 0.01
Saturate = np.zeros(Runs) + 0.045


Eggs = np.arange(70, (70*Runs)+1, 70)
Time = 1200
Conditions = np.zeros((Runs, 2)) + [0, 2]


ID = np.ones(Runs, dtype = int)

HT_m = np.zeros(Runs) + 20
HT_v = np.zeros(Runs) + 0.01

EL_m = np.zeros(Runs) + 0.500
EL_v = np.zeros(Runs) + 0.05

EW_m = np.zeros(Runs) + 0.180
EW_v = np.zeros(Runs) + 0.05

BR_start_m = np.zeros(Runs) + 3000
BR_start_v = np.zeros(Runs) + 0.05

BR_inf_m = np.zeros(Runs) + 1.05
BR_inf_v = np.zeros(Runs) + 0.05

BR_plast_m = np.zeros(Runs) + 1
BR_plast_v = np.zeros(Runs) + 0.05

Eff_larv_m = np.zeros(Runs) + 0.3
Eff_larv_v = np.zeros(Runs) + 0.05

Eff_var_m = np.zeros(Runs) + 0.05
Eff_var_v = np.zeros(Runs) + 0.05

MC_m = np.zeros(Runs) + 180
MC_v = np.zeros(Runs) + 0.05

WT_m = np.zeros(Runs) + 0.095
WT_v = np.zeros(Runs) + 0.1

Dig_m = np.zeros(Runs) + 1.5
Dig_v = np.zeros(Runs) + 0.05

calibrated_min_crit = np.zeros(Runs) + 180
Post_crit_lim = np.zeros(Runs, dtype = int) +  36
Waste_conversion = np.zeros(Runs) + 0.025
BS_initial = np.zeros(Runs) + 0.00007
BS_final_ratio = np.zeros(Runs) + 0.5

StartSA = np.zeros(Runs) + 0.015
GrowSA = np.zeros(Runs) + 0.002
Excr_timer = np.zeros(Runs, dtype = int) + 1


Culture_array = np.ndarray(Runs, dtype=object)

Trait_array = np.ndarray(Runs, dtype = object)

Surv = np.zeros(Runs)

Dev = np.ndarray(Runs, dtype = object)
MeanDev = np.zeros(Runs)
VarDev = np.zeros(Runs)

FinalMass = np.ndarray(Runs, dtype = object)
MeanMass = np.zeros(Runs)
VarMass = np.zeros(Runs)

xticklab = np.ndarray(Runs, dtype = object)



for r in range(Runs):
    print('executing: Run', r)
    
    Culture_array[r] = Culture(
        Surface_area=Surface_area[r],
        Height=Height[r], 
        Diffuse=Diffuse[r],
        W_band=W_band[r],
        Saturate = Saturate[r])
    
    Trait_array[r] = TraitGen(
        Eggs[r], ID = ID[r],
        HT_m = HT_m[r], HT_v = HT_v[r],
        EL_m = EL_m[r], EL_v = EL_v[r],
        EW_m = EW_m[r], EW_v = EW_v[r],
        BR_start_m = BR_start_m[r],
        BR_start_v = BR_start_v[r],
        BR_inf_m = BR_inf_m[r], 
        BR_inf_v = BR_inf_v[r],
        BR_plast_m = BR_plast_m[r],
        BR_plast_v = BR_plast_v[r],
        Eff_larv_m = Eff_larv_m[r],
        Eff_larv_v = Eff_larv_v[r],
        Eff_var_m = Eff_var_m[r], 
        Eff_var_v = Eff_var_v[r],
        MC_m = MC_m[r], MC_v = MC_v[r],
        WT_m = WT_m[r], WT_v = WT_v[r],
        Dig_m = Dig_m[r], Dig_v = Dig_v[r])
    
    Culture_array[r].Add_eggs(
        Eggs[r], Trait_array[r],
        calibrated_min_crit = calibrated_min_crit[r],
        Post_crit_lim = Post_crit_lim[r],
        Waste_conversion = Waste_conversion[r],
        BS_initial = BS_initial[r],
        BS_final_ratio = BS_final_ratio[r])
    
    Culture_array[r].Culture_run(Time, 
                Conditions = Conditions[r, :],
                StartSA = StartSA[r],
                GrowSA = GrowSA[r], 
                Excrete_timer = Excr_timer[r])
    
    Surv[r] = Culture_array[r].Survivorship
    Dev[r] = Culture_array[r].Dev_time[Culture_array[r].Dev_time>0]
    
    FinalMass[r] = Culture_array[r].Mass_profile[
        -1, Culture_array[r].Mass_profile[-1, :] > 0]
    xticklab[r] = str(Eggs[r])

    MeanDev[r] = np.mean(Dev[r])
    MeanMass[r] = np.mean(FinalMass[r])
    
    VarDev[r] = np.var(Dev[r])
    VarMass[r] = np.var(FinalMass[r])
    


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

fig1, ax1 = plt.subplots()
ax1.plot(Eggs, Surv, 'ro-')
ax1.set_xticks(Eggs, xticklab)
ax1.set_ylabel("Survivorship")
ax1.set_xlabel("Egg Number (Waste ON)")

fig2, ax2 = plt.subplots()
sns.boxplot(ax = ax2, data = Dev, showmeans = True, 
            width = 0.65,
            boxprops={"facecolor": 'lightskyblue', 
                      'edgecolor' : 'black'}, 
            meanprops = {'markerfacecolor' : 'coral', 
                         'markeredgecolor': 'coral', 'markersize' : 6},
            medianprops = {'color' : 'indigo'},
            whiskerprops = {'color' : 'black'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : 'o',
                          'markeredgecolor' : 'black',
                          'markerfacecolor' : 'white',
                          'markersize' : 5},
            capwidths = 0.25)

ax2.set_xticklabels(xticklab)
ax2.set_xlabel("Egg Number (Waste ON)")
ax2.set_ylabel("Egg to Wandering Development Time (hrs)")

fig3, ax3 = plt.subplots()
sns.boxplot(ax = ax3, data = FinalMass, showmeans = True, 
            width = 0.65,
            boxprops={"facecolor": 'floralwhite', 
                      'edgecolor' : 'black'},
            meanprops = {'markerfacecolor' : 'coral', 
                         'markeredgecolor': 'coral', 'markersize' : 6},
            whiskerprops = {'color' : 'black'},
            medianprops = {'color' : 'indigo'},
            capprops = {'color' : 'black'},
            flierprops = {'marker' : 'o',
                          'markeredgecolor' : 'black',
                          'markerfacecolor' : 'white',
                          'markersize' : 5},
            capwidths = 0.25)
ax3.set_xticklabels(xticklab)
ax3.set_xlabel("Egg Number (Waste ON)")
ax3.set_ylabel("Dry Mass at Wandering (ug)")


for axis in ['left', 'bottom']:
    ax1.spines[axis].set_linewidth(2)
    ax2.spines[axis].set_linewidth(2)
    ax3.spines[axis].set_linewidth(2)
    

# fig1.savefig('Results/Plots/WasteCrowdSurv.png', dpi=300)
# fig2.savefig('Results/Plots/WasteCrowdDev.png', dpi=300)
# fig3.savefig('Results/Plots/WasteCrowdMass.png', dpi=300)
