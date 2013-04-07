#include <stdio.h>
#include <stdlib.h>

/* Checks log files from regularly scheduled web crawler 
 *
 * Returns:
 *
 * 0 if log file indicates no bad images found
 * 2 if log file indicates bad images found
 * 3 if bad images status unknown/error reading log file
 *
 * If bad images exist, they are listed in the log file
*/
int main(int argc, char *argv[]) {
  FILE *fp;
  fp = fopen("bad_images.log", "r");
  char i;
  int return_val = 3;

  if (fp != NULL) {
    /* The first character of the log file is the number of bad images */
    if ( (i = getc(fp)) != EOF ) { 
      if ( atoi(&i) > 0) {
	printf("WARNING: Bad images found in bad_images.log\n");
	return_val = 2;
      }
      else if ( atoi(&i) == 0) {
	return_val = 0;
	printf("No bad images found in bad_images.log\n");
      }
    }
  }

  fclose(fp);
  return return_val;
}

