module com.tabell.demotabell {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.tabell.demotabell to javafx.fxml;
    exports com.tabell.demotabell;
}