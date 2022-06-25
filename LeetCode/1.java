class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> indexMap = new HashMap<Integer,Integer>();
        for(int i=0; i<nums.length; i++){
            Integer required = (Integer)(target - nums[i]);
            if(indexMap.containsKey(required)){
                int toReturn[] = {indexMap.get(required), i};
                return toReturn;
            }
            indexMap.put(nums[i], i);
        }
        return null;
    }
}
