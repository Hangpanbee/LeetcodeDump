class Solution {
    public int minDeletions(String s) {
        
        HashMap<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            counter.put(s.charAt(i), counter.getOrDefault(s.charAt(i), 0) + 1);
        };
        
        
        int[] bucketSort = new int[s.length()+1];
        for (Map.Entry<Character, Integer> count: counter.entrySet() ) {
            bucketSort[count.getValue()] += 1;
        };
        
        //System.out.println(Arrays.toString(bucketSort));
        int ans = 0;
        Stack<Integer> availIndex = new Stack<>();
        for (int i = 0; i < bucketSort.length; i++) {
            if (bucketSort[i] == 0) {
                availIndex.add(i);
            } else if (bucketSort[i] > 1) {
                
                while (bucketSort[i] > 1) {
                    if (!availIndex.isEmpty()) ans += i - availIndex.pop();
                    else ans += i;
                    bucketSort[i] -= 1;
                }
            };
        };
        
        return ans;
        
    }
}