import numpy as np

def TraitGen(Eggnum, ID = 1,
             HT_m = 20, HT_v = 0.01,
             EL_m = 0.500, EL_v = 0.05,
             EW_m = 0.180, EW_v = 0.05,
             BR_start_m = 3000, BR_start_v = 0.05,
             BR_inf_m = 0.8, BR_inf_v = 0.05,
             BR_plast_m = 2, BR_plast_v = 0.05,
             Eff_larv_m = 0.15, Eff_larv_v = 0.05,
             Eff_var_m = 0.1, Eff_var_v = 0.05,
             MC_m = 180, MC_v = 0.05,
             WT_m = 0.05, WT_v = 0.05,
             Dig_m = 1.5, Dig_v = 0.05):
    '''
    Generates various trait values for all the larvae of a given culture.
    Besides the starting number and population ID, all other traits have
    two parameter settings - mean and coefficient of variation (cv).
    Unless otherwise stated, all traits with cv > 0 have values randomly
    drawn from a normal distribution with given mean and standard
    deviation (mean * cv).
    The trait descriptions are given in the following text. For each trait
    besides Eggnum and ID, the '_m' variable stands for mean, '_v' stands
    for cv.

    Parameters
    ----------
    Eggnum : int
        Starting number of eggs in a culture.

    1. ID : int
        Population ID for larvae. Used for bitypic cultures.

    2. HT : float,
        Hatching time. The default mean is 20 hours. The default cv is 0.01.
        (Venkitachalam et al. 2021)

    3. EL : float
        Egg length. The default mean is 0.500 mm. The default cv is 0.05.
        (Venkitachalam et al. 2021)

    4. EW : float
        Egg width. The default mean is 0.180 mm. The default cv is 0.05
        (Venkitachalam et al. 2021)

    5. BR_start : float
        Starting number of bites per time step (i.e. bite rate).
        The default mean is 3000. The default cv is 0.05.
        (Santos et al. 1997, Joshi et al. 2003)

    6. BR_inf : float
        The crowding level (feeding band occupancy) at which bite rate peaks.
        The default mean is 0.8. The default cv is 0.05.

    7. BR_plast : float
        The factor by which bite rate is increased at BR_inf.
        The default mean is 2. The default cv is 0.05.

    8. Eff_larv : float
        Base food to biomass conversion efficiency.
        The default mean is 0.15. The default cv is 0.05.
        (Bakker 1961)

    9. Eff_var : float
        Standard deviation of factor by which efficiency can change
        every time step, Drawn from a normal distribution with mean 1.
        The default mean std. dev. per larva is 0.1.
        The default cv of this std. dev., varying across larvae, is 0.05.

    10. MC : float
        The minimum critical mass required for pupation.
        The default mean is 180 ug. The default cv is 0.05.
        (Santos et al. 1997)

    11. WT : float
        Threshold beyond which waste ingested kills the larvae.
        The default mean is 0.05 times larval mass. The default cv is 0.05.

    12. Dig : float
        Factor of larval length up to which food column is accessible.
        The default mean is 1.5. The default cv is 0.05.


    Returns
    -------
    Traitarray:
    A numpy 2D array with rows as the different traits.
    Columns as trait values for each larva in the culture.

    '''
    # Initiates a trait array with rows representing different traits,
    # columns represent individual larvae
    Traitarray = np.zeros((12, Eggnum))

    # Loads random number generator for randomly drawing values
    # from normal distribution
    rng = np.random.default_rng()

    # Besides ID, each trait value for each larva is randomly drawn from a
    # normal distribution with the given mean, std. dev.
    # np.random.normal(a, b, c) calls the normal distribution function
    # a = mean, b = standard deviation, c = number of samples drawn (larvae)
    # The order of traits is listed in the TraitGen function description

    Traitarray[0, :] += ID
    Traitarray[1, :] = rng.normal(HT_m, (HT_m * HT_v), Eggnum)
    Traitarray[2, :] = rng.normal(EL_m, (EL_m * EL_v), Eggnum)
    Traitarray[3, :] = rng.normal(EW_m, (EW_m * EW_v), Eggnum)
    Traitarray[4, :] = rng.normal(BR_start_m,(BR_start_m * BR_start_v), Eggnum)
    Traitarray[5, :] = rng.normal(BR_inf_m, (BR_inf_m * BR_inf_v), Eggnum)
    Traitarray[6, :] = rng.normal(BR_plast_m,(BR_plast_m * BR_plast_v), Eggnum)
    Traitarray[7, :] = rng.normal(Eff_larv_m,(Eff_larv_m * Eff_larv_v), Eggnum)
    Traitarray[8, :] = rng.normal(Eff_var_m, (Eff_var_m * Eff_var_v), Eggnum)
    Traitarray[9, :] = rng.normal(MC_m, (MC_m * MC_v), Eggnum)
    Traitarray[10, :] = rng.normal(WT_m, (WT_m * WT_v), Eggnum)
    Traitarray[11, :] = rng.normal(Dig_m, (Dig_m * Dig_v), Eggnum)

    return Traitarray

# Trial for debugging
Traittry = TraitGen(10, 1)