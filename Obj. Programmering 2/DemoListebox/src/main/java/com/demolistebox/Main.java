package com.demolistebox;

import javafx.application.Application;
import javafx.beans.Observable;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import javax.swing.*;
import java.io.IOException;
import java.util.ArrayList;

public class Main extends Application {

    // Definerer en listeboks:
    private ListView liste;

    // Lager modell-delen, her en ArrayList string
    private ArrayList<String> ukedager = new ArrayList<>();

    @Override
    public void start(Stage vindu) throws IOException {
        //FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("hello-view.fxml"));

        vindu.setTitle("Demo av listeboks");

        // Lager listeboksen
        liste = new ListView();
        // Legger inn ukedagene i ArrayList'en:
        ukedager.add("Mandag");
        ukedager.add("Tirsdag");
        ukedager.add("Onsdag");
        ukedager.add("Torsdag");
        ukedager.add("Fredag");
        ukedager.add("Lørdag");
        ukedager.add("Søndag");

        // Lager kontrollobjektet:
        ObservableList<String> innhold = FXCollections.observableArrayList();
        // Legger ukedagene inn i listen:
        innhold.addAll(ukedager);
        // Knytter kontrollobjektet til listeboksen:
        liste.setItems(innhold);

        // Lager en knapp:
        Button knapp = new Button("Les valg");
        knapp.setOnAction(e -> behandleValg());

        // Panel for å styre layout
        BorderPane root = new BorderPane();

        // Legger inn listeboks & knapp
        root.setCenter(liste);
        root.setBottom(knapp);

        // Viser root
        Scene scene = new Scene(root, 320, 240);
        vindu.setScene(scene);
        vindu.show();
    }

    // Lytteren for knappen:
    public void behandleValg() {

        // Hente ut valg i listeboksen: Default er single selection, men vi kan også sette multiple selection....
        // Uansett leses valgene inn i en ny observablelist
        ObservableList valgtEelementer  = liste.getSelectionModel().getSelectedIndices();

        // Siden vi har single selection ligger valget på plass 0 i valgteElementer
        // Det vi henter er index til valgt ukedag i den orginale ArrayList'en:
        int indeks = (int)valgtEelementer.get(0);

        // Så kan vi skrive ut valgt ukedag:
        System.out.println(ukedager.get(indeks));

    }


    public static void main(String[] args) {
        launch();
    }
}