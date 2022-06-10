class Solution {
    String s;
   
public String shortestPalindrome(String s) {
        StringBuilder res = new StringBuilder();
        int j=0, end = s.length();
        // aacecaaa j = 0 end = 8
        // ababba j = 0 end = 6
        while(true){
            j=0;
            // j = 0
            for(int i=end-1;i>=0;i--){
                // i = 5
                // i = 4
                if(s.charAt(i) == s.charAt(j)) j++;
                // j = 1, j = 2
            }
            if(j==end) break;
            end = j;
            // end = 2
        }
        //tringBuilder firstPart = new StringBuilder().append(s.substring(end, s.length())).reverse();
        //System.out.println(firstPart);
        res.append(s.substring(end, s.length())).reverse().append(s.substring(0, end)).append(s.substring(end, s.length()));
        return res.toString();
    }
        
    
}