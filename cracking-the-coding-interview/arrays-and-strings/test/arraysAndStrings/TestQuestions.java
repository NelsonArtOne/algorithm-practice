package arraysAndStrings;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestQuestions {
    
    @Test
    public void isUniqueChars() {
        Questions q = new Questions();
        String string = "Bom dia";

        boolean myAnswer = q.isUniqueChars(string);
        boolean bookAnswer = q.isUniqueCharsBook(string); 
    
        assertEquals(true, myAnswer);
        assertEquals(true, bookAnswer);
    }

    @Test
    public void isNotUniqueChars() {
        Questions q = new Questions();
        String string = "Batata";

        boolean myAnswer = q.isUniqueChars(string); 
        boolean bookAnswer = q.isUniqueCharsBook(string);

        assertEquals(false, myAnswer);
        assertEquals(false, bookAnswer);
    }

    @Test
    public void isPermutation() {
        String string = "Banana";
        String permut = "Anbana";
        
        Questions q = new Questions();
        boolean myAnswer = q.isPermutation(string, permut);

        assertEquals(true, myAnswer);
    }

    @Test
    public void isNotPermutation() {
        String string = "Banana";
        String permut = "Abbana";
        
        Questions q = new Questions();
        boolean myAnswer = q.isPermutation(string, permut);

        assertEquals(false, myAnswer);
    }

    @Test
    public void isPermutationDifferentSize() {
        String string = "Banana";
        String permut = "Anbanaa";
        
        Questions q = new Questions();
        boolean myAnswer = q.isPermutation(string, permut);

        assertEquals(false, myAnswer);
    }

    @Test
    public void isPermutationUpperCase() {
        String string = "Banana";
        String permut = "ANBANA";
        
        Questions q = new Questions();
        boolean myAnswer = q.isPermutation(string, permut);

        assertEquals(true, myAnswer);
    }

    @Test
    public void isPermutationSum() {
        String string = "bc";
        String permut = "ad";
        
        Questions q = new Questions();
        boolean myAnswer = q.isPermutation(string, permut);

        assertEquals(false, myAnswer);
    }

}