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

    /*HW1 - Robot waves at me with his left hand at 1 Hz*/
    //Initialize the robot 
    H_ref.ref[LSP] = 0.0;
    H_ref.ref[LSR] = 0.0;
    H_ref.ref[LSY] = 0.0;
    H_ref.ref[LEB] = 0.0;
    H_ref.ref[LWR] = 0.0;
    H_ref.ref[LWP] = 0.0;
    ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
    sleep(3);

    H_ref.ref[LEB] = -3.0;
    H_ref.ref[LSP] = -0.8;
    ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
    sleep(8);

    int count = 0;
    int signal = 1;
    //Wave movement with the left hand
    while (count < 20){
	 H_ref.ref[LSY] = signal*1.0;
         H_ref.ref[LWP] = signal*1.0;
         ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
	 usleep(500000);
         signal *= -1;
	 count += 1;
     }

    H_ref.ref[LSP] = 0.0;
    H_ref.ref[LSR] = 0.0;
    H_ref.ref[LSY] = 0.0;
    H_ref.ref[LEB] = 0.0;
    H_ref.ref[LWR] = 0.0;
    H_ref.ref[LWP] = 0.0;

    /* Print out the actual position of the LEB */
    double posLEB = H_state.joint[LEB].pos;
    printf("Joint = %f\r\n",posLEB);

    /* Print out the Left foot torque in X */
    double mxLeftFT = H_state.ft[HUBO_FT_L_FOOT].m_x;
    printf("Mx = %f\r\n", mxLeftFT);

    /* Write to the feed-forward channel */
    ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));

}
