/* -*- mode: c; tab-width: 4; indent-tabs-mode: n; c-basic-offset: 4 -*- 
 *
 * $Id: nb_kernel313_ia32_sse2.h,v 1.1 2004/12/26 19:31:00 lindahl Exp $
 * 
 * This file is part of Gromacs        Copyright (c) 1991-2004
 * David van der Spoel, Erik Lindahl, University of Groningen.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * To help us fund GROMACS development, we humbly ask that you cite
 * the research papers on the package. Check out http://www.gromacs.org
 * 
 * And Hey:
 * Gnomes, ROck Monsters And Chili Sauce
 */
#ifndef _NB_KERNEL313_IA32_SSE2_H_
#define _NB_KERNEL313_IA32_SSE2_H_

/*! \file  nb_kernel313_ia32_sse2.h
 *  \brief ia32 SSE2-optimized versions of nonbonded kernel 313
 *
 *  \internal
 */


/*! \brief Nonbonded kernel 313 with forces, optimized for ia32 sse2.
 *
 *  \internal
 *
 *  <b>Coulomb interaction:</b> Tabulated <br>
 *  <b>VdW interaction:</b> Lennard-Jones <br>
 *  <b>Water optimization:</b> TIP4P interacting with non-water atoms <br>
 *  <b>Forces calculated:</b> Yes <br>
 *
 *  \note All level1 and level2 nonbonded kernels use the same
 *        call sequence. Parameters are documented in nb_kernel.h
 */
void
nb_kernel313_ia32_sse2  (int *    nri,        int      iinr[],    int      jindex[],
                         int      jjnr[],     int      shift[],   double   shiftvec[],
                         double   fshift[],   int      gid[],     double   pos[],
                         double   faction[],  double   charge[],  double * facel,
                         double * krf,        double * crf,       double   Vc[],
                         int      type[],     int *    ntype,     double   vdwparam[],
                         double   Vvdw[],     double * tabscale,  double   VFtab[],
                         double   invsqrta[], double   dvda[],    double * gbtabscale,
                         double   GBtab[],    int *    nthreads,  int *    count,
                         void *   mtx,        int *    outeriter, int *    inneriter,
                         double * work);





/*! \brief Nonbonded kernel 313 without forces, optimized for ia32 sse2.
 *
 *  \internal
 *
 *  <b>Coulomb interaction:</b> Tabulated <br>
 *  <b>VdW interaction:</b> Lennard-Jones <br>
 *  <b>Water optimization:</b> TIP4P interacting with non-water atoms <br>
 *  <b>Forces calculated:</b> No <br>
 *
 *  \note All level1 and level2 nonbonded kernels use the same
 *        call sequence. Parameters are documented in nb_kernel.h
 */
void
nb_kernel313nf_ia32_sse2(int *    nri,        int      iinr[],    int      jindex[],
                         int      jjnr[],     int      shift[],   double   shiftvec[],
                         double   fshift[],   int      gid[],     double   pos[],
                         double   faction[],  double   charge[],  double * facel,
                         double * krf,        double * crf,       double   Vc[],
                         int      type[],     int *    ntype,     double   vdwparam[],
                         double   Vvdw[],     double * tabscale,  double   VFtab[],
                         double   invsqrta[], double   dvda[],    double * gbtabscale,
                         double   GBtab[],    int *    nthreads,  int *    count,
                         void *   mtx,        int *    outeriter, int *    inneriter,
                         double * work);




#endif /* _NB_KERNEL313_IA32_SSE2_H_ */
