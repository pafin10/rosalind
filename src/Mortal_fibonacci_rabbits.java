import java.util.ArrayList;
import java.util.List;

public class Mortal_fibonacci_rabbits {

    public static long fib_mortal(int n_months_passed, int m_months_alive) {

        long youngsters_prev = 0;
        long grown_ups_prev = 0;
        long oldies_prev = 0;
        long youngsters = 1;
        long grown_ups = 0;
        long oldies = 0;
        long sum = 0;
        List<Long> timeline = new ArrayList<>();

        // How many rabbits will live AFTER n months, so the first number of the sequence has index 0. Thus return b.
        // in jeder Generation: Summe ist gleich Summe aus vorheriger Generation: Junge + 2* Ausgewachsen + Ausgewachsen_3, wobei in Generation t:
        // Ausgewachsen_t = Junge_t-1, Ausgewachsen_3_t = Ausgewachsen_t, Junge = Ausgewachsen_3_t + Ausgewachsen


    // code works, but still integer overflow for large values - see BigInteger class
        for(int counter = 1; counter <= n_months_passed; counter++) {

            if(counter == 1) {
                timeline.add(youngsters);
                grown_ups = youngsters;
                youngsters_prev = 1;
                youngsters = 0;
            }
            else {
                grown_ups = youngsters_prev;
                oldies += grown_ups_prev;
                youngsters = oldies_prev + grown_ups_prev;
                timeline.add(youngsters);
                // the oldies from the previous iteration have reproduced and are ready to die

                if(counter > m_months_alive) {
                    // Remove the rabbits that are m months old;
                    oldies -= timeline.get(counter - 1 - m_months_alive);
                }
                grown_ups_prev = grown_ups;
                youngsters_prev = youngsters;
                oldies_prev = oldies;
            }
          }
        sum = youngsters + grown_ups + oldies;

        return sum;}

    // Problem: rabbits now die after m months
    // We must do two things: 1. adjust the variables for the fact that a rabbit pair has died (after m months of life)
    // 2. modify the loop such that

    public static void main(String[] args) {
        System.out.println(fib_mortal(92, 16));
    }
}
