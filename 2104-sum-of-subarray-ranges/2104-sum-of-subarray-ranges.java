class Solution {
    public long subArrayRanges(int[] nums) {
    // How many subarrays where the current value is the max 
    //     8  7  3  4           8 7 3 4
    //PLE [8  7  3  3]          [8] [7] [3] [4]
    //PLaE[8  8  7  7]          [8,7] [7,3] [3,4]
    //NLE [7  3  3  4]          [8,7,3] [7,3,4]
    //NLaE[8  7  4  3]          [8,7,3,4]
    // 8*4 + 7*3 + 3 + 4*2 = 32+21+3+8 = 64 
    // 8+7*2+3*6+4*1 = 8+14+18+4=44 
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        ArrayDeque<Integer> deStack = new ArrayDeque<>();
        int[] PLE = new int[nums.length];
        Arrays.fill(PLE, -1);
        int[] NLE = new int[nums.length];
        Arrays.fill(NLE, nums.length);
        int[] PLaE = new int[nums.length];
        Arrays.fill(PLaE, -1);
        int[] NLaE = new int[nums.length];
        Arrays.fill(NLaE, nums.length);
        for (int i = 0; i < nums.length; i++) {
            // i = 8
            // i = 7
            // i = 3
            // i = 4
            while (!stack.isEmpty() && nums[stack.peekLast()] > nums[i]) {
                stack.pollLast();
            }
            // stack = []
            while (!deStack.isEmpty() && nums[deStack.peekLast()] < nums[i]) {
                deStack.pollLast();
            } 
            // deStack = [0,1,2]
            
            if (!stack.isEmpty()) {
                PLE[i] = stack.peekLast();
            }
            //PLE = [-1,-1,-1,2]
            if (!deStack.isEmpty()) {
                PLaE[i] = deStack.peekLast();
            }
            //PLaE = [-1,0,1,4]
            //stack=[0], deStack=[0]
            //stack=[1], deStack=[0,1]
            //stack=[2]
            stack.add(i);
            deStack.add(i);
        }
        stack = new ArrayDeque<>();
        deStack = new ArrayDeque<>();
        for (int i = nums.length-1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peekLast()] >= nums[i]) {
                stack.pollLast();
            }
            
            while (!deStack.isEmpty() && nums[deStack.peekLast()] <= nums[i]) {
                deStack.pollLast();
            }
            
            if (!stack.isEmpty()) {
                NLE[i] = stack.peekLast();
            }
            
            if (!deStack.isEmpty()) {
                NLaE[i] = deStack.peekLast();
            }
            
            stack.add(i);
            deStack.add(i);
        }
        //      [8,  7, 3, 4]
        //PLE   [-1,-1,-1, 2]
        //NLE   [ 1, 2, 4, 4]
        //PLaE  [-1, 0, 1, 1]
        //NLaE  [ 4, 4, 3, 4]
        // La: 8*1*4 + 7*3 + 3*1*1 + 4*2*1 = 32+21+3+8
        // 
        long sumLargest = 0;
        long sumSmallest = 0;
        for (int i = 0; i < nums.length; i++) {
            sumLargest += (long) nums[i]*(i-PLaE[i])*(NLaE[i]-i);
            sumSmallest += (long) nums[i]*(i-PLE[i])*(NLE[i]-i);
        }
        //System.out.println(Arrays.toString(NLaE));
        //System.out.println(sumLargest);
        return (long) sumLargest-sumSmallest;
    }
}