import java.util.*;

import javax.swing.JOptionPane;

import java.io.*;
public class Bilregister {
	ArrayList<Person> personer = new ArrayList<Person>();
	ArrayList<Postadresse> postadresser = new ArrayList<Postadresse>();
	ArrayList<Bil> biler = new ArrayList<Bil>();
	private String postfil = "postnummere.txt";
	
	public Postadresse postadresse(String pnr){
		Collections.sort(postadresser);
		for(int i = 0;i < postadresser.size();i++) {
			Postadresse padr = postadresser.get(i);
			if(padr.getPnr().equals(pnr)) return padr;
		}
		return null;		
	}
	
	public void regEier(String enavn,String fnavn,Postadresse postadr) {
		personer.add(new Person(enavn,fnavn,postadr));
	}
	
	public void regPost(String pnr,String pnavn) {
		postadresser.add(new Postadresse(pnr,pnavn));
	}
	
	public void regBil(String regnr,String merke,Person p) {
		Bil nybil = new Bil(regnr,merke,p);
		biler.add(nybil);
		p.regBil(nybil);
	}
	
	public Person getPerson(String enavn) {
		for(int i = 0;i < personer.size();i++) {
			Person p = personer.get(i);
			if(p.getNavn().equals(enavn)) return p;
		}
		return null;
	}
	
	public Postadresse finnPostadresse(String postnr) {
		for(int i = 0; i < postadresser.size(); i++) {
			Postadresse pa = postadresser.get(i);
			if(pa.getPnr().equals(postnr)) return pa;
		}
		return null;
	}
	
	
	public BufferedReader leseFil(String filnavn) {
		BufferedReader innfil=null;
		try {
			File f=new File(filnavn);
	 		FileInputStream fs=new FileInputStream(f);
	 		InputStreamReader isr=new InputStreamReader(fs);
			innfil=new BufferedReader(isr);
		} catch(Exception e) {}
		return innfil;
	} //Slutt metode

	//Allokerer fil for skriving:
	public PrintStream skriveFil(String filnavn) {
		PrintStream utfil=null;
		try {
			utfil=new PrintStream(new FileOutputStream(new File(filnavn)));
		}catch(Exception e){}
		return utfil;
	} //Slutt metode
	
	public void skrivPostnummer(String filnavn) {
		PrintStream utfil = null;
		try {
			utfil = skriveFil(filnavn);
			for(int i = 0;i < postadresser.size();i++) {
				utfil.println(postadresser.get(i).toFile());
			}
			//utfil.close();
		}catch(Exception e){}
		finally {
			try {
				if(utfil != null) utfil.close();
			}catch(Exception e){}
		}
	}
	
	public void lesPostnummer(String postfil) throws Exception {
		BufferedReader innpost = leseFil(postfil);
		String innlinje;
		StringTokenizer inndata;
		try {
			while(innpost.ready()) {
				innlinje = innpost.readLine();
				inndata = new StringTokenizer(innlinje,",");
				while(inndata.hasMoreTokens()) {
					String pnr = inndata.nextToken();
					String pnavn = inndata.nextToken();
					Postadresse nypost = new Postadresse(pnr,pnavn);
					postadresser.add(nypost);
				} //innlesing av bil
			} //innlesing av biler
			//innpost.close();
		}catch(Exception e) {throw new Exception("Kan ikke lese postadressefil");}
		finally {
			try {
				if(innpost != null) innpost.close();
			}catch(Exception e){}
		}
	}
	
	public void lesEiere(String fil) throws Exception {
		BufferedReader inneier = null;
		String innlinje;
		StringTokenizer inndata;
		try {			
			inneier = leseFil(fil);			
			while(inneier.ready()) {
				innlinje = inneier.readLine();
				inndata = new StringTokenizer(innlinje,",");
				while(inndata.hasMoreTokens()) {
					String enavn = inndata.nextToken();
					String fnavn = inndata.nextToken();
					String pnr = inndata.nextToken();
					Postadresse padr = finnPostadresse(pnr);
					Person nyeier = new Person(enavn,fnavn,padr);
					personer.add(nyeier);
				} //innlesing av bil
			} //innlesing av biler
			inneier.close();
		}catch(Exception e){throw new Exception("Kan ikke lese eierfil");}
		finally {
			try {
				if(inneier != null) inneier.close();
			}catch(Exception e){throw new Exception("kan ikke lukke eierfil");}
		}
	}
	
	public void lesBiler(String bilfil) throws Exception {
		BufferedReader innbil = null;	
		String innlinje;
		StringTokenizer inndata;
		try {
			innbil = leseFil(bilfil);
			while(innbil.ready()) {
				innlinje = innbil.readLine();
				inndata = new StringTokenizer(innlinje,",");
				while(inndata.hasMoreTokens()) {
					String eiernavn = inndata.nextToken();
					String regnr = inndata.nextToken();
					String merke = inndata.nextToken();					
					Person eieren = finnEier(eiernavn);
					Bil nybil = new Bil(regnr,merke,eieren);
					biler.add(nybil);	
					eieren.regBil(nybil);
				} //innlesing av bil
			} //innlesing av biler
			innbil.close();
		}catch(Exception e){throw new Exception("Kan ikke lese bilfil");}
		finally {
			try {
				if(innbil != null) innbil.close();
			}catch(Exception e){throw new Exception("kan ikke lukke bilfil");}
		} //finally
	}

	
	public void lesFil(String bilfil,String eierfil,String postfil) throws Exception {
		try {
			lesPostnummer(postfil);
			lesEiere(eierfil);
			lesBiler(bilfil);
		}catch(Exception e){throw e;}		
	}

	public void skrivFil(String bilfil,String eierfil,String postfil) throws Exception {
		PrintStream utbil = null;
		PrintStream uteier = null;
		try {
		utbil = skriveFil(bilfil);
		uteier = skriveFil(eierfil);
		int teller = 0;
		skrivPostnummer(postfil);
		while(teller < personer.size()) {
			Person eneier = personer.get(teller);
			uteier.println(eneier.toFile());
			teller++;
		}//while
		uteier.close();
		teller = 0;
		while(teller < biler.size()) {
			Bil enbil = biler.get(teller);
			utbil.println(enbil.toFile());
			teller++;
		}//while
		utbil.close();
		}catch(Exception e){throw new Exception("Kan ikke lese postadressefil");}
		//System.out.println("Data er lagret");
		finally {
			try {
				if(uteier != null) uteier.close();
				if(utbil != null) utbil.close();
			}catch(Exception e){}
		}
	} //metode

	public Person finnEier(String enavn) {
		boolean funnet = false;
		int teller = 0;
		Person eneier = null;
		while(!funnet) {
			eneier = personer.get(teller);
			eneier.getNavn();
			if(eneier.getNavn().equals(enavn)) funnet = true;
			else teller++;
		}
		return eneier;
	}

	public ArrayList hentBiler() {
		return biler;
	}

	public ArrayList hentEiere() {
		return personer;
	}



}
