import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Culture_class import Culture
from Traits import TraitGen

Cult3mLShallow = Culture(Surface_area=600, Height=5, Diffuse=True, 
                       W_band=0.01, Saturate = 0.045)


Cult3mLDeep = Culture(Surface_area=200, Height=15, Diffuse=True, 
                       W_band=0.01, Saturate = 0.045)


Eggs = 600
Time = 1500
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

DevShallow = np.log10(Cult3mLShallow.Dev_time)
DevDeep = np.log10(Cult3mLDeep.Dev_time)

MortShallow = np.log10(Cult3mLShallow.Mort_time)
MortDeep = np.log10(Cult3mLDeep.Mort_time)

yLabels = ['HT', 'EL', 'EW', 'BR_strt', 'BR_inf', 'BR_p', 'EffM', 'EffV',
           'MinCrit', 'WasteTol', 'DigF']

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

for i in range(11):
    
    fig1, ax1 = plt.subplots(2, 1, sharex = True)
    
    sns.scatterplot(ax = ax1[0], 
                x = MortShallow[MortShallow>0], 
                y = Trait_array[i+1, MortShallow > 0], 
                marker = 'o', edgecolor = 'crimson', facecolor = 'salmon', 
                alpha = 0.2)
    sns.scatterplot(ax = ax1[0], 
                x = DevShallow[DevShallow>0], 
                y = Trait_array[i+1, DevShallow > 0], 
                marker = 'o', edgecolor = 'deepskyblue', 
                facecolor = 'lightskyblue', alpha = 0.8)
    
    sns.scatterplot(ax = ax1[1], 
                x = MortDeep[MortDeep>0], 
                y = Trait_array[i+1, MortDeep > 0], 
                marker = 'o', edgecolor = 'crimson', facecolor = 'salmon',
                alpha = 0.2)
    sns.scatterplot(ax = ax1[1], 
                x = DevDeep[DevDeep>0], 
                y = Trait_array[i+1, DevDeep > 0], 
                marker = 'o', edgecolor = 'deepskyblue', 
                facecolor = 'lightskyblue', alpha = 0.8)
    
    ax1[0].set_ylabel("Shallow"+yLabels[i])
    ax1[0].set_xlabel("Log 10 Time")
    ax1[1].set_ylabel("Deep" + yLabels[i])
    ax1[1].set_xlabel("Log 10 Time")
    # ax1[1].set_xlim(2, 2.5)
    
    
    fig1b, ax1b = plt.subplots(1, 2, sharey = True)
    
    sns.boxplot(ax = ax1b[0], 
                data = [Trait_array[i+1, DevShallow>0], 
                        Trait_array[i+1, MortShallow>0]], 
                showmeans = True,
                boxprops={'edgecolor' : 'black'}, 
                meanprops = {'markersize' : 8, 'markerfacecolor' : 'lightgreen',
                             'markeredgecolor' : 'darkgreen'},
                medianprops = {'color' : 'indigo'},
                whiskerprops = {'color' : 'black'},
                capprops = {'color' : 'black'},
                flierprops = {'markersize' : 5})
    
    sns.boxplot(ax = ax1b[1], 
                data = [Trait_array[i+1, DevDeep>0], 
                        Trait_array[i+1, MortDeep>0]], 
                showmeans = True,
                boxprops={'edgecolor' : 'black'}, 
                meanprops = {'markersize' : 8, 'markerfacecolor' : 'lightgreen',
                             'markeredgecolor' : 'darkgreen'},
                medianprops = {'color' : 'indigo'},
                whiskerprops = {'color' : 'black'},
                capprops = {'color' : 'black'},
                flierprops = {'markersize' : 5})
    
    ax1b[0].set_xticklabels(['ShalSurv', 'ShalMort'])
    ax1b[1].set_xticklabels(['DeepSurv', 'DeepMort'])
    ax1b[0].set_ylabel(yLabels[i])
################# SAVES #####################################################

# fig1a.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/WastePermShallow.png', dpi=300)

# fig1b.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/WastePermDeep.png', dpi=300)

# fig2a.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/DigDepthShallow.png', dpi=300)

# fig2b.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/DigDepthDeep.png', dpi=300)

# fig3a.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/SAOccShallow.png', dpi=300)

# fig3b.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/SAOccDeep.png', dpi=300)
