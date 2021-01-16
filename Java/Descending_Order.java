package Java;

import java.util.Arrays;
import java.util.Collections;

public class Descending_Order {
    public static int sortDesc(final int num) {
        String str = Integer.toString(num);
        String fNum = "";

        // Creating array of string length
        Integer[] ch = new Integer[str.length()];

        // Copy character by character into array
        for (int i = 0; i < str.length(); i++) {
            ch[i] = Integer.parseInt(String.valueOf(str.charAt(i)));
        }

        Arrays.sort(ch, Collections.reverseOrder());

        System.out.println(Arrays.toString(ch));

        for (int i : ch) {

            fNum += i;
        }
        return Integer.parseInt(fNum);
    }
}
