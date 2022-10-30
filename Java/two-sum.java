import java.util.*;;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> passed = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            int diff = target-n;
            
            if (passed.containsKey(diff)) {
                return new int[] {i, passed.get(diff)};
            }

            passed.put(n, i);
        }
        return new int[] {};
    }
}