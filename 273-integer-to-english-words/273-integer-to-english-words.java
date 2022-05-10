class Solution {
        private final HashMap<Integer, String> to10 = new HashMap<>() {{put(1, "One"); put(2, "Two"); put(3, "Three"); put(4, "Four"); put(5, "Five"); put(6, "Six"); put(7, "Seven"); put(8, "Eight"); put(9, "Nine");}};
        private final HashMap<Integer, String> to20 = new HashMap<>(){{put(10, "Ten"); put(11, "Eleven"); put(12, "Twelve"); put(13, "Thirteen"); put(14, "Fourteen"); put(15, "Fifteen"); put(16, "Sixteen"); put(17, "Seventeen"); put(18, "Eighteen"); put(19, "Nineteen");}};  
        private final HashMap<Integer, String> to100 = new HashMap<>(){{put(20, "Twenty"); put(30, "Thirty"); put(40, "Forty"); put(50, "Fifty"); put(60, "Sixty"); put(70, "Seventy"); put(80, "Eighty"); put(90, "Ninety");}};

    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        
        HashMap<Integer, String> toInfinite = new HashMap<>(){{put(0, ""); put(1, "Thousand"); put(2, "Million"); put(3, "Billion"); put(4, "Trillion");}};
        ArrayList<String> ans = new ArrayList<>();
        int length = (num == 0) ? 1 : (int)Math.log10(num) + 1;
        int comma = Math.floorDiv(length, 3);
        int currNum;
        if (comma == 3) {
            currNum = num/1000000000;
            if (currNum > 0) {
            ans.add(to10.get(num/1000000000));
            ans.add("Billion");
            num %= 1000000000;
            comma--;
            }
        }
        while (comma >= 0) {
            num = num % (int)(Math.pow(10, (int) 3*(comma+1)));
            
            if (comma > 0) 
                {currNum = num/(int) Math.pow(10, 3*comma);}
            else {currNum = num;};

            if (currNum > 0) {
                hundredNumberToWords(currNum, ans);
                if (comma > 0) ans.add(toInfinite.get(comma));
            }
            comma -= 1;
         
        
        };
        //System.out.println(ans.toString());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            String space = " ";

            if (i == (ans.size()-1) ) {
                space = "";
            };
            sb.append(ans.get(i));
            sb.append(space);
        };
      
        
        return sb.toString();
        
    }
    
    private List<String> hundredNumberToWords(int num, ArrayList<String> ans) {
        int currNum;
        currNum = Math.floorDiv(num, 100);
        if (currNum > 0) {
            ans.add(to10.get(currNum));
            ans.add("Hundred");
        };
        currNum = num%100;
        if (0 < currNum && currNum < 10) {
            ans.add(to10.get(currNum));
        } else if (currNum == 0) {
            ;
        } else if (currNum < 20) {
            ans.add(to20.get(currNum));
        } else {
            int currNum1 = Math.floorDiv(currNum, 10)*10;
            //System.out.println(currNum1);
            ans.add(to100.get(currNum1));
            currNum = currNum%10;
           // System.out.println(currNum);
            if (currNum > 0) {
                ans.add(to10.get(currNum));
            };
        };
        
        return ans;  
    };
}