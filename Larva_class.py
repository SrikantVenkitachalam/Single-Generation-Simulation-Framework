import numpy as np

class Larva:
    def __init__(self, Trait_values, calibrated_min_crit = 180,
                 Post_crit_lim = 36, Waste_conversion = 0.05,
                 BS_initial = 0.00007, BS_final_ratio = 0.5):
        '''
        Creates an instance of a 'larva' that interact with the 
        instance of the Culture class.
        The constructor (__init__) sets up trait values, as well as the
        checks and timers around them that are used in the Feed function 
        (see below). 
        The parameters used (and population ID, in case of mixed cultures) 
        are input in the form of an array (Trait_values). 
        This array is a column of the 2D Traitarray from the TraitGen function.
        The trait indices have been described in the respective file (Traits). 

        Parameters
        ----------
        Trait_values : numpy 1D array
        Contains population ID and all the trait values for a given larva.
        
        calibrated_min_crit : int
        Measured minimum critical mass to pupation. Used for calibrating 
        Larval length and cross-section surface area.
        The default value is 200 ug.
        
        Post_crit_lim : int
        Defines the maximum number of time steps a given larva can feed, 
        after exceeding the minimum critical mass to pupation.
        The default value is 36 times steps (hours).
        
        Waste_conversion : float
        Defines the fraction of food eaten that is converted to 
        metabolic waste, each time step.
        The default fraction is 0.025.
        
        BS_initial : float
        The initial scaling of bite mass as a function of larval body mass.
        The default values is 0.00007.
        
        BS_final_ratio : float
        The final reduction in bite mass scaling (see above) as a proportion 
        of BS_initial.
        The default value is 0.5

        Returns
        -------
        None.
        
        NOTE: ALL MASS CITED IN THE SIMULATION IS DRY MASS DATA.
        See Santos et al. 1997

        '''
        
        self.ID = Trait_values[0] # Population ID
        
        self.Hatch_time = Trait_values[1] # Egg hatching time
        # Counter for hatching of larva
        self.HT_counter = np.round(self.Hatch_time)
        
        self.Egg_length = Trait_values[2] # Egg length, mm
        # Starting larval length = Egg length
        self.Larval_length = self.Egg_length 
        
        self.Egg_width = Trait_values[3] # Egg width, mm
        # Egg cross section Surface Area (SA), square mm
        self.Egg_SA = np.power(self.Egg_width/2, 2) * np.pi
        # Starting larval SA = Egg SA
        self.Larval_SA = self.Egg_SA
        
        # following is the calculation for egg mass (starting larval size).
        # Egg volume is calculated for a cylinder.
        # Base assumption: 0.5 mm length and 0.18 mm width 
        # give approx. 2.7 ug egg mass.
        # Length and width from: Venkitachalam et al. 2022 (MB values)
        # Egg mass from: Bakker 1961
        # Thus, egg mass for given egg length and width can be calculated.
        Egg_vol = self.Egg_length * self.Egg_SA 
        Egg_vol_for_avg = 0.500 * np.pi * np.power(0.09, 2)
        self.Egg_mass = (Egg_vol * 2.7)/Egg_vol_for_avg
        # The larval mass is initialised as the egg mass
        self.Mass = self.Egg_mass
        
        # Set initial bite rate
        self.BR_initial = Trait_values[4]
        # Initialise realised bite rate with initial bite rate
        self.BR_current = self.BR_initial 
        
        # Set the SA Occupancy at which bite rate peaks
        self.BR_inflection = Trait_values[5]
        # Set the factor by which bite rate is multiplied at inflection point
        self.BR_plast_peak = Trait_values[6]
        
        # Set the mean efficiency value (food to biomass conversion)
        self.Efficiency_mean = Trait_values[7]
        # Initialise realised efficiency with mean efficiency
        self.Efficiency_current = self.Efficiency_mean
        # Set the standard deviation of normal dist. for eff. variation
        self.Efficiency_variation = Trait_values[8]
        # Set efficiency variation factor
        # This value is changed every time step based on efficiency variation
        # It is then multiplied with the efficiency mean
        self.Eff_factor = 1
        
        # Set minimum critical mass to pupation
        self.Min_crit_mass = Trait_values[9]
        # Set the max mass possible (3 times min. crit. mass) Santos et al 1997
        self.Max_mass = self.Min_crit_mass * 3
        
        # Set max possible larval SA, which scales with mass up to max mass
        # A calibrated max. larval mass is assumed to give 
        # cross-section larval diameter of 1.4 mm.
        # calibrated max. mass is obtained via: calibrated_min_crit * 3
        # Calibrated diameter obtained from Kaznowski et al. 1985.
        Diameter_calibrated = 1.4
        SA_calibrated = np.pi * np.power((Diameter_calibrated/2), 2)
        self.Max_SA = self.Max_mass * (SA_calibrated/(calibrated_min_crit * 3))
        
        # Set max possible larval length, which scales with mass up to max mass
        # A calibrated max. larval mass is assumed to give 
        # larval length of 4.6 mm.
        # calibrated max. mass is obtained via: calibrated_min_crit * 3
        # Calibrated length value obtained from 
        # Alpatov 1929, Kaznowski et al 1985.
        Len_calibrated = 4.6
        self.Max_Len = self.Max_mass * (Len_calibrated/(calibrated_min_crit*3))
        
        
        # A pre-determined bite scale is used to determine bite mass.
        # Set Bite Scale (BS), which starts at a certain proportion of 
        # larval mass and decreases as mass increases (up to max. mass).
        self.BS_initial = BS_initial # starting Bite Scale
        self.BS_final_ratio = BS_final_ratio # final bite scale reduction
        # Initialise realised bite scale with initial bite scale
        self.BS_current = self.BS_initial
        
        # Set the larval waste tolerance threshold:
        # Proportion of larval mass up to which waste can be ingested;
        # If this proportion is exceeded, the larva dies.
        self.Waste_tolerance = Trait_values[10]
        
        # Set the larval length multiplier for digging length
        self.Digging_factor = Trait_values[11]
        
        # The following are checks or placeholders for variables that will be
        # called after the onset of feeding.
        
        # Status of individual, changes as follows:
        # 0   ->    1    ->    2     ->    3
        # Egg -> PreCrit -> PostCrit -> Wandering
        # If dead, then Status has negative value, denoting cause of death:
        # -1 : Due to starvation (food runs out)
        # -2 : Due to waste toxicity (waste ingested crosses threshold)
        # -5 : Due to culture timer running out
        # Set current status to 0 (Egg)
        self.Status = 0
        
        # Post reaching the minimum critical size, the larva feeds up to 
        # Post_crit_limit time steps. 
        # Post_crit_timer keeps a count of time steps elapsed since PostCrit.
        self.Post_crit_timer = 0
        self.Post_crit_limit = Post_crit_lim
        
        # Placeholder values for important larval feeding properties
        self.Bite_mass = 0 # Bite mass placeholder
        self.Food_eaten = 0 # Food eaten at given time step placeholder
        self.Growth = 0 # Growth at given time step placeholder
        self.Waste_eaten = 0 # Waste eaten in a time step (0 as placeholder)
        self.Waste_ingested_total = 0 # Total waste ingested placeholder
        self.Waste_threshold = 0 # Waste tolerance threshold placeholder
        
        # Fraction of food eaten at given time step excreted as waste
        self.Waste_conversion = Waste_conversion
        
        # End of Larva constructor
    
    
    def Feed(self, Food, Waste, Dens_exp, Con0, Con1, Masspercentile):
        '''
        Defines the feeding behaviour of a larva at a given time step. 
        This function is called within a Culture class instance. 

        Parameters
        ----------
        Food : float
            The mass of food accessed by the larva.
            
        Waste : float
            The mass of waste experienced by the larva.
        
        Dens_exp : float
            Current vial effective SA occupancy.
            
        Con0 : int
            Same as Conditions[0]: Bite rate conditions from Culture class
                = 0: Bite rate does not change with SA Occupancy.
                = 1: Bite rate and food eaten change with SA Occupancy.
        
        Con1 : int
            Same as Conditions[1]:Waste ingestion conditions from Culture class
                = 0: No effect of waste ingested
                >= 1: Waste ingested causes larval death beyond threshold.
                = 2 bite rate reduces due to ingested waste. 
                    The decrease is a NON linear relationship with 
                    waste ingested/waste threshold
            
        Masspercentile: float
            The percentile within which the larva lies w.r.t. body mass.
        
        Returns
        -------
        Food : float
            Input Food - Food eaten
            
        WasteGen : float
            Amount of waste excreted
            
        Waste : float
            Input Waste - Waste ingested

        '''
        
        #----------------------------------------------------------------------
        
        # Under uncrowded conditions, Bite rate increases with larval mass, 
        # up to a maximum of 2x initial bite rate, at max mass
        BR_uncrowded = self.BR_initial + ((self.Mass/self.Max_mass) *
                                             (self.BR_initial))
        
        # Larval SA increases with larval mass up to a max SA at max mass
        self.Larval_SA = self.Egg_SA + ((self.Mass/self.Max_mass) *
                                        (self.Max_SA - self.Egg_SA))
        
        # Larval Length increases with larval mass up to a max Len at max mass
        self.Larval_length = self.Egg_length + ((self.Mass/self.Max_mass) * 
                                         (self.Max_Len - self.Egg_length))
        #----------------------------------------------------------------------
        
        BR_waste_mod = 1 # Initialise bite rate modifier based on waste
        BR_SA_mod = 1 # Initialise bite rate modifier based on SA occupancy
        FE_Reducemod = 1 # Initialise food eaten modifier based on SA occupancy
        RedMass = 0 # Initialise food eaten modifier based on mass percentile
        
        if Con0 >= 1:
            # Bite rate changes with SA Occupancy
            # Bite rate increases up to a peak value
            # (based on BR_plast_peak)
            # This value is reached at the inflection SA Occupancy.
            BR_SA_mod = 1 + self.BR_plast_peak/(
                1 + np.exp(20*(self.BR_inflection - Dens_exp))
                )
            
            # Food eaten modifier's dependence on larval mass percentile
            # It's limited to a 10% change possible
            RedMass = 0.9 + (Masspercentile/100) *0.1
            # Food eaten reduces based on the SA occupancy,
            # dipping more steeply if the larval mass is relatively low
            FE_Reducemod = 1 - 1/(
                1 + np.exp(20*(RedMass - Dens_exp))
                )
            
            if FE_Reducemod < 0.01:
                # sets minimum value of reduction of food eaten
                FE_Reducemod = 0.01
        
        
        if Con1 == 0:
            # Deactivates Waste in the system if Conditions for waste 
            # are inactive
            Waste = 0
            
        elif Con1 >= 1:
            # Waste is ingested, based on the ratio of waste and food 
            # available to the larva.
            # ingested waste also slows down the bite rate of larva, 
            # based on amount ingested proportional to the tolerance threshold
            self.Waste_threshold = self.Waste_tolerance * self.Mass
            
            if Con1 == 2:
                # Bite rate modifier based on proportion ingested waste and 
                # waste tolerance threshold
                BR_waste_mod = 1/(
                    1 + (np.exp(15*(
                (self.Waste_ingested_total/self.Waste_threshold) - 0.5)))
                    )
            
            
        # Bite scale decreases with larval mass,
        # down to a minimum final ratio of initial bite scale, at max mass
        self.BS_current = self.BS_initial - ((self.Mass/self.Max_mass) * 
                                (self.BS_final_ratio * self.BS_initial))
        # Bite mass based on bite scale and current larval mass
        self.Bite_mass = self.Mass * self.BS_current
        
        self.BR_current = BR_uncrowded * BR_SA_mod * BR_waste_mod
        
        if self.BR_current <= (self.BR_initial/100):
            # Set a minimum bite rate to a hundredth of initial bite rate
            self.BR_current = self.BR_initial/100
        
        
        #Total food + waste consumed based on bite mass and realised bite rate,
        # also affected by SA occupancy.
        Total_consumed = self.Bite_mass * self.BR_current * FE_Reducemod
        
        # Food eaten depends on food concentration in medium
        self.Food_eaten = Total_consumed * (Food/(Food + Waste))
        
        # Waste eaten proportional to waste concentration in medium
        self.Waste_eaten = Total_consumed * (Waste/(Waste + Food))
        
        assert (np.round(Total_consumed, 4) == 
                np.round(self.Food_eaten + self.Waste_eaten,4))
        
        if self.Waste_eaten >= Waste:
            # prevents waste from going to negative values
            self.Waste_eaten = Waste
        # Waste eaten adds to total waste ingested
        self.Waste_ingested_total += self.Waste_eaten
        
        
        if Con1 == 0:
            # No waste exists under this condition
            WasteGen = 0
        
        elif Con1 > 0:
            # waste excreted as fraction of food eaten
            WasteGen = self.Food_eaten * self.Waste_conversion
            
            # NOTE: WASTE EATEN IS SUBTRACTED FROM WASTE GENERATED 
            # This is primarily done for ease of bookkeeping of waste.
            # This should not create a large dissonance in the overall results
            # since new waste is added to the system in a couple of hours. 
            
            WasteGen -= self.Waste_eaten
            
            if WasteGen <= 0:
                # in case waste eaten is greater than waste generated,
                # waste generated is set to 0.
                WasteGen = 0
            
        # Loads random number generator for randomly drawing efficiency value
        # from normal distribution
        rng = np.random.default_rng()
        # Generate efficiency variation factor
        self.Eff_factor = rng.normal(1, self.Efficiency_variation)
        # Realised efficiency at current time step
        self.Efficiency_current = self.Efficiency_mean * self.Eff_factor
        if self.Efficiency_current < 0:
            # ensures that efficiency doesn't acquire negative values.
            self.Efficiency_current = 0
        # Growth is food eaten tempered by realised efficiency
        self.Growth = self.Food_eaten * self.Efficiency_current
        # Larval mass increases by growth amount
        self.Mass += self.Growth
        
        return WasteGen, FE_Reducemod, BR_uncrowded, BR_waste_mod, BR_SA_mod, RedMass
        