import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

public class MaksukorttiTest {
    
    Maksukortti kortti;
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
        kortti = new Maksukortti(10); 
    }
    
    @After
    public void tearDown() {
    }

    @Test
    public void konstruktoriAsettaaSaldonOikein() {
        assertEquals("Kortilla on rahaa 10.0 euroa",  kortti.toString());
    }
    @Test
    public void syoEdullisestiVahentaaSaldoaOikein() {
        kortti.syoEdullisesti();
        assertEquals("Kortilla on rahaa 7.5 euroa", kortti.toString());
    }
    @Test
    public void syoEdullisestiEiVieSaldoaNegatiiviseksi() {
        kortti.syoMaukkaasti();
        kortti.syoMaukkaasti();
        // nyt kortin saldo on 2
        kortti.syoEdullisesti();
        assertEquals("Kortilla on rahaa 2.0 euroa", kortti.toString());
    }  
    
    @Test
    public void kortilleVoiLadataRahaa() {
        kortti.lataaRahaa(25);
        assertEquals("Kortilla on rahaa 35.0 euroa", kortti.toString());
    }
    
    @Test
    public void kortinSaldoEiYlitaMaksimiarvoa() {
        kortti.lataaRahaa(200);
        assertEquals("Kortilla on rahaa 150.0 euroa", kortti.toString());
    }
    @Test
    public void syoMaukkaastiEiVieSaldoaNegatiiviseksi() {
        kortti.syoMaukkaasti();
        kortti.syoMaukkaasti();
        // nyt kortin saldo on 2
        kortti.syoMaukkaasti();
        assertEquals("Kortilla on rahaa 2.0 euroa", kortti.toString());
    } 
    @Test
    public void negatiivinenLatausEiVaikutaSaldoon() {
        kortti.lataaRahaa(-12.00);
        assertEquals("Kortilla on rahaa 10.0 euroa", kortti.toString());
    }
    @Test 
    public void voiOstaaEdullisenLounaanKunTasasumma() {
        Maksukortti edullinenKortti = new Maksukortti(2.50);
        edullinenKortti.syoEdullisesti();
        assertEquals("Kortilla on rahaa 0.0 euroa", edullinenKortti.toString());
    }
    @Test 
    public void voiOstaaMaukkaanLounaanKunTasasumma() {
        Maksukortti maukasKortti = new Maksukortti(4.0);
        maukasKortti.syoMaukkaasti();
        assertEquals("Kortilla on rahaa 0.0 euroa", maukasKortti.toString());
    }
}
