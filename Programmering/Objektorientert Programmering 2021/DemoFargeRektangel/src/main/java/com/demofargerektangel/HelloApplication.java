package com.demofargerektangel;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {

    String[] farger = new String["RØD","BLÅ","GRØNN"];
    Rectangle rektangel;
    ComboBox<String> fargevalg;
    @Override
    public void start(Stage primaryStage) throws IOException {
        BorderPane root = new BorderPane();

        // Vbox til radioknappene
        VBox knappepanel = new VBox();
        VBox combopanel = new VBox();

        // Lager comboboksen, legger fargene inn og setter tittel
        fargevalg = new ComboBox();
        fargevalg.getItems().addAll(farger);
        fargevalg.setValue("Fargevalg");
        fargevalg.getOnAction(e -> behandleValg());

        // Legger combopanelet inn i borderpane, legger inn knappepanelet
        root.setLeft(combopanel);
        root.setRight(knappepanel);

        // Lager avkrysningsbokser:
        CheckBox rød = new CheckBox("RØD");
        CheckBox blå = new CheckBox("Blå");
        CheckBox grønn = new CheckBox("Grønn");

        // Legger inn i knappepanelet
        knappepanel.getChildren().addAll(rød,blå,grønn);

        // Legger inn i combopanel
        combopanel.getChildren().add(fargevalg);

        // Lager rektangelet, setter posisjon
        rektangel = new Rectangle();
        rektangel.setX(150.0f);
        rektangel.setY(75.0);
        rektangel.setWidth(200.0);
        rektangel.setHeight(100.0);
        rektangel.setFill(Color.RED); // Setter grunnfarge

        // Legger inn i rootpanelet
        root.setCenter(rektangel);

        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        primaryStage.setTitle("Hello!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public void behandleValg() {
        // Henter valget fra comboboksen:
        String valg = fargevalg.getValue();
        if (valg.equals("RØD")) rektangel.setFill(Color.RED);
        else if (valg.equals("BLÅ")) rektangel.setFill(Color.BLUE);
        else rektangel.setFill(Color.GREEN);
    }

    public static void main(String[] args) {
        launch();
    }
}