import static java.lang.Float.sum;

public class Mendels_First_Law {

    // we want to calculate the probability that any two individuals of a population given by k + m + n organisms possess a dominant allele.
    // k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.


    static double calculate_probability(int k, int m, int n) {
        // if first organism is k, second may be any
        double probability_first_k = (double)(k)/(k+m+n);
        // if first organism is m and second is k, offspring has dominant allele
        // if first organism is m and second is n, there is a 1 in 2 chance, given first is m, that offspring has dominant allele
        // if first and second organism is m, there is a 3 in 4 chance, given first is m, that offspring has dominant allele
        double probability_first_m = (double)(m)/(k+m+n) * (double)(k)/(k+m+n-1) + (double)(m)/(k+m+n) * ((double)(n)/(k+m+n-1))/2 + (double)(m)/(k+m+n) * ((double)(m-1)/(k+m+n-1))*0.75;
        // if first organism is n and second is k, offspring has dominant allele
        // if first organism is n and second is m, there is a 1 in 2 chance, given first is n, that offspring has dominant allele
        double probability_first_n = (double)(n)/(k+m+n) * (double)(k)/(k+m+n-1) + (double)(n)/(k+m+n) * ((double)(m)/(k+m+n-1))/2;
        return  probability_first_m + probability_first_k + probability_first_n;
    }

    public static void main(String[] args) {
        System.out.println(calculate_probability(22, 30, 27));
    }
}
