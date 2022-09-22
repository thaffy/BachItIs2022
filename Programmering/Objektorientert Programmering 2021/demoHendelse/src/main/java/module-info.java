module com.example.demohendelse {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demohendelse to javafx.fxml;
    exports com.example.demohendelse;
}