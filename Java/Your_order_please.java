package Java;

import java.util.*;

public class Your_order_please {
    public static String order(String words) {
        String[] arrOfStr = words.split(" ");
        String[] numbers = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };
        Stack<String> stack = new Stack<String>();
        String strFinal = "";

        for (String b : numbers) {
            for (String a : arrOfStr) {
                if (a.indexOf(b) != -1) {
                    stack.add(Integer.parseInt(b) - 1, a);
                }

            }

        }

        Object[] arr = stack.toArray();
        for (int j = 0; j < arr.length; j++) {
            if (j == arr.length - 1) {
                strFinal += arr[j];
            } else {
                strFinal += arr[j] + " ";
            }

        }

        return strFinal;

    }
}