import java.util.Enumeration;
import java.util.Hashtable;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, Integer> hashtable = new Hashtable<>();
        int[] res = new int[2];
        for(int i=0;i<nums.length;i++){
            if(hashtable.containsKey(target-nums[i])){
                res[0]=hashtable.get(target-nums[i]);
                res[1]=i;
            }
            hashtable.put(nums[i],i);
        }
        return res;
    }
}