module com.example.demo29okt {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demo29okt to javafx.fxml;
    exports com.example.demo29okt;
}