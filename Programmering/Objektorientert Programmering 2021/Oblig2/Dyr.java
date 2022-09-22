package trond.Oblig2;

import java.text.Collator;
import java.util.ArrayList;

public class Dyr {
	private String id;
	private char kj�nn;
	private double lengde;
	private double vekt;
	private String fangststed;
	private String dato;
	public ArrayList<Gjenfangst> gjenfangster = new ArrayList<Gjenfangst>();
	private final static Collator KOLLATOR = Collator.getInstance();

	public Dyr(String i,char k,double l,double v,String s,String d) {
		id = i;
		kj�nn = k;
		lengde = l;
		vekt = v;
		fangststed = s;
		dato = d;
	} //Konstrukt�r
	
	public int compareTo(Dyr dyr) {
		return KOLLATOR.compare(this.id,dyr.id);
	}
		
	public boolean equals(Dyr dyr) {
		return KOLLATOR.equals(this.id,dyr.id);
	}

	public ArrayList<Gjenfangst> hentFangster() {
		return gjenfangster;
	}

	public String hentId() {
		return id;
	}

	public char hentKj�nn() {
		return kj�nn;
	}

	public double hentLengde() {
		return lengde;
	}

	public double hentVekt() {
		return vekt;
	}

	public String hentSted() {
		return fangststed;
	}

	public String hentDato() {
		return dato;
	}

	public void regGjenfangst(Gjenfangst g) {
		gjenfangster.add(g);
	}
	
	public ArrayList<Gjenfangst> getGjenfangst() {
		return gjenfangster;
	}
	
	
	
	public String toString() {
		return "ID: " + id + "    " + kj�nn + "    " + lengde + "    " + vekt + "    " + fangststed + "    " + dato;
	}



}
