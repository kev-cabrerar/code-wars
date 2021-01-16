package Java;

public class Multiples_of_3_or_5 {

    public int solution(int number) {
        var sum = 0;

        for (int x = number - 1; x >= 0; x--) {
            if (x % 3 == 0 && x % 5 == 0) {
                sum += x;
            }

            else if (x % 3 == 0) {
                sum += x;
            }

            else if (x % 5 == 0) {
                sum += x;
            }

        }

        return sum;
    }
}