package com.tabell.demotabell;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.FlowPane;
import javafx.stage.Stage;

import java.io.IOException;

public class Main extends Application {

    // Oppretter et tabellobjekt:
    private TableView tabell = new TableView();

    // Oppretter obserablelist, med et par personer...
    private ObservableList<Person> data = FXCollections.observableArrayList(
            new Person("Ole Brum","Hundremeterskogen","123456789"),
            new Person("Naseed Al-Nøff","Grisebankbakken","987654321"));

    private TextField nyttnavn,nyadresse,nytelefon;

    @Override
    public void start(Stage stage) throws IOException {
        // FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("hello-view.fxml"));

        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 400, 400);
        stage.setTitle("Demo av enkel tabell");

        // Setter størrelsen på vinduet:
        stage.setWidth(300);
        stage.setHeight(400);

        // Oppretter kolonner for tabellen (og setter bredde):
        TableColumn colNavn = new TableColumn("Navn"); colNavn.setMinWidth(100);
        TableColumn colAdresse = new TableColumn("Adresse"); colAdresse.setMinWidth(100);
        TableColumn colTelefon = new TableColumn("Telefon"); colTelefon.setMinWidth(100);

        // Vi trenger nå et objekt som henter ut verdier fra personobjektene:
        colNavn.setCellValueFactory(new PropertyValueFactory<Person,String>("navn"));
        colAdresse.setCellValueFactory(new PropertyValueFactory<Person,String>("adresse"));
        colTelefon.setCellValueFactory(new PropertyValueFactory<Person,String>("telefon"));

        // Legger kolonne til tabellen:
        tabell.getColumns().addAll(colNavn,colAdresse,colTelefon);
        // Legger observablelista data til tabellen
        tabell.setItems(data);

        // Layout
        root.setTop(new Label("Telefonliste"));
        root.setCenter(tabell);

        // Flowpane for tekstfelter og knapp
        FlowPane registreringspanel = new FlowPane();

        // Lager registreringsfelter ( og bakgrunnstekst + bredde)
        nyttnavn = new TextField(); nyttnavn.setPromptText("Navn"); nyttnavn.setMaxWidth(colNavn.getPrefWidth());
        nyadresse = new TextField(); nyadresse.setPromptText("Adresse"); nyadresse.setMaxWidth(colAdresse.getPrefWidth());
        nytelefon = new TextField(); nytelefon.setPromptText("Telefon"); nytelefon.setMaxWidth(colTelefon.getPrefWidth());

        // Lager en knapp for registrering
        Button knapp = new Button("Legg til");
        knapp.setOnAction(e -> behandleNy());

        // Legger tekstfelter og knapp til i flowpane'et:
        registreringspanel.getChildren().addAll(nyttnavn,nyadresse,nytelefon,knapp);
        root.setBottom(registreringspanel);

        stage.setScene(scene);
        stage.show();
    }

    public void behandleNy() {
        // Når det trykkes på knappen, lages et nytt Person-objekt som da legges til i data
        data.add(new Person(nyttnavn.getText(),nyadresse.getText(),nytelefon.getText()));
    }

    public static void main(String[] args) {
        launch();
    }
}