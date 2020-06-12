from __future__ import division
import os 
import sys
import numpy as np
import shutil

def get_to_dir(path):
	try:
		os.mkdir(path)
		os.chdir(path)
	except:
		os.chdir(path)
		
energy = 12; #(shift || die "Need an energy boost\n");
myrand = 1993

gmx_kernel = '/gpfs/exfel/data/user/juncheng/SPBProject/src/program/gromacs-3.3.3/src/kernel/' # modified ionize.c
gmx_tools = '/gpfs/exfel/data/user/juncheng/SPBProject/src/program/gromacs-3.3.3/src/tools/' 

#gmx_kernel = '/home/nicusor/software/gromacs-3.3.3/src/kernel/' # unmodified version ionize.c
#gmx_tools = '/home/nicusor/software/gromacs-3.3.3/src/tools/'

cwd = os.getcwd()
tmp = cwd + '/SIMS'

#os.mkdir(tmp)
get_to_dir(tmp)


#NOTE that you need strings here, because Perl will expand numbers to
#a string representation otherwise
#imax_list = ['1e12', '3e12', '1e13']
#pulse_list = ['0.002','0.005','0.01','0.02','0.05','0.1']

imax_list = ['1e12']
pulse_list = ['0.002']

pulse_profile = open(cwd + '/profile.txt', 'r')
lines = pulse_profile.readlines()

t0 = lines[0].split()[0]
t1 = lines[1].split()[0]

timestep = float(t1)-float(t0) # timestep

numofsteps = len(lines)-1    # number of steps


fwhm_to_sigma = 2*np.sqrt(2*np.log(2))
for imax in imax_list:
    for p in pulse_list:
        DIR = tmp + '/imax_'+ imax + '_pulse_' + p + '_' + 'energy_' + str(energy)
        get_to_dir(DIR)
        shutil.copy2(os.path.join(cwd, 'profile.txt'),DIR) 

        # Convert FWHM to sigma
        print float(p)
        pulse = float(p)/fwhm_to_sigma
        #dt = 0.00005
        dt = timestep*0.001 # from fs to ps
        dt = timestep # from fs to ps
        #dt = 0.00005
        #	nsteps = int((pulse*6)/dt)
        nsteps = numofsteps
        #tinit = -pulse*3
        tinit = t0 

        nstxout = 1 # int(nsteps/60.0) # otherwise maybe integer division
        nstlog  = 1 #int(0.0005/dt)
        #if (nsteps < 60):
        #    nstxout = 1; 
        nstlog  = 1;

        #print ('***********' x 80)."\n".('*' x 80)."\n";
        print ('**************** \n')
        print "*  Starting simulation with the following parameters\n";
        print "*  imax    = {0}\n".format(imax)
        print "*  pulse   = {0}\n".format(pulse)
        print "*  energy  = {0}\n".format(energy)
        print "*  nsteps  = {0}\n".format(nsteps)
        print "*  nstxout = {0}\n".format(nstxout)
        print "*  tinit   = {0}\n".format(tinit)
        print "*  DT      = {0}\n".format(dt)
        print "*  dir     = {0}\n".format(DIR)
        print ('**************** \n')

        #print ('*' x 80)."\n".('*' x 80)."\n";
        #open a file in perl for writing by prepending >
        #FP = open('grompp.mdp', 'w')
        #open FP, ">grompp.mdp";
        #Shell like here doc syntax, by using double quotes tell perl to
        #interpolate variables.
        #print FP <<"EOF";

        with open('grompp.mdp', 'w') as FP:
	        mydata = """; VARIOUS PREPROCESSING OPTIONS = 
title                    = Testing imax = {0}, pulse = {1}, energy = {2}, start = 0
cpp                      = /lib/cpp
define                   = -DFLEX_SPC

; RUN CONTROL PARAMETERS = 
integrator               = md
; start time and timestep in ps = 
tinit                    = {5} 
dt                       = {6} 
nsteps                   = {3} 
; number of steps for center of mass motion removal = 
nstcomm                  = 0

; LANGEVIN DYNAMICS OPTIONS = 
; Temparature, friction coefficient (amu/ps) and random seed = 
ld_temp                  = 300
ld_fric                  = 0
ld_seed                  = 1993

; ENERGY MINIMIZATION OPTIONS = 
emtol                    = 0.001
emstep                   = 0.1
nstcgsteep               = 1000

; OUTPUT CONTROL OPTIONS = 
; Output frequency for coords (x), velocities (v) and forces (f) = 
nstxout                  = {4} 
nstvout                  = 0
nstfout                  = 0
; Output frequency for group stuff and for energies (nstprint) = 
nstlog                   = {8} 
nstenergy                = {8}
; Output frequency for xtc files, and associated precision = 
nstxtcout                = 0
xtc_precision            = 1000
; This selects the subset of atoms for the XTC file. = 
; Only the first group gets written out, it does not make sense = 
; to have multiple groups. By default all atoms will be written = 
xtc_grps                 = Protein
; Selection of energy groups = 
energygrps               = system

; NEIGHBORSEARCHING PARAMETERS = 
; nblist update frequency = 
nstlist                  = 0
; ns algorithm (simple or grid) = 
ns_type                  = simple
deltagrid                = 2
; Box type, rectangular, triclinic, none = 
pbc                      = No

; OPTIONS FOR ELECTROSTATICS = 
; Method for doing electrostatics = 
coulombtype              = cut-off
vdwtype                  = cut-off
; cut-off lengths        = 
rlist                    = 0
rcoulomb                 = 0
rvdw                     = 0
rvdw_switch		 = 0
; Dielectric constant (DC) for twin-range or DC of reaction field = 
epsilon_r                = 1
; Apply long range dispersion corrections for Energy and Pressure = 
bdispcorr                = no

; OPTIONS FOR WEAK COUPLING ALGORITHMS = 
; Temperature coupling   = 
Tcoupl                   = no
tc_grps                  = system
tau_t                    = 0.1
ref_t                    = 300
; Pressure coupling      = 
Pcoupl                   = no

; SIMULATED ANNEALING CONTROL = 
annealing                = no
; Time at which temperature should be zero (ps) = 
zero_temp_time           = 0

; GENERATE VELOCITIES FOR STARTUP RUN = 
gen_vel                  = yes
gen_temp                 = 20.0
gen_seed                 = 173529

; OPTIMIZATIONS FOR SOLVENT MODELS = 
; Solvent molecule name (blank: no optimization) = 
solvent_optimization     = SOL
; Number of atoms in solvent model. = 
; (Not implemented for non-three atom models) = 
nsatoms                  = 3

; OPTIONS FOR BONDS     = 
constraints              = none;all-bonds
morse                    = yes

; NMR refinement stuff  = 
; Distance restraints type: None, Simple or Ensemble = 
disre                    = No

; Free energy control stuff = 
free_energy              = no

; User defined thingies = 
userint1                 = {9}
userint2                 = {2}
userint3                 = 0
userint4                 = 0
userreal1                = 0.0
userreal2                = {0} 
userreal3                = {1} 
userreal4                = 100

	 
""".format(imax, pulse, energy, nsteps, nstxout, tinit, dt, DIR, nstlog, myrand)

    		FP.writelines(mydata)
        FP.close()
	    #exit(0)

        tpr = "topol.tpr" # topology file
	    # /home/ibrahim/software/GROMACS/gromacs-3.3.3/src/kernel, /home/ibrahim/software/GROMACS/gromacs-3.3.3/src/tools
	    #system 
	        # "grompp",'-v','-c',"$cwd/after_em",'-p',"$cwd/topol",'-o',$tpr;
        os.system(gmx_kernel + 'grompp -v -c ' + cwd + '/after_em' + ' -p ' + cwd + '/topol' +' -o ' + tpr ) # kernel
	    #os.system(gmx_kernel + 'mdrun -v ionize -o traj.trr -s ' + tpr)
        os.system(gmx_kernel + 'mdrun -v -ionize -s ' + tpr + ' -o traj.trr')
        print (gmx_kernel + 'mdrun -v -ionize -s ' + tpr + ' -o traj.trr')
        print (DIR)
        #os.system('gzip md.log ener.edr traj.trr confout.gro ionize.log ionize.xvg &') #system "gzip md.log ener.edr traj.trr confout.gro ionize.log ionize.xvg &";
        os.chdir(cwd)
	       	#system 
		    #"mdrun",'-v',($imax != 0 ? '-ionize' : ''),'-o',
		    #'traj.trr','-s',$tpr;
	        #here we need the shell to put this in the background
	        	#system "gzip md.log ener.edr traj.trr confout.gro ionize.log ionize.xvg &";
	
 
