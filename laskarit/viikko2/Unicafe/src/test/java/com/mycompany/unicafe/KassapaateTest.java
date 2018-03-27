package com.mycompany.unicafe;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

public class KassapaateTest {
    
    Kassapaate paate;
    
    @Before
    public void setUp() {
        this.paate = new Kassapaate();
    }
    
    @Test
    public void alkuSaldoOikein() {
        assertTrue(this.paate.kassassaRahaa()==100000);
    }
    @Test
    public void syoEdullisestiTarpeeksiSaldoa() {
        assertTrue(this.paate.syoEdullisesti(260)==20);
    }
    @Test
    public void syoEdullisestiEiTarpeeksiSaldoa() {
        assertTrue(this.paate.syoEdullisesti(130)==130);
    }
    @Test
    public void syoEdullisestiAnnosSaldoKasvaa() {
        this.paate.syoEdullisesti(300);
        assertTrue(this.paate.edullisiaLounaitaMyyty()==1);
    }
    @Test
    public void syoMaukkaastiTarpeeksiSaldoa() {
        assertTrue(this.paate.syoMaukkaasti(460)==60);
    }
    @Test
    public void syoMaukkaastiEiTarpeeksiSaldoa() {
        assertTrue(this.paate.syoMaukkaasti(130)==130);
    }
    @Test
    public void syoMaukkaastiAnnosSaldoKasvaa() {
        this.paate.syoMaukkaasti(500);
        assertTrue(this.paate.maukkaitaLounaitaMyyty()==1);
    }
    @Test
    public void syoEdullisestiKortillaTarpeeksiSaldoa() {
        Maksukortti kortti = new Maksukortti(260);
        assertTrue(this.paate.syoEdullisesti(kortti));
    }
    @Test
    public void syoEdullisestiKortillaEiTarpeeksiSaldoa() {
        Maksukortti kortti = new Maksukortti(130);
        assertFalse(this.paate.syoEdullisesti(kortti));
    }
    @Test
    public void syoEdullisestiKortillaAnnosSaldoKasvaa() {
        Maksukortti kortti = new Maksukortti(260);
        this.paate.syoEdullisesti(kortti);
        assertTrue(this.paate.edullisiaLounaitaMyyty()==1);
    }
    @Test
    public void syoMaukkaastiKortillaTarpeeksiSaldoa() {
        Maksukortti kortti = new Maksukortti(460);
        assertTrue(this.paate.syoMaukkaasti(kortti));
    }
    @Test
    public void syoMaukkaastiKortillaEiTarpeeksiSaldoa() {
        Maksukortti kortti = new Maksukortti(260);
        assertFalse(this.paate.syoMaukkaasti(kortti));
    }
    @Test
    public void syoMaukkaastiKortillaAnnosSaldoKasvaa() {
        Maksukortti kortti = new Maksukortti(500);
        this.paate.syoMaukkaasti(kortti);
        assertTrue(this.paate.maukkaitaLounaitaMyyty()==1);
    }
    @Test
    public void lataaPositiivinenSummaKortille() {
        Maksukortti kortti = new Maksukortti(500);
        this.paate.lataaRahaaKortille(kortti, 1000);
        assertTrue(kortti.saldo()==1500);
    }
    @Test
    public void lataaNegatiivinenSummaKortille() {
        Maksukortti kortti = new Maksukortti(500);
        this.paate.lataaRahaaKortille(kortti, -1000);
        assertTrue(kortti.saldo()==500);
    }
}
