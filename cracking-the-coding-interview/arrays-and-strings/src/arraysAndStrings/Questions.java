package arraysAndStrings;

class Questions {

    //Neste problema, considerei o espaço como caractere válido.
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

    public boolean isUniqueCharsTwoBook(String str) {
        int checker = 0; 
        
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i) - 'a';

            if ((checker & (1 << val)) > 0) {
                return false;
            }
            checker |= (1 << val);
        }
        return true;
    }

    // Para este problema, assumi que Banana == ANBANA é verdadeiro.
    // Removendo toUpperCase(), Banana == ANBANA retorna falso.
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
