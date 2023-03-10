import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static String[] DNAstring = new String[30];
    static double k;
    public static void main(String[] args) {

        StringBuilder stringBuilder = new StringBuilder();
        String filepath = "/Users/mad_hatter/Downloads/rosalind_gc.txt";

        try {
        Scanner scanner = new Scanner(new File(filepath));
        while(scanner.hasNextLine()) {
            String line = scanner.nextLine();
            stringBuilder.append(line);
        }
        scanner.close();

        String file = stringBuilder.toString();

        System.out.println(Arrays.toString(getSingleStrings(file)));
        System.out.println(Arrays.toString(computeGC_ratios(getSingleStrings(file))));

        k = computeGC_max(computeGC_ratios(getSingleStrings(file)));
        System.out.println(k);

            // Why does this not work - I want to check what the index of the max GC ratio is and compare it to the indices of the single strings to get the right ID
            for(int i = 0; i < 11; i++) {
                if(k/100 == (computeGC_ratios(getSingleStrings(file))[i]))
                    System.out.println(i);
            }

    } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static String [] getSingleStrings(String g) {
            DNAstring = g.split("[> ]");
    return DNAstring;
    }

    public static double [] computeGC_ratios(String [] g) {

        double [] GC_ratios = new double[11];
        int GC_sum = 0;
        String [] IDs = new String[10];



        for(int j = 1; j < g.length; j++) {
            for(int l = 0; l < g[j].length(); l++) {
                int k = "Rosalind_0808".length();
                if(g[j].charAt(l) == ('C') || g[j].charAt(l) == 'G')
                    GC_sum++;
            }
            if(g[j].length() != 0)
                GC_ratios[j] = (double)GC_sum/(((g[j]).length()) - k);
            GC_sum = 0;
        }

        return GC_ratios;}

    public static double computeGC_max(double [] d) {
        double [] sortedArray = Arrays.stream(d).sorted().toArray();
        return sortedArray[sortedArray.length-1] * 100;
    }
}