class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            // a and b, bit shifted by 1, temp ensures we use old value of a
            int temp = (a & b) << 1; 

            a = a ^ b;  // a xor b
            b = temp;
        }
        return a;
    }
}