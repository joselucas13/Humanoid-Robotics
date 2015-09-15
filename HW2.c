/* Standard Stuff */
#include <string.h>
#include <stdio.h>
#include <unistd.h>

/* Required Hubo Headers */
#include <hubo.h>

/* For Ach IPC */
#include <errno.h>
#include <fcntl.h>
#include <assert.h>
#include <unistd.h>
#include <pthread.h>
#include <ctype.h>
#include <stdbool.h>
#include <math.h>
#include <inttypes.h>
#include "ach.h"


/* Ach Channel IDs */
ach_channel_t chan_hubo_ref;      // Feed-Forward (Reference)
ach_channel_t chan_hubo_state;    // Feed-Back (State)

int main(int argc, char **argv) {

    /* Open Ach Channel */
    int r = ach_open(&chan_hubo_ref, HUBO_CHAN_REF_NAME , NULL);
    assert( ACH_OK == r );

    r = ach_open(&chan_hubo_state, HUBO_CHAN_STATE_NAME , NULL);
    assert( ACH_OK == r );

    /* Create initial structures to read and write from */
    struct hubo_ref H_ref;
    struct hubo_state H_state;
    memset( &H_ref,   0, sizeof(H_ref));
    memset( &H_state, 0, sizeof(H_state));

    /* for size check */
    size_t fs;

    /* Get the current feed-forward (state) */
    r = ach_get( &chan_hubo_state, &H_state, sizeof(H_state), &fs, NULL, ACH_O_LAST );
    if(ACH_OK != r) {
        assert( sizeof(H_state) == fs );
    }

    /*HW2*/
    //Initialize the robot 

    H_ref.ref[LSR] = +0.07;
    H_ref.ref[RSR] = -0.07;
    sleep(10);

    // Change the mass to just one leg
    float mov1 = 0;
    while (mov1 < 0.16){
        mov1 += 0.016;
    	  H_ref.ref[LHR] = -mov1;
    	  H_ref.ref[RHR] = -mov1;
    	  H_ref.ref[LAR]= mov1;
    	  H_ref.ref[RAR] = mov1;
        ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
	      //printf("mov1:%f\n",mov1);
        sleep(2);
    }
    
    // Put the right leg up
    float mov2 = 0;
    float mov3 = -mov1;
    while (mov2 < 0.8){
	      mov2 += 0.1;
        mov3 += 0.02;
        mov1 -= 0.036;
    	  H_ref.ref[RKN] = 2.0*mov2;
    	  H.ref[RHP] = -1.0*mov2;
    	  H_ref.ref[RAP]= -mov2;

        H_ref.ref[RAR] = mov1;
        ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
	      printf("mov2:%f\nmov1:%f\n",mov2,mov1);
        sleep(2);
    }

   ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
   sleep(10);

    float amplitude = 0.2;
    float freq = 0.25;
    float period = 1/freq;
    float count = 0;
    float mov4 = 0;
    float ang1 = asin(amplitude/0.3);
    float t1,t2,temp;
    
    //Go up and down with the left leg
    while (count < 100){
	  //get time
        r = ach_get( &chan_hubo_state, &H_state, sizeof(H_state), &fs, NULL, ACH_O_LAST );
	      if(ACH_OK != r) {
		    assert( sizeof(H_state) == fs );
	      }
	      t1 = H_state.time;
        //printf("t1: %f\n",t1);

        mov4 = (ang1/2)*(sin(M_PI/2 + count*0.1*M_PI) - 1);
        //printf("mov4:%f\n",mov4);
        H_ref.ref[LKN] = -1.2*mov4;
        H_ref.ref[LHP] = +0.6*mov4;
	      H_ref.ref[LAP] = +0.6*mov4;

	      ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
	 
	      //get time
        r = ach_get( &chan_hubo_state, &H_state, sizeof(H_state), &fs, NULL, ACH_O_LAST );
	      if(ACH_OK != r) {
		      assert( sizeof(H_state) == fs );
	      }
	      t2 = H_state.time;
        //printf("t2: %f\n",t2);
	
	      temp = (period/20 - (t2 - t1));
        if (temp < 0) temp = 0;

	      usleep(temp*1000000);

	      count += 1;
     }

    /* Write to the feed-forward channel */
    ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));

}
