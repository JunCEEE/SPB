/* -*- mode: c; tab-width: 4; indent-tabs-mode: n; c-basic-offset: 4 -*- 
 *
 * $Id: nb_kernel211_x86_64_sse.h,v 1.1 2004/12/26 19:33:01 lindahl Exp $
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
#ifndef _NB_KERNEL211_X86_64_SSE_H_
#define _NB_KERNEL211_X86_64_SSE_H_


/*! \file  nb_kernel211_x86_64_sse.h
 *  \brief x86_64 SSE-optimized versions of nonbonded kernel 211
 *
 *  \internal
 */


/*! \brief Nonbonded kernel 211 with forces, optimized for x86_64 sse.
 *
 *  \internal
 *
 *  <b>Coulomb interaction:</b> Reaction-field <br>
 *  <b>VdW interaction:</b> Lennard-Jones <br>
 *  <b>Water optimization:</b> SPC/TIP3P interacting with non-water atoms <br>
 *  <b>Forces calculated:</b> Yes <br>
 *
 *  \note All level1 and level2 nonbonded kernels use the same
 *        call sequence. Parameters are documented in nb_kernel.h
 */
void
nb_kernel211_x86_64_sse  (int *   nri,        int     iinr[],   int     jindex[],
                       int     jjnr[],     int     shift[],  float   shiftvec[],
                       float   fshift[],   int     gid[],    float   pos[],
                       float   faction[],  float   charge[], float * facel,
                       float * krf,        float * crf,      float   Vc[],
                       int     type[],     int *   ntype,    float   vdwparam[],
                       float   Vvdw[],     float * tabscale, float   VFtab[],
                       float   invsqrta[], float   dvda[],   float * gbtabscale,
                       float   GBtab[],    int *   nthreads, int *   count,
                       void *  mtx,        int *   outeriter,int *   inneriter,
                       float * work);




/*! \brief Nonbonded kernel 211 without forces, optimized for x86_64 sse.
 *
 *  \internal
 *
 *  <b>Coulomb interaction:</b> Reaction-field <br>
 *  <b>VdW interaction:</b> Lennard-Jones <br>
 *  <b>Water optimization:</b> SPC/TIP3P interacting with non-water atoms <br>
 *  <b>Forces calculated:</b> No <br>
 *
 *  \note All level1 and level2 nonbonded kernels use the same
 *        call sequence. Parameters are documented in nb_kernel.h
 */
void
nb_kernel211nf_x86_64_sse(int *   nri,        int     iinr[],   int     jindex[],
                       int     jjnr[],     int     shift[],  float   shiftvec[],
                       float   fshift[],   int     gid[],    float   pos[],
                       float   faction[],  float   charge[], float * facel,
                       float * krf,        float * crf,      float   Vc[],
                       int     type[],     int *   ntype,    float   vdwparam[],
                       float   Vvdw[],     float * tabscale, float   VFtab[],
                       float   invsqrta[], float   dvda[],   float * gbtabscale,
                       float   GBtab[],    int *   nthreads, int *   count,
                       void *  mtx,        int *   outeriter,int *   inneriter,
                       float * work);





#endif /* _NB_KERNEL211_X86_64_SSE_H_ */
