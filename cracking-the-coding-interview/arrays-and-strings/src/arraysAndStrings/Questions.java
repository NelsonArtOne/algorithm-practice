package arraysAndStrings;

class Questions {

    public boolean isUniqueChars(String string) {
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

    public boolean isUniqueCharsBook(String str) {
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

    // Para este problema, assumi que Banana == ANBANA é verdadeiro.
    public boolean isPermutation(String string, String permut) {
        if (string.length() != permut.length()) return false;
        
        string = string.toUpperCase();
        permut = permut.toUpperCase(); 

        int[] array = new int[128];

        for (int i = 0; i < string.length(); i++) {
            array[string.charAt(i)] += 1; 
        }

        for (int i = 0; i < permut.length(); i++) {
            if(array[permut.charAt(i)] == 0) return false;
            array[permut.charAt(i)] -= 1;
        }
        return true;
    }
}
