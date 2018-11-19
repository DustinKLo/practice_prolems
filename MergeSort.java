import java.util.Arrays;

class MergeSort {

    public static int[] combine(int[] a, int[] b){
        int length = a.length + b.length;
        int[] result = new int[length];
        System.arraycopy(a, 0, result, 0, a.length);
        System.arraycopy(b, 0, result, a.length, b.length);
        return result;
    }

    public int[] mergeSort(int[] ls) {
        if(ls.length == 1) {
            return ls;
        }
        int len = ls.length;
        int[] left = Arrays.copyOfRange(ls, 0, len/2);
        int[] right = Arrays.copyOfRange(ls, len/2, len);
        left = mergeSort(left);
        right = mergeSort(right);

        int i = 0; // array index for left
        int j = 0; // array index for right
        int k = 0; // array index for sorted
        int[] sorted = new int[len];
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

        if(i < left.length) {
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

    public static void main(String args[]) {
        MergeSort test = new MergeSort();
        int[] arr = new int[]{1,2,3,4,5,6,7,8,9,10,11,12,12,11,10,9,8,7,6,5,4,3,2,1};
        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.toString(test.mergeSort(arr)));
    }

}
