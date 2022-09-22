package com.example.main;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.FlowPane;
import javafx.event.ActionEvent;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    // Må deklareres globalt:
    TextField navn; // For å skrive navn.
    Label hilsen; // For å skrive hilsen.
    @Override
    public void start(Stage primaryStage) {
        try {
            // Skifter til FlowPane
            FlowPane root = new FlowPane();
            Button ok = new Button("OK");
            // Knytter knappen til lytteren:
            ok.setOnAction(e -> behandleKlikk());
            Label ledetekst = new Label("Hva heter du?");

            // Lager objektet
            navn = new TextField();

            // Setter bredden på tekstfeltet:
            navn.setPrefColumnCount(15);

            // Lager label'en hilsen
            hilsen = new Label();

            // Legger objektene inn i panelet:
            root.getChildren().addAll(ledetekst,navn,ok,hilsen);

            Scene scene = new Scene(root,400,400);
            scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
            primaryStage.setScene(scene);
            primaryStage.show();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
    public void behandleKlikk() {
        hilsen.setText("Hei på deg, " + navn.getText());

    }

    public static void main(String[] args) {
        launch();
    }
}