# Functions 

## Dispersion curve estimative 


import numpys as np

def create_velocity_model_from_profile(model_profile):

    dens_values_unique,dens_index_unique = np.unique(model_profile,return_index=True)

    dens_index_unique = sorted(dens_index_unique)

    depth_ = np.linspace(0,-2.,len(model_profile)+1)

    thickness_ = [depth_[i] for i in dens_index_unique]
    thickness_.append(-2.0)

    thickness = np.diff(thickness_)*(-1)

    dens = model_profile[dens_index_unique]

    vp, vs = calculate_parameters(dens)

    vmodel = []
    for idx in range(len(dens)):

        # thickness, Vp, Vs, density
        # km, km/s, km/s, g/cm3        

        vmodel.append([thickness[idx]/1000,vp[idx]/1000,vs[idx]/1000,dens[idx]/1000])
   
    velocity_model = np.array(vmodel)    

    return velocity_model

def create_velocity_model_from_profile_vs(model_profile):
    
    vmodel = []
    for (thickness,vs) in zip(*model_profile):
 
        vp, dens = calculate_parameters_from_vs(vs)
        
        # thickness, Vp, Vs, density
        # km, km/s, km/s, g/cm3

        vmodel.append([thickness,vp/1000,vs/1000,dens/1000])
   
    velocity_model = np.array(vmodel)    

    return velocity_model

def estimate_disp_from_velocity_model(vel_mol,number_samples=100):
    # Periods must be sorted starting with low periods
    hz = np.linspace(1, 100.0, number_samples) # Hertz
    
    t = 1/hz[::-1] # Hertz to seconds
    
    # Fundamental mode corresponds to mode 0
    pdisp = PhaseDispersion(*vel_mol.T,dc=0.0001)

    cpr = pdisp(t, mode=0, wave="rayleigh")

    return cpr    