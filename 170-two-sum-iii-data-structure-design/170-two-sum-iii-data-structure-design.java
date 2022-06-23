class TwoSum {
    // twoSum(2) twoSum(2) -> find(4)
    TreeMap<Integer, Integer> twoSum;
    public TwoSum() {
        twoSum = new TreeMap<>();
    }
    
    public void add(int number) {
        twoSum.put(number, twoSum.getOrDefault(number, 0) + 1);
    }
    
    public boolean find(int value) {
        
        for (Map.Entry<Integer, Integer> m: twoSum.entrySet()) {
            int target = value - m.getKey();
            
            if (target == m.getKey()) {
                if (twoSum.get(target) >= 2) return true;
                else return false;
            } else if (twoSum.containsKey(target))
                return true;
        }
        return false;
            
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */