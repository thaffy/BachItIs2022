package trond.Oblig2;

public class Gaupe extends Dyr {
	double �retustlengde;
	
	public Gaupe(String i,char k,double l,double v,String s,String d,double �tl) {
		super(i,k,l,v,s,d);
		this.�retustlengde = �tl;
	} //Konstrukt�r
	
	@Override
	public String toString() {
		return super.toString() + "\t" + �retustlengde;
	}
	
	public double get�retustlengde() {
		return �retustlengde;
	}	

}
