package com.example;
 
import org.junit.Test;
import static org.junit.Assert.*;
 
public class MyTest {
    @Test
    public void testAddition() {
        int result = Calculator.add(2, 2);
        assertEquals(4, result);
    }
}
