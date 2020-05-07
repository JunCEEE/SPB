#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
  char *filename = "../../controller/dumpPulse/gromacs.txt";
  /*char *filename = "./test.txt";*/
  FILE *fp = fopen(filename, "r");
  char *line = NULL;
  size_t len = 0;
  ssize_t read;

  size_t line_idx = 0;
  // Number of lines
  size_t nl;
  if (fp == NULL)
    exit(EXIT_FAILURE);
  // Get number of lines
  while ((read = getline(&line, &len, fp)) != -1) {
    line_idx += 1;
  }
  nl = line_idx;
  line_idx = 0;
  rewind(fp);

  double *time = malloc(nl * sizeof(double));
  double *inten = malloc(nl * sizeof(double));

  // Read data into varaibles
  while ((read = getline(&line, &len, fp)) != -1) {
    sscanf(line, "%lf %lf", &time[line_idx], &inten[line_idx]);
    line_idx++;
  }
  fclose(fp);

  /*printf("delta_t = %5e \n",time[1]-time[0]);*/
  double dt0 = time[1] - time[0];
  // New timestep >= 4e-17 s
  double dt = 10e-17; // s
  int n_skip = dt / dt0;
  /*printf("n_skip = %i \n", n_skip);*/

  size_t i = 0;
  while (*(inten + i * n_skip)) {
    double *p_mid = inten + i * n_skip;
    /*double *inten_mid = inten + i * n_skip;*/
    double sum_inten = 0;
    int n_sum = 0;
    /*printf("p_mid: %.5e\n", *(p_mid));*/
    /*printf("p_inten: %.5e\n", *(inten + i * n_skip));*/
    for (int j = 0; j < n_skip; ++j) {
      double *p_new = p_mid + j - (int)ceil(n_skip / 2);
      if (p_new >= inten) {
        sum_inten += *(p_mid + j - (int)ceil(n_skip / 2));
        /*printf("%.5e\n", *(p_mid + j - (int)ceil(n_skip / 2)));*/
        /*printf("%.5e\n", *(p_new));*/
        n_sum++;
      }
    }

    double mean_inten = sum_inten / n_sum;
    /*printf("%.5e %.5e\n", *(time + i * n_skip) - time[0], mean_inten);*/
    printf("%.5e %.5e\n", *(time + i * n_skip), mean_inten);
        /*printf("n_sum = %d ", n_sum);*/
        /*printf("mean_inten = %.5e\n", sum_inten / n_sum);*/

        /*printf("%.5e %.5e\n", *(time+i*n_skip)-time[0], *(inten+i*n_skip));*/
        i++;
    /*printf("\n");*/
  }

  if (line)
    free(line);
  free(time);
  free(inten);
  exit(EXIT_SUCCESS);
}
