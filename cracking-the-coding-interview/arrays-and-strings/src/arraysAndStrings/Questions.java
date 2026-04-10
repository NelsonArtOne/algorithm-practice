package arraysAndStrings;
 
class Questions {

    public boolean isUnique(String string) {
        string = string.toUpperCase();
        int stringSize = string.length();

        for (int i = 0; i < stringSize - 1; i++) {
            for (int j = i + 1; j < stringSize; j++) {
                if (string.charAt(i) == string.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean isUniqueChars(String str) {
        if (str.length() > 128) return false;

        boolean[] char_set = new boolean[128];

        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i); 

            if (char_set[val]) {
                return false;
            }
            char_set[val] = true;
        }
        return true;
    }
}
