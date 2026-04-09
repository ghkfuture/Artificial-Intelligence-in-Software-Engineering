#ifndef MACRO_SAFETY_H
#define MACRO_SAFETY_H

#include <stdio.h>

#ifdef DEBUG_MODE
	#define DEBUG_PRINT(msg) printf("DEBUG [%s:%d]: %s\n", __FILE__, __LINE__, msg)
#else
	#define DEBUG_PRINT(msg)
#endif

#define MULTIPLY(a, b) ((a) * (b))

#endif
