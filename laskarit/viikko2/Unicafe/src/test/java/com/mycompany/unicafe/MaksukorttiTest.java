package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(10);
    }
    
    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }
    @Test
    public void saldoAlussaOikein() {
        assertTrue(this.kortti.saldo()==10);
    }
    @Test
    public void lataaminenKasvattaaSaldoaOikein() {
        this.kortti.lataaRahaa(13);
        assertTrue(this.kortti.saldo()==23);
    }
    @Test 
    public void rahanOttaminenToimiiKunTarpeeksiSaldoa() {
        assertTrue(this.kortti.otaRahaa(3));
    }
    @Test
    public void saldoEiMuutuKunRahaaEiTarpeeksi() {
        assertFalse(this.kortti.otaRahaa(100));
    }
    @Test
    public void toStringMetodiOikein() {
        this.kortti.lataaRahaa(145);
        assertEquals("saldo: " + this.kortti.saldo()/100 + "." 
                + this.kortti.saldo()%100, this.kortti.toString());
    }
}
