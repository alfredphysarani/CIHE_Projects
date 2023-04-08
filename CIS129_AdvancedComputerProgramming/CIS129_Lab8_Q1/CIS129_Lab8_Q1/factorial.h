double factorial(int n) {
	double fac = 1;
	for (int i = 1; i <= n; i++){
		fac *= i;
	}
	return fac;
}