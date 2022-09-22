module com.demofargerektangel {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.demofargerektangel to javafx.fxml;
    exports com.demofargerektangel;
}