module com.example.demofarge12november {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demofarge12november to javafx.fxml;
    exports com.example.demofarge12november;
}