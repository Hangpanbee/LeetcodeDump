class Solution {
    public int calPoints(String[] ops) {
        
        Stack<Integer> stk = new Stack();  
        for (String op: ops) {
            //System.out.println(op);
            if (op.equals("C")) {
                stk.pop();
            } else if (op.equals("D")) {
                //System.out.println(op);
                stk.push(stk.peek() * 2);
            } else if (op.equals("+")) {
                int num1 = stk.pop();
                int num2 = stk.peek();
                //System.out.println(num2);
                stk.push(num1);
                stk.push(num2+num1);
        
            } else {
                //System.out.println(op);
                stk.push(Integer.parseInt(op));
            };
      };
        
    int sum = 0;
    while (stk.size() > 0) {
        int pop= stk.pop();

        sum += pop;
    };
    
    return sum;
        
    };
};