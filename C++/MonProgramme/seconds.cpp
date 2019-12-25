#include "seconds.h"

int totalSeconds(int hour, int minute, int seconds)
{
    int total(0);
    total += hour * 60 * 60;
    total += minute * 60;
    total += seconds;
    return total;
}
