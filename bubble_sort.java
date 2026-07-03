class Solution {
    public void bubbleSort(int[] arr) {
        // code here
        int n =arr.length;
        
        for(int pass=1; pass<n; pass++){ // passes, if array has 5 elements then there will be 4 passes
            
            boolean swapped = false; // default flag
            
            for(int j=0; j<n-pass;j++){ // loop on every pass
                
                if(arr[j]>=arr[j+1]){ //comparing adjacent elements

                    // swapping
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                    
                    swapped = true; // flag->true if swapping happens
                }
            }
            
            if(!swapped){
                break; // break out of the loop if the array becomes sorted
            }
        }
        
    }
}
