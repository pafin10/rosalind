
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;


public class Consensus_and_profile {

    public static List<String> getMatrix(String fastaString) {
        List<String> string_matrix = new ArrayList<>();
        StringBuilder stringBuilder = new StringBuilder();
        String collection = " ";
        int i = 0;
        int lastIndex = 0;

        // Read in Fasta File and build String with only the sequences
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(fastaString));
            String line = bufferedReader.readLine();

            while(line != null) {
                if(!line.startsWith(">")) {
                    stringBuilder.append(line.trim());
                }
                else {
                    if(stringBuilder.length() > 0) {
                        string_matrix.add(stringBuilder.toString());
                        stringBuilder.setLength(0);
                    }
                }
                line = bufferedReader.readLine();
            }
            // add the last sequence to the matrix
            if(stringBuilder.length() > 0) {
                string_matrix.add(stringBuilder.toString());
        }

            // convert string to ArrayList, with each sequence as one element
        while(i < collection.length()) {
            if(Character.isWhitespace(collection.charAt(i))) {
                String substring = collection.substring(lastIndex, i);
                lastIndex = i;
                if(!substring.isEmpty()) {
                    string_matrix.add(substring.trim());
                }
            }
            i++;
        }

    return string_matrix;}

        catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


        public static String getProfileMatrixnConsensusString(List<String> stringMatrix) {
        String counts;
        int j, i = 0;
        int a_count = 0, c_count = 0,g_count = 0, t_count = 0;
        String A, C, G, T;
        StringBuilder stringBuilder = new StringBuilder();

        List<Integer> a_counts = new ArrayList<>();
        List<Integer> c_counts = new ArrayList<>();
        List<Integer> g_counts = new ArrayList<>();
        List<Integer> t_counts = new ArrayList<>();
        List<Integer> values = new ArrayList<>();
        List<Character> consensus_chars = new ArrayList<>();

        for(j = 0; j < stringMatrix.get(0).length(); j++) {
            a_count = 0;
            c_count = 0;
            g_count = 0;
            t_count = 0;
            for(String sequence: stringMatrix) {
                if(!Character.isWhitespace(sequence.charAt(j))) {
                    if(sequence.charAt(j) == 'A')
                        a_count++;
                    if(sequence.charAt(j) == 'C')
                        c_count++;
                    if(sequence.charAt(j) == 'G')
                        g_count++;
                    if(sequence.charAt(j) == 'T')
                        t_count++;
                }
            }
            a_counts.add(a_count);
            c_counts.add(c_count);
            g_counts.add(g_count);
            t_counts.add(t_count);
        }
        System.out.println("Counts for column " + j + ": A=" + a_count + ", C=" + c_count + ", G=" + g_count + ", T=" + t_count);

        for(int k = 0; k < a_counts.size(); k++) {
            //clear lists at beginning of each iteration!
            //consensus_chars.clear();
            values.clear();

            values.add(a_counts.get(k));
            values.add(c_counts.get(k));
            values.add(g_counts.get(k));
            values.add(t_counts.get(k));

            int max = Collections.max(values);

            if(max == a_counts.get(k)) {
                consensus_chars.add('A');
            }
            else if(max == c_counts.get(k)) {
                consensus_chars.add('C');
            }
            else if(max == g_counts.get(k)) {
                consensus_chars.add('G');
            }
            else if(max == t_counts.get(k)) {
                consensus_chars.add('T');
            }
        }

        StringBuilder stringBuilder1 = new StringBuilder();

        for(Character c: consensus_chars) {
            stringBuilder1.append(c);
        }


        for(Integer element: a_counts) {
            stringBuilder.append(element).append(" ");
        }
        A = stringBuilder.toString();
        stringBuilder.setLength(0);

        for(Integer element: c_counts) {
            stringBuilder.append(element).append(" ");
        }
        C = stringBuilder.toString();
        stringBuilder.setLength(0);

        for(Integer element: g_counts) {
            stringBuilder.append(element).append(" ");
        }
        G = stringBuilder.toString();
        stringBuilder.setLength(0);

        for(Integer element: t_counts) {
            stringBuilder.append(element).append(" ");
        }
        T = stringBuilder.toString();
        stringBuilder.setLength(0);

        String consensus = stringBuilder1.toString();
        counts = consensus + "\n" + "A: " + A + "\n" + "C: " + C + "\n" + "G: " + G + "\n" + "T: " + T + "\n";

        return counts;
    }

    public static void main(String[] args) {
        System.out.println(getProfileMatrixnConsensusString(getMatrix("/Users/mad_hatter/IdeaProjects/Rosalind/src/txt_files/rosalind_cons.txt")));
    }



}
