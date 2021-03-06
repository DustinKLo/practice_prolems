import java.util.Arrays;

class MergeSort {

    public static int[] mergeStep(int[] left, int[] right) {
        int i = 0; // array index for left
        int j = 0; // array index for right
        int k = 0; // array index for sorted
        int[] sorted = new int[left.length + right.length];
        int[] leftOver;
        while(i < left.length && j < right.length) {
            if(left[i] < right[j]) {
                sorted[k] = left[i];
                i++;
            } else {
                sorted[k] = right[j];
                j++;
            }
            k++;
        }

        if(i < j) {
            leftOver = Arrays.copyOfRange(left, i, left.length);
        } else {
            leftOver = Arrays.copyOfRange(right, j, right.length);
        }

        for(int n = 0; n < leftOver.length; n++) {
            sorted[k] = leftOver[n];
            k++;
        }
        return sorted;
    }

    public static int[] mergeSort(int[] ls) {
        if(ls.length == 1) {
            return ls;
        }
        int len = ls.length;
        int[] left = Arrays.copyOfRange(ls, 0, len/2);
        int[] right = Arrays.copyOfRange(ls, len/2, len);
        left = mergeSort(left); // recursive step, break it down until array of length 1
        right = mergeSort(right); // recursive step, break it down until array of length 1

        // each recursive level starting from array length 1 up
        // will combine the 2 ordered arrays into one larger ordered array
        return mergeStep(left, right);
    }

    public static void main(String args[]) {
        int[] arr = new int[]{1,2,3,4,5,6,7,8,9,10,11,12,12,11,10,9,8,7,6,5,4,3,2,1};
        System.out.println(Arrays.toString(arr));
        int[] sortedArray = mergeSort(arr);
        System.out.println(Arrays.toString(sortedArray));
    }

}
