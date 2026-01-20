'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the trait plots for the 600 eggs, 3mL combination under the 'deep' or 'shallow' type of culture, using the expanded model (see Manuscript/chapter 6 in thesis, supplementary section: final figure). The code that is commented out generates the data, the code that runs uncommented reads and generates the required plots.

NOTE: Please change the required directories for saving/reading data!!!
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from Culture_class import Culture
from Traits import TraitGen


# Reps = 30


# Eggs = 600
# Time = 1500
# Conditions = [1, 2]


# Trait_array = np.zeros((Reps, 12, Eggs))

# Trait_mean_Shallow_Surv = np.zeros((Reps, 12))
# Trait_mean_Shallow_Mort = np.zeros((Reps, 12))

# Trait_mean_Deep_Surv = np.zeros((Reps, 12))
# Trait_mean_Deep_Mort = np.zeros((Reps, 12))

# for r in range(Reps):
#     print(r)
    
#     Cult3mLShallow = Culture(Surface_area=600, Height=5, Diffuse=True, 
#                            W_band=0.01, Saturate = 0.045)
    
    
#     Cult3mLDeep = Culture(Surface_area=200, Height=15, Diffuse=True, 
#                            W_band=0.01, Saturate = 0.045)
    
    
    
#     Trait_array[r, :] = TraitGen(Eggs, ID = 1, 
#                            HT_m = 20, HT_v = 0.01,
#                            EL_m = 0.500, EL_v = 0.05,
#                            EW_m = 0.180, EW_v = 0.05,
#                            BR_start_m = 3000, BR_start_v = 0.05,
#                            BR_inf_m = 1.05, BR_inf_v = 0.05,
#                            BR_plast_m = 1, BR_plast_v = 0.05,
#                            Eff_larv_m = 0.3, Eff_larv_v = 0.05,
#                            Eff_var_m = 0.05, Eff_var_v = 0.05,
#                            MC_m = 180, MC_v = 0.05,
#                            WT_m = 0.095, WT_v = 0.1,
#                            Dig_m = 1.5, Dig_v = 0.05)
    
#     assert np.all(Trait_array[r] > 0)
    
#     Cult3mLShallow.Add_eggs(Eggs, Trait_array[r], calibrated_min_crit = 180,
#                           Post_crit_lim = 36, Waste_conversion = 0.025,
#                           BS_initial = 0.00007, BS_final_ratio = 0.5)
    
#     Cult3mLShallow.Culture_run(Time, Conditions, 
#                              StartSA = 0.015, GrowSA = 0.002, Excrete_timer=1)
    
    
#     Cult3mLDeep.Add_eggs(Eggs, Trait_array[r], calibrated_min_crit = 180,
#                           Post_crit_lim = 36, Waste_conversion = 0.025,
#                           BS_initial = 0.00007, BS_final_ratio = 0.5)
    
#     Cult3mLDeep.Culture_run(Time, Conditions, 
#                              StartSA = 0.015, GrowSA = 0.002, Excrete_timer=1)
    
#     assert len(Trait_array[r, :, 0]) == 12
    
#     for t in range(12):
#         Trait_mean_Shallow_Surv[r, t] = np.mean(Trait_array[r, t, 
#                                     (Cult3mLShallow.Dev_time > 0)])
#         Trait_mean_Shallow_Mort[r, t] = np.mean(Trait_array[r, t, 
#                                     (Cult3mLShallow.Mort_time > 0)])
        
        
#         Trait_mean_Deep_Surv[r, t] = np.mean(Trait_array[r, t, 
#                                     (Cult3mLDeep.Dev_time > 0)])
#         Trait_mean_Deep_Mort[r, t] = np.mean(Trait_array[r, t, 
#                                     (Cult3mLDeep.Mort_time > 0)])
        
#     if r != Reps-1:
#         Cult3mLShallow = None
#         Cult3mLDeep = None



#############################################################################
######################## PLOTS ##############################################
#############################################################################




# np.save("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\Cult3mLShallow.npy", Cult3mLShallow)

# np.save("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\Cult3mLDeep.npy", Cult3mLDeep)

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanShallowSurv.csv", Trait_mean_Shallow_Surv,
#            delimiter=",")

Trait_mean_Shallow_Surv = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanShallowSurv.csv",
                                     delimiter=",")

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanShallowMort.csv", Trait_mean_Shallow_Mort,
#            delimiter=",")

Trait_mean_Shallow_Mort = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanShallowMort.csv",
                                     delimiter=",")

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanDeepSurv.csv", Trait_mean_Deep_Surv,
#            delimiter=",")

Trait_mean_Deep_Surv = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanDeepSurv.csv", delimiter=",")

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanDeepMort.csv", Trait_mean_Deep_Mort,
#            delimiter=",")

Trait_mean_Deep_Mort = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitmeanDeepMort.csv", delimiter=",")


# np.save("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitarrayDeepShallow.npy", Trait_array)

Trait_array = np.load("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\TraitarrayDeepShallow.npy", allow_pickle = False)

# DevShallow = np.log10(Cult3mLShallow.Dev_time)

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\DevShallow.csv", DevShallow, delimiter=",")

DevShallow = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\DevShallow.csv", delimiter=",")

# DevDeep = np.log10(Cult3mLDeep.Dev_time)

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\DevDeep.csv", DevDeep, delimiter=",")

DevDeep = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\DevDeep.csv", delimiter=",")

# MortShallow = np.log10(Cult3mLShallow.Mort_time)

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\MortShallow.csv", MortShallow, delimiter=",")

MortShallow = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\MortShallow.csv", delimiter=",")

# MortDeep = np.log10(Cult3mLDeep.Mort_time)

# np.savetxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\MortDeep.csv", MortDeep, delimiter=",")

MortDeep = np.loadtxt("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\MortDeep.csv", delimiter=",")


####################### Plot Info. ###########################################

Mean_line = [20, 0.5, 0.18, 3000, 1.05, 1, 0.3, 0.05, 180, 0.095, 1.5]

yLabels = ["Hatching Time (hrs)", "Egg Length (mm)", "Egg Width (mm)",
"Initial Bite Rate", "Crowding Threshold", "Peak Crowding Bite Rate Mod",
"Mean Efficiency", "Efficiency c.o.v.", "Minimum Critical Mass (ug)",
"Waste Tolerance Factor", "Digging Length Multiplier"]

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
    
    ax1[0].axhline(Mean_line[i], color = 'purple', linestyle = '--', linewidth=2, alpha = 0.4, zorder = 1, label = '_Hidden')
    ax1[1].axhline(Mean_line[i], color = 'purple', linestyle = '--', linewidth=2, alpha = 0.4, zorder = 1)

    sns.scatterplot(ax = ax1[0], 
                x = DevShallow[DevShallow>0], 
                y = Trait_array[-1, i+1, DevShallow > 0], 
                marker = 'o', edgecolor = 'deepskyblue', 
                facecolor = 'lightskyblue', alpha = 0.8, label = 'Surviving')
    
    sns.scatterplot(ax = ax1[0], 
                x = MortShallow[MortShallow>0], 
                y = Trait_array[-1, i+1, MortShallow > 0], 
                marker = 'o', edgecolor = 'crimson', facecolor = 'salmon', 
                alpha = 0.2, label = 'Dying')
    
    sns.scatterplot(ax = ax1[1], 
                x = MortDeep[MortDeep>0], 
                y = Trait_array[-1, i+1, MortDeep > 0], 
                marker = 'o', edgecolor = 'crimson', facecolor = 'salmon',
                alpha = 0.2)
    sns.scatterplot(ax = ax1[1], 
                x = DevDeep[DevDeep>0], 
                y = Trait_array[-1, i+1, DevDeep > 0], 
                marker = 'o', edgecolor = 'deepskyblue', 
                facecolor = 'lightskyblue', alpha = 0.8)
    
    ax1[0].set_ylabel(yLabels[i])
    ax1[0].set_xlabel("Log 10 Time")
    ax1[1].set_ylabel(yLabels[i])
    ax1[1].set_xlabel("Log 10 Time")
    ax1[0].set_title("Shallow")
    ax1[1].set_title("Deep")
    ax1[0].legend(frameon = True)
    
    
    fig2, ax2 = plt.subplots(1, 2, sharey = True)
    
    ax2[0].axhline(Mean_line[i], color = 'grey', linestyle = '-', linewidth=3, alpha = 0.4, zorder = -1)
    ax2[1].axhline(Mean_line[i], color = 'grey', linestyle = '-', linewidth=3, alpha = 0.4, zorder = -1)

    sns.boxplot(ax = ax2[0], 
                data = [Trait_array[-1, i+1, DevShallow>0], 
                        Trait_array[-1, i+1, MortShallow>0]], 
                palette = ['lightskyblue', 'salmon'],
                showmeans = True,
                boxprops={'edgecolor' : 'black'}, 
                meanprops = {'markersize' : 8, 'markerfacecolor' : 'lightgreen',
                             'markeredgecolor' : 'darkgreen'},
                medianprops = {'color' : 'indigo'},
                whiskerprops = {'color' : 'black'},
                capprops = {'color' : 'black'},
                flierprops = {'markersize' : 5})
    
    sns.boxplot(ax = ax2[1], 
                data = [Trait_array[-1, i+1, DevDeep>0], 
                        Trait_array[-1, i+1, MortDeep>0]], 
                palette = ['lightskyblue', 'salmon'],
                showmeans = True,
                boxprops={'edgecolor' : 'black'}, 
                meanprops = {'markersize' : 8, 'markerfacecolor' : 'lightgreen',
                             'markeredgecolor' : 'darkgreen'},
                medianprops = {'color' : 'indigo'},
                whiskerprops = {'color' : 'black'},
                capprops = {'color' : 'black'},
                flierprops = {'markersize' : 5})
    
    ax2[0].set_xticklabels(['Surviving', 'Dying'])
    ax2[1].set_xticklabels(['Surviving', 'Dying'])
    ax2[0].set_ylabel(yLabels[i])
    ax2[0].set_title("Shallow")
    ax2[1].set_title("Deep")
    
    
    assert (np.round(np.mean(Trait_array[-1, i+1, DevShallow>0]), 2) == 
           np.round(Trait_mean_Shallow_Surv[-1, i+1], 2))
    
    assert (np.round(np.mean(Trait_array[-1, i+1, MortShallow>0]),2) == 
            np.round(Trait_mean_Shallow_Mort[-1, i+1], 2))
    
    assert (np.round(np.mean(Trait_array[-1, i+1, DevDeep>0]),2) == 
            np.round(Trait_mean_Deep_Surv[-1, i+1], 2))
    
    assert (np.round(np.mean(Trait_array[-1, i+1, MortDeep>0]),2) == 
            np.round(Trait_mean_Deep_Mort[-1, i+1], 2))
    
    
    fig3, ax3 = plt.subplots(1, 2, sharey = True)
    
    ax3[0].axhline(Mean_line[i], color = 'purple', linestyle = '--', linewidth=2, alpha = 0.4, zorder = 1)
    ax3[1].axhline(Mean_line[i], color = 'purple', linestyle = '--', linewidth=2, alpha = 0.4, zorder = 1)

    sns.stripplot(ax = ax3[0], data = [Trait_mean_Shallow_Surv[:, i+1],
                                    Trait_mean_Shallow_Mort[:, i+1]],
                  palette = ['lightskyblue', 'salmon'],
                  size = 8, zorder = 1, alpha = 0.8)
    sns.stripplot(ax = ax3[1], data = [Trait_mean_Deep_Surv[:, i+1],
                                    Trait_mean_Deep_Mort[:, i+1]],
                  palette = ['lightskyblue', 'salmon'],
                  size = 8, zorder = 1, alpha = 0.8)
    
    sns.pointplot(ax = ax3[0], data = [Trait_mean_Shallow_Surv[:, i+1],
                                    Trait_mean_Shallow_Mort[:, i+1]],
                  join = False,
                  errorbar='sd', color = 'black', capsize = 0.3)
    
    sns.pointplot(ax = ax3[1], data = [Trait_mean_Deep_Surv[:, i+1],
                                    Trait_mean_Deep_Mort[:, i+1]],
                  join = False,
                  errorbar='sd', color = 'black', capsize = 0.3)
    
    ax3[0].set_xticklabels(['Surviving', 'Dying'])
    ax3[1].set_xticklabels(['Surviving', 'Dying'])
    ax3[0].set_ylabel("Mean " + yLabels[i])
    ax3[0].set_title("Shallow; 30 Runs")
    ax3[1].set_title("Deep; 30 Runs")
    
    ################# SAVES ##################################################
    
    fig1.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/Trait plots/'+yLabels[i]+' TimeSingle.png', dpi=300)
    
    fig2.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/Trait plots/'+yLabels[i]+' Single.png', dpi=300)
    
    fig3.savefig('G:/My Drive/EBL - Ph.D/Simulations/SingleGen for Manuscript/Results/Plots/Trait plots/'+yLabels[i]+' MultiRun.png', dpi=300)
