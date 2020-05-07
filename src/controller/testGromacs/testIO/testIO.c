#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "smalloc.h"


int main(int argc, char const *argv[])
{
	FILE *f_profile = fopen("profile.txt","r");
	
	if (f_profile == NULL)
    {
        fprintf(stderr, "Failed to open file %s for reading\n", "profile.txt");
        return 1;
    }

    size_t n = 0;
    double buff_t;
    double buff_a;

    char line[4096];
    while (fgets(line, sizeof(line), f_profile) != NULL)
    {
	    sscanf(line,"%lf %lf",&buff_t,&buff_a);
	    n++;
	}

	printf("Read %i time slices from profile.txt\n",n);

	rewind(f_profile);

	double *t_fs = (double*) calloc (n,sizeof(double));
	double *power = (double*) calloc (n,sizeof(double));

    n = 0;

    while (fgets(line, sizeof(line), f_profile) != NULL)
    {
	    sscanf(line,"%lf %lf",&t_fs[n],&power[n]);
	    n++;
	}

	double dt = t_fs[1] - t_fs[0];
	int t_step = round(3.008/dt);
	printf("t_step: %i\n", t_step);
	printf("t = %.3e\n", t_fs[t_step]);


	return 0;
}