int checksumCalc(int arr[], int NUM_DIGIT){
	int checksum = 0;
	for (int i = 0; i <= NUM_DIGIT - 1; i++){
		if (i % 2 == 0){
			if (arr[i] * 2 > 9) {
				checksum += arr[i] * 2 % 10 + (arr[i] * 2 - arr[i] * 2 % 10)/10;
			}
			else {
				checksum += arr[i] * 2;
			}
		} else {
			checksum += arr[i];
		}
	}
	return checksum;
}

bool checksumValid(int n){
	if (n % 10 == 0){
		return true;
	} else {
		return false;
	}
}