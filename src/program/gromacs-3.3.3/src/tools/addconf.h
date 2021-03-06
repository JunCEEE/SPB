/*
 * $Id: addconf.h,v 1.19.4.3 2008/02/29 07:02:53 spoel Exp $
 * 
 *                This source code is part of
 * 
 *                 G   R   O   M   A   C   S
 * 
 *          GROningen MAchine for Chemical Simulations
 * 
 *                        VERSION 3.3.3
 * Written by David van der Spoel, Erik Lindahl, Berk Hess, and others.
 * Copyright (c) 1991-2000, University of Groningen, The Netherlands.
 * Copyright (c) 2001-2008, The GROMACS development team,
 * check out http://www.gromacs.org for more information.

 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 * 
 * If you want to redistribute modifications, please consider that
 * scientific software is very special. Version control is crucial -
 * bugs must be traceable. We will be happy to consider code for
 * inclusion in the official distribution, but derived work must not
 * be called official GROMACS. Details are found in the README & COPYING
 * files - if they are missing, get the official version at www.gromacs.org.
 * 
 * To help us fund GROMACS development, we humbly ask that you cite
 * the papers on the package - you can find them in the top README file.
 * 
 * For more info, check our website at http://www.gromacs.org
 * 
 * And Hey:
 * Groningen Machine for Chemical Simulation
 */
#include "typedefs.h"

extern 
void add_conf(t_atoms *atoms, rvec **x, rvec **v, real **r, bool bSrenew, 
	      matrix box, bool bInsert,
	      t_atoms *atoms_solvt,rvec *x_solvt,rvec *v_solvt,real *r_solvt, 
	      bool bVerbose,real rshell,int max_sol);
/* Add two conformations together, without generating overlap.
 * When not inserting, don't check overlap in the middle of the box.
 * If rshell > 0, keep all the residues around the protein (0..natoms_prot-1)
 * that are within rshell distance.
 * If max_sol > 0, add max max_sol solvent molecules.
 */
