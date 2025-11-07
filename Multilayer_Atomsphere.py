import numpy as np
import matplotlib.pyplot as plt


# Constants

rho0 = 1.2                             # kg/m^3
sigma = 5.67e-8                        # W / (m^2 * K^4)
Mr = 0.02896                           # kg / mol   
P0 = 101325                            # Pa
g0 = 9.80665                           # m / s^2
R_const = 8.3144598                    # J/(mol·K)
T_optimal = 300                        # K
epsilon = 1e-2                         # Threshold


# Atmospheric layers

atm_height = 10000                     
num_of_segments = 2000                 
height_of_segment = atm_height / num_of_segments
height = np.linspace( height_of_segment , atm_height , num_of_segments)


# Absorbption, Reflection and Transmission coeffeients

flux_in = 344                                   # Mars: 147.5 (W / m^2)?
atm_refl_coef = 0.3                             # 0.25 for Mars?
flux_after_albedo =  flux_in - atm_refl_coef * flux_in
alpha_VR = 1e-5                                 # Attenuation_coefficient (alpha) on surface (m^-1)
alpha_IR = np.linspace(0.02 , 0.12 , 6)          
T_in_VR_flux = np.zeros( len( height ) + 1 )    # transmitted visible radiation (downwards)
A_flux = np.zeros( len( height ) )              # absorbed radiation
E_flux = np.zeros( len( height ) )              # emitted radiation
T_in_IR_flux = np.zeros( len( height ) + 1)     # transmitted infrared radiation (downwards)
T_out_flux = np.zeros( len( height ) + 1)       # transmitted infrared radiation (upwards)
absorbed_on_surf = 0                            # flux absorbed by surface
E_space = 0                                     # flux escaped in space
T_in_IR_flux[ 0 ] =  0    


def Barometric_formula(height_array):  
    rho = np.ndarray( len( height ) )      
    for i in range( len( height ) ):
        rho[i] = rho0 * np.exp( - g0 * Mr * (  height[ i ]   )  / R_const / T_optimal )
    # plt.plot( rho/rho0 , height  , linestyle = '--' )
    # plt.xlabel('$ \\rho \ /  \ \\rho_0  $' , fontsize = 14)
    # plt.ylabel('$ Height \ [m] $' , fontsize = 14)
    # plt.title('$ Density\ over\ height $' , fontsize = 14)
    # plt.show()
    # plt.savefig('density_vs_height.png')
    return rho
   

def run_sim(Density):
    for j in range( len(alpha_IR) ):
        iterations=[]
        temp_list_C =[]
        temp_list_C.append(-20)        
        E_flux[:] = 0
        absorbed_on_surf=0
        T_in_VR_flux[:] = 0
        T_in_IR_flux[:] = 0
        T_out_flux[:] = 0
        n = 1
        while True:
            T_in_VR_flux[0] = flux_after_albedo
    
            ''' Downwards '''
    
            for i in range( 1 , len(height) + 1): 
                
                T_in_VR_flux[ i ] = T_in_VR_flux[ i-1 ] * np.exp( - alpha_VR *  ( height_of_segment  ))     
                T_in_IR_flux[  i  ] = (T_in_IR_flux[ i - 1 ]     ) * np.exp( - alpha_IR[j] * (  height_of_segment  )  )     
    
                A_flux[ i - 1 ] += T_in_VR_flux[ i - 1 ] - T_in_VR_flux[ i ] + T_in_IR_flux[ i - 1 ] - T_in_IR_flux[ i ]
    
                E_flux[ i - 1 ] += A_flux[ i - 1 ]  # what is absorbed here is then transmitted to upper and lower cell
    
                if i == 1:  #1st cell
    
                    E_space = E_flux[ i-1 ] / 2    # emit to space half of the absorbed flux
                    E_flux[i] += E_flux[ i-1 ] / 2  # emit to next cell half of the absorbed flux
    
                elif i>=2 and i< len(height) :  # same for the rest 
    
                    E_flux[ i ] += E_flux[ i - 1 ] / 2
    
                    E_flux[ i - 2 ] += E_flux[ i - 1 ] / 2
    
                elif i == len(height):  
    
                    E_flux[ i - 2 ] += E_flux[ i - 1 ]
                    absorbed_on_surf += E_flux[ i - 1 ]
    
            
            absorbed_on_surf = T_in_VR_flux[-1] +  T_in_IR_flux[-1]  + E_flux[-1]/2     
        
            ''' Upwards '''
    
            T_out_flux[ 0 ] =  absorbed_on_surf                       
            T_out_flux[ 1 ] = (T_out_flux[ 0 ]   +   0  ) * np.exp( - alpha_IR[j] * (   height_of_segment )  )     
    
            absorbed_on_surf += (T_out_flux[0] - T_out_flux[1]) / 2 
            
            
            for i in range( 2,  len(height) + 1 ):  
                
                T_out_flux[ i  ] = (T_out_flux[ i - 1 ]   -  E_flux[ -i + 1 ] / 2     ) * np.exp( - alpha_IR[j] * Density[ i - 1 ] * (   height_of_segment )  )     
                E_flux[ -i + 1 ] = T_out_flux[ i - 2 ] - T_out_flux[ i - 1 ]   
    
            T_in_IR_flux[0] += E_flux[ 0 ] / 2   
    
    
            temperature_surface_K = ( (absorbed_on_surf) / sigma)**(1/4)       
            temperature_surface_C = temperature_surface_K - 273.15
            temp_list_C.append(temperature_surface_C)
            
            E_space += E_flux[0] / 2
    
            iterations.append(n)
            
            if abs(temp_list_C[-1] - temp_list_C[-2]) < epsilon:
                print(f"Converged in {len(iterations)} iterations.")
                break
            n += 1

        print(f"Final temperature for alpha_IR = {alpha_IR[j]:.3f}: {temp_list_C[-1]:.2f} °C")
        print(f"Flux leaving earth for alpha_IR = {absorbed_on_surf:.3f} W/m^2")

        # plt.figure()
        # plt.plot(iterations, temp_list_C[1:], marker='o', linestyle='-', label=f'α = {alpha_IR[j]:.3f}')
        # plt.title(f'Temperature evolution for outgoing Flux ({absorbed_on_surf:.0f} W/m^2)')
        # plt.legend()
        # plt.xlabel('Iteration')
        # plt.ylabel('Surface Temperature [°C]')
        # plt.grid(True)
        # filename = f'temp_evolution_alpha_{absorbed_on_surf:.0f}.png'
        # plt.savefig(filename)
        # plt.close()

    return temp_list_C


rho = Barometric_formula(height)
temp = run_sim(rho)

