class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] persons) {
        // differences between a TreeMap and a HashMap (sorted right away)
        
        TreeMap<Integer, Integer> prefixMap = new TreeMap<>();
        int[] ans = new int[persons.length];
        
  
        for (int i=0; i < flowers.length; i++) {
            int prevFlowersStart = prefixMap.getOrDefault(flowers[i][0], 0);
            int prevFlowersEnd = prefixMap.getOrDefault(flowers[i][1]+1, 0);
            prefixMap.put(flowers[i][0], prevFlowersStart + 1);
            prefixMap.put(flowers[i][1]+1, prevFlowersEnd - 1);
            //System.out.println(flowers[i][1]);
 

        };
        TreeMap<Integer, Integer> sumMap = new TreeMap<>();
        int runningSum = 0;
        for (Map.Entry<Integer, Integer> sumFlowers: prefixMap.entrySet() ) {
            runningSum += sumFlowers.getValue();
            sumMap.put(sumFlowers.getKey(), runningSum);
            
        }
        
        //System.out.println(sumMap);
        for (int i = 0; i < persons.length; i++) {
            //System.out.println(sumMap.floorEntry(persons[i]));
            Map.Entry<Integer, Integer> floorKey = sumMap.floorEntry(persons[i]);
            if (floorKey == null) {
                ans[i] = 0;
            } else {
                ans[i] = floorKey.getValue();
            }

        }
        
        
        return ans;   
    }
}