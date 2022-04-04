module com.oad2.oad_arbkrav2 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.oad2.oad_arbkrav2 to javafx.fxml;
    exports com.oad2.oad_arbkrav2;
}