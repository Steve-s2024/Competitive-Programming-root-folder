//100%
class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] words = text.split(" ");
        ArrayList<String> ans = new ArrayList<>();
        for (int i = 2; i < words.length; i++) {
            if (words[i-1].equals(second) && words[i-2].equals(first)) ans.add(words[i]);
        }
        String [] res = new String[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i); 
        return res;
    }
}