module com.demolistebox {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;
    requires java.desktop;

    opens com.demolistebox to javafx.fxml;
    exports com.demolistebox;
}