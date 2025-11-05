public class Main {
    public static void main(String[] args) {
        final int SIZE = 5;
        int[] arr = {9, 34, 65, 78, 13};
        
        System.out.print("Чётные числа: ");
        for (int i = 0; i < SIZE; i++) {
            if (arr[i] % 2 == 0) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
        
        System.out.print("Нечётные числа: ");
        for (int i = 0; i < SIZE; i++) {
            if (arr[i] % 2 != 0) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
        
        int evenSum = 0;
        for (int i = 0; i < SIZE; i++) {
            if (arr[i] % 2 == 0) {
                evenSum += arr[i];
            }
        }
        System.out.println("Сумма чётных чисел: " + evenSum);
    }
}
