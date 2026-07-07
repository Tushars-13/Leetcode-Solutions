class Solution {
	void selectionSort(int[] arr) {
		// code here
		int n = arr.length;
		
		for (int i = 0; i<n - 1;i++ ) {
			
			// find minimum element
			for (int j = i + 1; j<n; j++) {
				
				if (arr[j]<arr[i]) {
					int temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
					
				}
			}
			
		}
	}
}