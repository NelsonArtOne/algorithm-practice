package arraysAndStrings;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class TestQuestions {
    
    @Test
    public void isUniqueCharsTrue() {
        Questions q = new Questions();
        String string = "Bom dia";
        boolean myAnswer = q.isUniqueChars(string);
        boolean bookAnswer = q.isUniqueCharsBook(string); 
    
        assertTrue(myAnswer);
        assertTrue(bookAnswer);
    }

    @Test
    public void isUniqueCharsFalse() {
        Questions q = new Questions();
        String string = "Batata";
        boolean myAnswer = q.isUniqueChars(string); 
        boolean bookAnswer = q.isUniqueCharsBook(string);

        assertFalse(myAnswer); 
        assertFalse(bookAnswer);
    }

    @Test
    public void isPermutationTrue() {
        String string = "Banana";
        String permut = "Anbana";
        
        Questions q = new Questions();
        boolean myAnswer = q.isPermutation(string, permut);

        assertTrue(myAnswer);
    }

    @Test
    public void isPermutationFalse() {
        String string = "Banana";
        String permut = "Abbana";
        
        Questions q = new Questions();
        boolean myAnswer = q.isPermutation(string, permut);

        assertEquals(false, myAnswer);
    }
    
}