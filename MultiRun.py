'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the data for 30 runs of the full framework design under the expanded model (see Manuscript/chapter 6 in thesis, "Predictions" section and supplementary section).

NOTE: Please change the required directories for saving/reading data!!!
'''

import multiprocessing as mp
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from Culture_class import Culture
from Traits import TraitGen


def MultiCrowdRun(Rep):
    
    rng = np.random.default_rng(Rep)
    
    CultHt = 3
    CultSA = 3
    CultE = 3
    
    HtMultiple = 5
    SAMultiple = 200
    EMultiple = 200
    
    Time = 1500
    
    Height = np.zeros((CultHt, CultSA, CultE))
    Surface_area = np.zeros((CultHt, CultSA, CultE))
    Eggs = np.zeros((CultHt, CultSA, CultE), dtype = int)
    
    Food_vol = np.zeros((CultHt, CultSA, CultE))
    Feeding_band_vol = np.zeros((CultHt, CultSA, CultE))
    Total_density = np.zeros((CultHt, CultSA, CultE))
    Effective_density = np.zeros((CultHt, CultSA, CultE))
    
    for a in range(CultHt):
        Height[a, :, :] += HtMultiple * (a + 1)
        
    for b in range(CultSA):
        Surface_area[:, b, :] += SAMultiple * (b + 1)
    
    for c in range(CultE):
        Eggs[:, :, c] += EMultiple * (c + 1)
    
    
    Food_vol += Height * Surface_area
    Total_density += Eggs/(Food_vol/1000)
    Feeding_band_vol[Height >= 6] += 6 * Surface_area[Height>=6]
    Feeding_band_vol[Height < 6] += Food_vol[Height < 6]
    Effective_density += Eggs/(Feeding_band_vol/1000)
    
    Diffuse = np.ones((CultHt, CultSA, CultE), dtype = bool)
    W_band = np.zeros((CultHt, CultSA, CultE)) + 0.01
    Saturate = np.zeros((CultHt, CultSA, CultE)) + 0.045
    
    # Eggs = np.arange(70, 70*CultRuns+1, 70); assert len(Eggs) == CultRuns
    
    Conditions = np.zeros(shape = (CultHt, CultSA, CultE, 2), dtype = int) + [1, 2]
    
    ID = np.ones((CultHt, CultSA, CultE), dtype = int)
    
    HT_m = np.zeros((CultHt, CultSA, CultE)) + 20
    HT_v = np.zeros((CultHt, CultSA, CultE)) + 0.01
    
    EL_m = np.zeros((CultHt, CultSA, CultE)) + 0.500
    EL_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    EW_m = np.zeros((CultHt, CultSA, CultE)) + 0.180
    EW_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    BR_start_m = np.zeros((CultHt, CultSA, CultE)) + 3000
    BR_start_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    BR_inf_m = np.zeros((CultHt, CultSA, CultE)) + 1.05
    BR_inf_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    BR_plast_m = np.zeros((CultHt, CultSA, CultE)) + 1
    BR_plast_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    Eff_larv_m = np.zeros((CultHt, CultSA, CultE)) + 0.3
    Eff_larv_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    Eff_var_m = np.zeros((CultHt, CultSA, CultE)) + 0.05
    Eff_var_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    MC_m = np.zeros((CultHt, CultSA, CultE)) + 180
    MC_v = np.zeros((CultHt, CultSA, CultE)) + 0.05
    
    WT_m = np.zeros((CultHt, CultSA, CultE)) + 0.095
    WT_v = np.zeros((CultHt, CultSA, CultE)) + 0.1
    
    Dig_m = np.zeros((CultHt, CultSA, CultE)) + 1.5
    Dig_v = np.zeros((CultHt, CultSA, CultE)) + 0.05

    calibrated_min_crit = np.zeros((CultHt, CultSA, CultE)) + 180
    Post_crit_lim = np.zeros((CultHt, CultSA, CultE), dtype = int) +  36
    Waste_conversion = np.zeros((CultHt, CultSA, CultE)) + 0.025
    BS_initial = np.zeros((CultHt, CultSA, CultE)) + 0.00007
    BS_final_ratio = np.zeros((CultHt, CultSA, CultE)) + 0.5
    
    StartSA = np.zeros((CultHt, CultSA, CultE)) + 0.015
    GrowSA = np.zeros((CultHt, CultSA, CultE)) + 0.002
    # StartDens = np.zeros((CultHt, CultSA, CultE)) + 0.5
    Excr_timer = np.zeros((CultHt, CultSA, CultE), dtype = int) + 1
    
    Culture_array = np.ndarray((CultHt, CultSA, CultE), dtype=object)
    
    Trait_array = np.ndarray((CultHt, CultSA, CultE), dtype = object)
    
    Surv = np.zeros((CultHt, CultSA, CultE))
    
    Dev = np.ndarray((CultHt, CultSA, CultE), dtype = object)
    MeanDev = np.zeros((CultHt, CultSA, CultE))
    VarDev = np.zeros((CultHt, CultSA, CultE))
    
    FinalMass = np.ndarray((CultHt, CultSA, CultE), dtype = object)
    MeanMass = np.zeros((CultHt, CultSA, CultE))
    VarMass = np.zeros((CultHt, CultSA, CultE))
    
    xticklab = np.ndarray((CultHt, CultSA, CultE), dtype = object)
    
    for i in range(CultHt):
        for j in range(CultSA):
            for k in range(CultE):
                print('executing: Rep.', Rep, i, j, k)
                
                Culture_array[i, j, k] = Culture(
                    Surface_area=Surface_area[i, j, k],
                    Height=Height[i, j, k], 
                    Diffuse=Diffuse[i, j, k],
                    W_band=W_band[i, j, k],
                    Saturate = Saturate[i, j, k])
                
                Trait_array[i, j, k] = TraitGen(
                    Eggs[i, j, k], ID = ID[i, j, k],
                    HT_m = HT_m[i, j, k], HT_v = HT_v[i, j, k],
                    EL_m = EL_m[i, j, k], EL_v = EL_v[i, j, k],
                    EW_m = EW_m[i, j, k], EW_v = EW_v[i, j, k],
                    BR_start_m = BR_start_m[i, j, k],
                    BR_start_v = BR_start_v[i, j, k],
                    BR_inf_m = BR_inf_m[i, j, k], 
                    BR_inf_v = BR_inf_v[i, j, k],
                    BR_plast_m = BR_plast_m[i, j, k],
                    BR_plast_v = BR_plast_v[i, j, k],
                    Eff_larv_m = Eff_larv_m[i, j, k],
                    Eff_larv_v = Eff_larv_v[i, j, k],
                    Eff_var_m = Eff_var_m[i, j, k], 
                    Eff_var_v = Eff_var_v[i, j, k],
                    MC_m = MC_m[i, j, k], MC_v = MC_v[i, j, k],
                    WT_m = WT_m[i, j, k], WT_v = WT_v[i, j, k],
                    Dig_m = Dig_m[i, j, k], Dig_v = Dig_v[i, j, k])
                
                Culture_array[i, j, k].Add_eggs(
                    Eggs[i, j, k], Trait_array[i, j, k],
                    calibrated_min_crit = calibrated_min_crit[i, j, k],
                    Post_crit_lim = Post_crit_lim[i, j, k],
                    Waste_conversion = Waste_conversion[i, j, k],
                    BS_initial = BS_initial[i, j, k],
                    BS_final_ratio = BS_final_ratio[i, j, k])
                
                Culture_array[i, j, k].Culture_run(Time, 
                            Conditions = Conditions[i, j, k, :],
                            StartSA = StartSA[i, j, k],
                            GrowSA = GrowSA[i, j, k], 
                            Excrete_timer = Excr_timer[i, j, k])
                
                Surv[i, j, k] = Culture_array[i, j, k].Survivorship
                Dev[i, j, k] = Culture_array[i, j, k].Dev_time[Culture_array[i, j, k].Dev_time>0]
                
                FinalMass[i, j, k] = Culture_array[i, j, k].Mass_profile[
                    -1, Culture_array[i, j, k].Mass_profile[-1, :] > 0]
                xticklab[i, j, k] = str(Eggs[i, j, k])

                MeanDev[i, j, k] = np.mean(Dev[i, j, k])
                MeanMass[i, j, k] = np.mean(FinalMass[i, j, k])
                
                
                VarDev[i, j, k] = np.var(Dev[i, j, k])
                VarMass[i, j, k] = np.var(FinalMass[i, j, k])
                
                
                Culture_array[i, j, k] = []
                Trait_array[i, j, k] = []
                
    Htflat = Height.flatten()
    SAflat = Surface_area.flatten()
    Eggflat = Eggs.flatten()
    Foodflat = Food_vol.flatten()
    FBflat = Feeding_band_vol.flatten()
    TDensflat = Total_density.flatten()
    EffDensflat = Effective_density.flatten()
    Survflat = Surv.flatten()
    Devflat = MeanDev.flatten()
    VDevflat = VarDev.flatten()
    Massflat = MeanMass.flatten()
    VMassflat = VarMass.flatten()
    Replicate = np.zeros(len(Htflat), dtype = int) + Rep
    
    
    CompiledRaw = [Replicate, Htflat, SAflat, Eggflat, Foodflat, FBflat, TDensflat, EffDensflat, Survflat, Devflat, VDevflat, Massflat, VMassflat]
    
    Culture_array = None
    Trait_array = None
    
    print(Rep)
    
    return CompiledRaw


if __name__ == '__main__':
    
    Headers = [
        'Replicate',
        'Height (mm)',
        'Surface area (mm2)',
        'Eggs',
        'Food volume (mm3)',
        'Feeding band volume (mm3)',
        'Total density',
        'Effective density',
        'Survivorship',
        'Mean time to wandering (hrs)',
        'Variance time to wandering (hrs2)',
        'Mean mass at wandering (ug)',
        'Variance mass at wandering (ug2)'
        ]
    
    Replicates = np.arange(20, 30, dtype = int)
    
    Compiled_full  = pd.DataFrame(columns=Headers)
    
    for i in Replicates:
        
        Tstart = time.time()
    
        CompTemp = MultiCrowdRun(i)
        
        CompTemp2 = {
        'Replicate' : CompTemp[0],
        'Height (mm)' : CompTemp[1],
        'Surface area (mm2)' : CompTemp[2],
        'Eggs' : CompTemp[3],
        'Food volume (mm3)' : CompTemp[4],
        'Feeding band volume (mm3)' : CompTemp[5],
        'Total density' : CompTemp[6],
        'Effective density' : CompTemp[7],
        'Survivorship' : CompTemp[8],
        'Mean time to wandering (hrs)' : CompTemp[9],
        'Variance time to wandering (hrs2)' : CompTemp[10],
        'Mean mass at wandering (ug)' : CompTemp[11],
        'Variance mass at wandering (ug2)' : CompTemp[12]
        }
        
        CompTemp2 = pd.DataFrame(CompTemp2)
        
        CompTemp2.to_csv("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\CompiledDataRep"+str(i)+".csv")
        
        # np.save("D:\SingleGenSimResults\CultureRep"+str(i), CultTemp)
        # np.save("D:\SingleGenSimResults\TraitsRep"+str(i), TraitTemp)
        
        Compiled_full = pd.concat([Compiled_full, CompTemp2],
                                 ignore_index=True)
        
        # CultTemp = None
        # TraitTemp = None
        
        Tend = time.time()
        Time_total = Tend-Tstart
        print("Replicate: ", i, "; Time taken = ", Time_total, "s")
        
    Compiled_full.to_excel("G:\My Drive\EBL - Ph.D\Simulations\SingleGen for Manuscript\Results\Compiled_data_Full"+ str(Replicates[0]) + str(Replicates[-1]) + ".xlsx")