package arraysAndStrings;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestQuestions {
    
    @Test
    public void isUniqueTrue() {
        Questions q = new Questions();
        boolean result = q.isUnique("Bom dia");

        assertEquals(true, result);
    }

    @Test
    public void isUniqueFalse() {
        Questions q = new Questions();
        boolean result = q.isUnique("Batata"); 

        assertEquals(false, result);
    }
    
}