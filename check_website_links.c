#include <stdio.h>

/* Checks log files from regularly scheduled web crawler 
 *
 * Returns:
 *
 * 0 if log file indicates no broken links found
 * 2 if log file indicates broken links found
 * 3 if broken links status unknown/error reading log file
 *
 * If broken links exist, they are listed in the log file
*/
int main(int argc, char *argv[]) {
  FILE *fp;
  fp = fopen("bad_links.log", "r");
  char i;
  int return_val = 3;

  if (fp != NULL) {
    /* The first character of the log file is the number of broken links */
    if ( (i = getc(fp)) != EOF ) {
      if (i > 0) {
	printf("WARNING: Broken links found in bad_links.log\n");
	return_val = 2;
      }
      else if (i == 0) {
	return_val = 0;
	printf("No broken links found in bad_links.log\n");
      }
    }
  }

  fclose(fp);
  return return_val;
}
