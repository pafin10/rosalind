import java.util.ArrayList;
import java.util.List;

public class Finding_a_motiv {

    public static String find_substring_locations(String s, String t) {
        // for all substrings of length t in s, check whether s.substring is equal to t. If true return substring[0].
        List<String> s_substrings = new ArrayList<>();
        List<Integer> positions = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < s.length() - t.length(); i ++) {
            s_substrings.add(i, s.substring(i, t.length() + i));
        }

        // index of substring in array is now equal to index of first appearance of searched sequence in string s
        for(int j = 0; j < s_substrings.size(); j++) {
                if(s_substrings.get(j).equals(t)) {
                    positions.add(j + 1);
        }}
        for(Integer position:positions) {
            sb.append(position + " ");
        }

    return sb.toString();}

    public static void main(String[] args) {
        System.out.println(find_substring_locations("TATCGCTTGAGCATCAGTCTTGAGCCCCCTTGAGCGTACTTGAGCCTTGAGCCTTGAGCCTTGAGCCCGTGAACTTGAGCCCTTGAGCCCTTGAGCTGCCCTTGAGCGCTTGAGCACTTGAGCAAACCCTTGAGCTGAGCACTTGAGCTCTTGAGCTCTTGAGCTCTTCCTTGAGCACGCTTGAGCACTTGAGCGCTTGAGCTCCCCTTGAGCCACTTGAGCATCACTTGAGCACCTTGAGCAGCTTGAGCGCCGCCAGACGCTTGAGCGTATCGTCTTGAGCCTTGAGCATACTCGATTTCCTTGAGCCTTGAGCCTTGAGCTTCTTGAGCTACTACTTGAGCCTTGAGCCTTGAGCCTTGAGCGCTTGAGCCTTGAGCACACTTGAGCACCTTGAGCGTTCCGTCCAACTTGAGCCTTGAGCGTAACTTTCCTTGAGCAAACTTGAGCACCTCTTGAGCCTTGAGCAGTTCTTGAGCCGCCTTGAGCGGCTTGAGCTATATAAATCTTGAGCCATTCCTTGAGCCTTGAGCCTTGAGCCTTGAGCGCTTGAGCCTTGAGCTGGGTTCTTGAGCTCACTTGAGCATATCTCTTGAGCCCTTGAGCTCTTGAGCGACCAGGGGCTTGAGCCTTGAGCGGTATCTTGAGCCTCGTCTTGAGCCGGCTTGAGCCTTGAGCTCTTGAGCCCGCGAGCTTGAGCCCTTGAGCTACTACTTGAGCGCTCGTTCCCGCTTGAGCCTTGAGCCAAGCTTGAGCCTACTTGAGCCTTGAGCCCTTGAGCCTTGAGCCTTGAGCATTCTTGAGCCCTTGAGCCCTTGAGCCGGCGCTCCGCTTGAGCCTTGAGCCTTGAGCCTTGAGCCGTCTTGAGCCTTGAGCAGTCTTGAGCCGCTTGAGCCCTTGAGCACCTTGAGCACCTTGAGCCCTTGAGCCCGCTTGAGCCTTGAGCCGATTC\n"
                , "CTTGAGCCT"));
    }
}
