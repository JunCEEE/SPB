#include <math.h>
#include <string.h>
#include <stdio.h>
#include <string.h>


size_t readProfile(double *t_profile,double *inten_profile)
{
    FILE *fp = fopen("/home/ibrahim/software/GROMACS/gromacs-3.3.3/src/kernel/profile.txt","r");
    if (fp == NULL)
    {
      fprintf(stderr, "Failed to open file %s for reading\n", "profile.txt");
      return 1;
    }

    size_t n = 0;
    double buff_t;
    double buff_a;
    int STRLEN = 700;

    char line[STRLEN+1];
    while (fgets2(line,STRLEN,fp))
    {
      sscanf(line,"%lf %lf",&buff_t,&buff_a);
      n++;
    }

    printf("Read %i time slices from profile.txt\n",n);

    frewind(fp);
    n = 0;

    snew(t_profile,n);
    snew(inten_profile,n);

    while (fgets2(line,STRLEN,fp))
    {
      sscanf(line,"%lf %lf",&t_profile[n],&inten_profile[n]);
      n++;
    }

    return n;
}


double powerSASE(double t,double *t_profile,double *inten_profile, size_t n_profile)
{
  double dt = t_profile[1] - t_profile[0];
  int t_step = round(t/dt);
  if (t_step < n_profile)
    return inten_profile[t_step];
  else 
    return 0.0;
}

double *t_profile, *inten_profile;
n_profile = readProfile(t_profile, inten_profile);
pt = powerSASE(t,t_profile,inten_profile,n_profile)
