import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static String[] DNAstring = new String[30];
    static double k;

    public static void main(String[] args) {

        StringBuilder stringBuilder = new StringBuilder();
        String filepath = "/Users/mad_hatter/Downloads/rosalind_gc-3.txt";

        try {
            Scanner scanner = new Scanner(new File(filepath));
            while(scanner.hasNextLine()) {
                String line = scanner.nextLine();
                stringBuilder.append(line);
            }

            scanner.close();

            String file = stringBuilder.toString();

            // save sequences with IDs in a string array
            String [] singleStrings;
            singleStrings = getSingleStrings(file);

            // compute index of highest GC ratio
            double [] gc_ratios = computeGC_ratios(getSingleStrings(file));
            int r = getMaxIndex(gc_ratios);
            System.out.println(r);

            // use index to search for correct String in singleStrings and cut out ID
            String maxGC_String = singleStrings[r];
            String maxGC_ID = maxGC_String.substring(0, "Rosalind_0292".length());

            // print array with unordered GC ratios
            System.out.println(Arrays.toString(computeGC_ratios(singleStrings)));


            // compute maximum GC ratio
            k = computeGC_max(computeGC_ratios(getSingleStrings(file)));

            // return maximum GC ratio and ID of corresponding string
            System.out.println(maxGC_ID);
            System.out.println(k);
        }
        catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static String [] getSingleStrings(String g) {
            DNAstring = g.split("[> ]");
    return DNAstring;
    }

    public static int getMaxIndex(double[] d) {
        int u = 0;
        for(int i = 1; i < (d.length); i++) {
            if((d[i]) > d[u])
                u = i;}
    return u;}

    public static double [] computeGC_ratios(String [] g) {

        double [] GC_ratios = new double[11];
        int GC_sum = 0;
        int h = "Rosalind_0808".length();

        for(int j = 0; j < g.length; j++) {
            for(int l = 0; l < g[j].length(); l++) {
                if(g[j].charAt(l) == ('C') || g[j].charAt(l) == 'G')
                    GC_sum++;
            }
            System.out.println(GC_sum);
            if(g[j].length() != 0)
                GC_ratios[j] = (double)GC_sum/((g[j]).length() - h);
            GC_sum = 0;
        }
        return GC_ratios;
    }

    public static double computeGC_max(double [] d) {
        double [] sortedArray = Arrays.stream(d).sorted().toArray();
        return sortedArray[sortedArray.length-1] * 100;
    }
}