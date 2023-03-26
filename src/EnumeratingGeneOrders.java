import java.util.*;

public class EnumeratingGeneOrders {

    public static int permutationCount(int i) {
        if(i == 1)
            return i;
        else return i*permutationCount(i-1);
        }

    public static List<List<Integer>> generatePermutations(List<Integer> nums) {
        List<List<Integer>> result = new ArrayList<>();
        generatePermutationsHelper(nums, new ArrayList<>(), result);
        return result;
    }

    private static void generatePermutationsHelper(List<Integer> nums, List<Integer> permutation, List<List<Integer>> result) {
    if(nums.isEmpty()) {
        result.add(permutation);
    } else {
        for(int i = 0; i < nums.size(); i++) {
            // we subsequently select one integer from the original list to create all permutations
            // which include that integer
            List<Integer> newNums = new ArrayList<>(nums);
            newNums.remove(i);
            // creates new empty list in first iteration
            // thereafter, current values of permutation are copied into a new list newPermutation
            List<Integer> newPermutation = new ArrayList<>(permutation);
            newPermutation.add(nums.get(i));
            generatePermutationsHelper(newNums, newPermutation, result);
        }
    }
}
    public static List<Integer> generateList(int i) {
        int k = 0;
        Integer[] numbers = new Integer[i];

        while(k < i) {
            numbers[k] = k+1;
            k++;
        }

        List<Integer> list = new ArrayList<>(Arrays.asList(numbers));
    return list;}

    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(generateList(5));
        List<List<Integer>> permutations = generatePermutations(nums);
        System.out.println(permutations);
        System.out.println(permutations.size());

    }
}
